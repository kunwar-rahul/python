#******************************************************************************************#
#	Author : kunwar-rahul (Rahul Kunwar)												   #
#   																					   #
#   In order to make this code work one needs to login into the gmail account that one 	   #
#   wants to use and then go to this link below and turn off Access for less secure apps   #
#	https://www.google.com/settings/security/lesssecureapps                                #
#                                                                                          #
#                                                                                          #
#******************************************************************************************#
import smtplib
import socks

#if one is behind proxy otherwise comment out
socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, 'www.proxy.com', port=XXXX)
socks.wrapmodule(smtplib)

smtpserver = 'smtp.gmail.com'
smtpuser = 'sender@gmail.com'  
smtppass = 'password'  

RECIPIENTS = ['user1@gmail.com', 'user2@example.com']
SENDER = 'sender@gmail.com'
SUBJECT = "<Subject>"

HEADER = ("From: %s\r\nSubject: %s\r\nTo: %s\r\n\r\n"
       % (SENDER, SUBJECT, ", ".join(RECIPIENTS)))
BODY = "<Message Body> \r\n"

MSG = HEADER + BODY

server = smtplib.SMTP(smtpserver,25)
server.ehlo()
server.starttls() 
server.ehlo()
server.login(smtpuser,smtppass)
server.set_debuglevel(1)
server.sendmail(SENDER, RECIPIENTS, MSG)
server.quit()
print('Mail sent successfully')