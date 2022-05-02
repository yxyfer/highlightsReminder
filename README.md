[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# highlightsReminder
A simple Project that allows you to save your Kindle Highlights and be sent a mail with a random selection everyday


# How to use

## Getting started

### Get the highlights data
- Download your highlights from kindle in the json form (explanation soon to come)
- run 
```python3
from highlights.kindle_parser import HighlightsParserKindle
HighlightsParserKindle()
```
- ___NOTE___: a better version will be released very soon

### .ENV setUP:

To send yourself emails you'll need a sender's email and a receiver's email.

```shell
# Create a .env
cp .env.template .env
# Open the .env file you just created
vim .env
```

You can now add your sender's email and password and the recipient's email.

___NOTE___: I am in no case responsible if you push your code online or get it stolen in anyway. I advise you to create a fake email with a random password that you use just for this. (Later on the code will function through access tokens which are more secure, but for now it isn't the case). You are responsible for protecting your password :)
. 
### Run the solution:

```shell
cd highlightsReminder
python3 main.py
```

### GOING further (Automation):

#### Using the solution on a server(/computer that runs all the time)

In crontab add the following line to receive a mail everyday at 6:45pm:

```crontab
# /etc/crontab

45 18 * * * pi cd /<your_path_to_the_folder>/highlightsReminder/; $(which python3) main.py >> ~/cron.log 2>&1

```
