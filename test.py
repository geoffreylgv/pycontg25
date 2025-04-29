import smtplib
import ssl

smtp_server = "pytogo.org"
port = 465  # For starttls
sender_email = "ibrahim@pytogo.org"
password = "W@$$iou9827"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
server = smtplib.SMTP("pytogo.org", 465)
try:
    
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email
    receiver_email = "wachioubouraima56@gmail.com"
    message = """\
    Subject: Hi there
    This message is sent from Python."""
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()