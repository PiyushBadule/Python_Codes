import smtplib

def send_email_to_multiple_users(subject, message_body, recipient_emails):
    """
    Send an email to multiple users using Gmail's SMTP server.

    Args:
    subject (str): Subject line of the email.
    message_body (str): The main content of the email.
    recipient_emails (list): List of recipient email addresses.

    Returns:
    None
    """
    try:
        # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'sender@gmail.com'  # Replace with your email
        sender_password = ''  # Replace with your email password

        # Establish a secure session with the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Prepare the email message
        message = f'Subject: {subject}\n\n{message_body}'

        # Sending the email to each recipient in the list
        for recipient_email in recipient_emails:
            server.sendmail(sender_email, recipient_email, message)

        # Terminate the SMTP session
        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to send an email to multiple users.
    """
    subject = "Testing sending using gmail"
    message_body = "Message You Need to Send Write Here"
    recipient_emails = ["user1@gmail.com", "user2@gmail.com"]

    send_email_to_multiple_users(subject, message_body, recipient_emails)
    print("Emails sent successfully.")

if __name__ == "__main__":
    main()

# If you get the error "smtplib.SMTPAuthenticationError:"

# Go to this link and select Turn On

# https://www.google.com/settings/security/lesssecureapps
