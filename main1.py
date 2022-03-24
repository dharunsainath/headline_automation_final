import requests  # http requests

from bs4 import BeautifulSoup  # web scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''


# extracting Hacker News Stories

def main1project(email):


    cnt = extract_news()
    content += cnt
    content += ('<br>------<br>')
    content += ('<br><br>End of Message')

    # lets send the email

    print('Composing Email...')

    # update your email details
    # make sure to update the Google Low App Access settings before







