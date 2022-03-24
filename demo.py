import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("pythonsaitan@outlook.com", "Viratkohli@18")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("pythonsaitan@outlook.com", "kcvijay247@gmail.com", message)

# terminating the session
s.quit()