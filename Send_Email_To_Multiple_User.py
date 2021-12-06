import smtplib

EMAIL_HOST_USER = 'sender@gmail.com'
EMAIL_HOST_PASSWORD = ''

# list of email_id to send the mail
list1 = ["user1@gmail.com", "user2@gmail.com"]
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
Text = "Message You Need to Send Write Here"
SUBJECT = "Testing sending using gmail"
message = 'Subject: {}\n\n{}'.format(SUBJECT, Text)

for li in list1:
	s.sendmail(EMAIL_HOST_USER, li, message)
s.quit()

# If you get the error "smtplib.SMTPAuthenticationError:"

# Go to this link and select Turn On

# https://www.google.com/settings/security/lesssecureapps