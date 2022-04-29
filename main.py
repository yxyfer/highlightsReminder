import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from mailer.sending_information import SENDINGinformation
from highlights_reminder import kindle_highlights, Quote


# def __main__():
sending_info = SENDINGinformation()

message = MIMEMultipart("alternative")
message["Subject"] = "Daily 5 - Book Quotes"
message["From"] = sending_info.ENV_SENDER_EMAIL
message["To"] = sending_info.ENV_RECIPIENT_EMAIL
text = ""
html = """\
<style>
@media screen and (max-width: 530px) {
    .blockquote p {
        font-family: 'Times New Roman';
        font-size: 26px;
        font-weight: bold;
    }

    .blockquote:before {
        position: absolute;
        font-family: 'Times New Roman';
        top: 0;
        line-height: .655;
        left: -10px;
        content: '“';
        font-size: 250px;
        color: rgba(0,0,0,0.1);
    }
}
@media screen and (min-width: 531px) {
    .blockquote p {
        font-family: 'Times New Roman';
        font-size: 26px;
        font-weight: bold;
    }

    .blockquote:before {
        position: absolute;
        font-family:  'Times New Roman';
        top: 0;
        line-height: .655;
        left: -50px;
        content: '“';
        font-size: 250px;
        color: rgba(0,0,0,0.1);
    }
}
table { 
	border-spacing: 0px 30px;
}
.blockquote {
    position: relative;
}

.container {
    border-radius: 25px;
    border: 2px solid #73AD21;
    padding: 20px;
	height: auto;
}
.quote_info {
    text-align: right;
}
H5.title {
    text-decoration: underline;
 	margin-top: 0;
    margin-bottom: 0;
    line-height: 1;
    font-size: 15px;
}
H6.authors {
	color: grey;
    margin: 0;
    padding: 0;
    font-size: 13px;
}
.quote {
    text-align: justify;
    font-size: 21px;
}
</style>
<html>
  <body>
    <h1> Matt's Daily Quotes </h1>

    <table width='100%' align='center' border='0' cellspacing='0' cellpadding='0'>
        <tr>
            <td align="center">
                <table width="600" border="0" cellspacing="0" cellpadding="0">
"""

kindle_highlights = kindle_highlights("books")

for quote in kindle_highlights.get_daily_n(5):
    html += "<tr style='padding-top: 20px;'>"
    html += "<td align='center' class='container'>"
    html += (
        "<blockquote class='blockquote'><p class='quote'>"
        + quote.quote
        + "</p></blockquote>"
    )
    html += "<div class ='quote_info'>"
    html += "<H5 class ='title'>" + quote.title + "</H5>"
    html += "<H6 class='authors'>by: " + quote.authors + "</H6>"
    html += "</div></td></tr>"

html += """
                </table>
            </td>
        </tr>
    </table>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sending_info.ENV_SENDER_EMAIL, sending_info.ENV_SENDER_PASSWORD)
    server.sendmail(
        sending_info.ENV_SENDER_EMAIL,
        sending_info.ENV_RECIPIENT_EMAIL,
        message.as_string(),
    )
