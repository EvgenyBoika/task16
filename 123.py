#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from subprocess import check_output

# Get the git log --stat entry of the new commit
log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])

# Create a plaintext email message
msg = MIMEText("Look, I'm actually doing some work:\n\n%s" % log)

msg['Subject'] = 'Git post-commit hook notification'
msg['From'] = 'heka51shok@gmail.com'
msg['To'] = 'dealfreee@gmail.com'

# Send the message
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo()
session.login(msg['From'], '2335heka51_shok')

session.sendmail(msg['From'], msg['To'], msg.as_string())
session.quit()