from smtplib import SMTP


host = "smtp.gmail.com"
port = 587
username = "example@gmail.com" # Your email address
password = "example" # Your password
from_email = username # email_address = username
to_list = ["example@gmail.com"] # List of users you want to send messages to.


server_connection = SMTP( host, port)
server_connection.ehlo_or_helo_if_needed()
server_connection.starttls()
server_connection.login(username, password)
server_connection.sendmail(from_email, to_list, "Welcome to Python Mailing!" )
print("Mail sent successfully!")
server_connection.quit()
