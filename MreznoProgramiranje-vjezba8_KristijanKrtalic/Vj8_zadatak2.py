import smtplib

client = smtplib.SMTP('localhost',1025)

fromaddr = 'kristijan.krtalic002gmail.com'
toaddrs = 'kristijan.krtalic002@gmail.com'
msg = 'Hello'

client.sendmail(fromaddr, toaddrs, msg)
client.quit()