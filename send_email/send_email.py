import smtplib

host="smtp.gmail.com"
port=587
username="username@gmail.com"
password="password"
from_email = username
to_list=[ "zhongturtle@gmail.com"]


email_conn=smtplib.SMTP(host,port) #make connect
email_conn.ehlo()  #test whether the connect is ready
email_conn.starttls() #enables upgrading otherwise plaintext communication between clients and mail servers, to encrypted communication.
email_conn.login(username,password) #login 
email_conn.sendmail(from_email, to_list, "hello there this is an email message")#send email ,which's format like from "from_email" to "to_list" with text "hello there there"

email_conn.quit() #disconnect

from smtplib import SMTP


ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "Hello there this is an email message")
ABC.quit()


from smtplib import SMTP, SMTPAuthenticationError, SMTPException


pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong_password")
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

pass_wrong.quit()

