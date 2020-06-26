
import ssl,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass as password

sender_email = input("Sender email : ")
password = password.getpass()
receiver_email = input("Reciever email : ")

message = MIMEMultipart("alternative")
message["Subject"] = "Python Assignmnt"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html = """
<html>
<body>
<h1>Hello,</h1>
<h3>Good evening</h3>
</body>
</html>
"""

# Turn html to MIMEText objects
mimeObj = MIMEText(html, "html")
# Attach MIMEMultipart message to message
message.attach(mimeObj)

# Create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login(sender_email, password)

# Send the mail
server.sendmail(sender_email, receiver_email, message.as_string())

server.quit()
