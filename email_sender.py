from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
def email_send(email,content):

    SERVER = 'smtp.gmail.com'  # "your smtp server"
    PORT = 587  # your port number
    FROM = 'harleypy4@gmail.com'  # "your from email id"
    TO = email  # "your to email ids"  # can be a list
    PASS = 'harleypython@4'  # "your email id's password"

    # fp = open(file_name, 'rb')
    # Create a text/plain message
    # msg = MIMEText('')
    msg = MIMEMultipart()

    # msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
    msg['Subject'] = 'Top News Stories HN [Automated Email]'
    msg['From'] = FROM
    msg['To'] = TO

    msg.attach(MIMEText(content, 'html'))
    # fp.close()

    print('Initiating Server...')

    server = smtplib.SMTP(SERVER, PORT)
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    # server.ehlo
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())

    print('Email Sent...')

    server.quit()

#email_send("kcvijay247@gmail.com","this is a sample mail")