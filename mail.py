import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# SMTPLİB MAİL PROGRAMI
usr_mail = input("Mail : ")
usr_passwd = input("Password : ")
mesaj = MIMEMultipart()
mesaj["From"] = usr_mail
mesaj["To"]   = input("To : ")

mesaj["Subject"] = input("Title : ")

yazi = input("""
## BODY ##
== >>
""")

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) # sunucu seçtik
    mail.ehlo()  # bağlandık

    mail.starttls() #encrypt edilme
    mail.login(usr_mail,usr_passwd) #servera bağlanma
    #           mail     şifre

    # GÖNDERME AŞAMASI

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail Başarıyla Gönderildi !")
    mail.close()
except:
    sys.stderr.write("Bir Sorun Oluştu!")
    sys.stderr.flush()