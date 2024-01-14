import smtplib

def send_email(subject, message_body, recipient_email):
    """
    Send an email using Gmail's SMTP server.

    Args:
    subject (str): Subject line of the email.
    message_body (str): The main content of the email.
    recipient_email (str): The recipient's email address.

    Returns:
    bool: True if email is sent successfully, False otherwise.
    """
    try:
        # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'sender@gmail.com'  # Replace with your email
        sender_password = 'password'  # Replace with your email password

        # Establish a secure session with the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Prepare the email message
        message = f'Subject: {subject}\n\n{message_body}'

        # Sending the email
        server.sendmail(sender_email, recipient_email, message)

        # Terminate the SMTP session
        server.quit()

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    """
    Main function to send an email.
    """
    subject = "Testing sending using gmail"
    message_body = "Message You Need to Send Write Here"
    recipient_email = "example@gmail.com"

    if send_email(subject, message_body, recipient_email):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")

if __name__ == "__main__":
    main()


# If you get the error "smtplib.SMTPAuthenticationError:"

# Go to this link and select Turn On

# https://www.google.com/settings/security/lesssecureapps
