# In order to send an email using Python, you can use the smtplib library. 
# This library allows sending email through Python using the SMTP protocol.
# The basic process of sending email in Python is as follows: Connect to SMTP server using username and password.
# Setting the email content including the email's sender, recipient, subject, and text. send mail. SMTP server disconnection.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
port = 587  # Port for starttls
sender_email = "YOUR_EMAIL_ADDRESS"  # Enter your address
password = input("Type your password and press enter: ")
receiver_email = "YOUR_EMAIL_ADDRESS"  # Enter receiver address

message = MIMEMultipart("alternative")
message["Subject"] = "Important update regarding our product"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML versions of your message
text = """\
Hi,
How are you? This is just a quick update to inform you about a new product feature that we have added.
Best,
Product Team"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you? This is just a quick update to inform you about a new product feature that we have added.<br>
       Best,<br>
       Product Team
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part1)
message.attach(part2)

# Login to the SMTP server
server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)

# Send the message
server.sendmail(sender_email, receiver_email, message.as_string())

# Cleanup
server.quit()

print("Email sent successfully!")
