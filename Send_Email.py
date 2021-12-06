import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
EMAIL_HOST_USER = 'sender@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
Text = "Message You Need to Send Write Here"
SUBJECT = "Testing sending using gmail"
message = 'Subject: {}\n\n{}'.format(SUBJECT, Text)
s.sendmail(EMAIL_HOST_USER, "example@gmail.com", message)
s.quit()

# If you get the error "smtplib.SMTPAuthenticationError:"

# Go to this link and select Turn On

# https://www.google.com/settings/security/lesssecureapps