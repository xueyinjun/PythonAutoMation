#utf-8

import smtplib

smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj = smtplib.SMTP_SSL('smtp.example.com',476)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Sincerely,Bob')
smtpObj.quit()

