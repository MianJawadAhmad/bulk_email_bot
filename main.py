import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('your email','password')
server.sendmail('from',
                'to',
                'Hay myself testing your code ;')
