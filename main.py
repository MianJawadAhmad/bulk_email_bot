import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('16pwbcs0531@uetpeshawar.edu.pk','adnan321')
server.sendmail('16pwbcs0531@uetpeshawar.edu.pk',
                'a.jawad321@gmail.com',
                'Hay myself testing your code ;')