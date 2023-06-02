SMTP_SERVER="SMTP.gmail.COM"
smtp_port = 587
smtp_username=os.getenv('from_email','')
smtp_password = os.getenv('email_password', '')

import smtplib


#aposs isso criar o mimemultpart e importar e instalar, seguir um passo a passo quando precisar