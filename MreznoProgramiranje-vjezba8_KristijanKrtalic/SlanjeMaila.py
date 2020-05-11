import smtplib

email_address=('KikiKrtalich007@gmail.com')
email_password=('xxxxxxx')

with smtplib.SMTP('smtp.gmail.com',587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(email_address,email_password)
    
    predmet='Python test za profesora'
    body='Pozdrav ovo je python test'
    
    Message=f'predmet:{predmet}\n\n{body}'
    
    smtp.sendmail(email_address, email_address ,Message)
    
    