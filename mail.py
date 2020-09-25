import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def SendMail():
    usr_mail = input("Mail : ")
    usr_passwd = input("Password : ")
    msg_to  = input("To : ")
    ImgFileName = input("File Name : ")
    subject = input("Title : ")
    body = input("Text : ")
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = usr_mail
    msg["To"]   = msg_to


    text = MIMEText(body)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(usr_mail,usr_passwd)
    s.sendmail(msg["From"],msg["To"],msg.as_string())
    
    s.quit()


while True: 
    print("""
            *************************
            | coded by root@ebby:~# |
            *************************
            |        Options        |
            *************************
            | 1. Text Sender        |
            *************************
            | 2. Text+Image Sender  |
            *************************
            | 9. Break              |
            *************************
                """)

    option = int(
        input("Option : ")
    )
    if option == 1:
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


    elif option == 2:
        SendMail()
    elif option == 9:
        exit()
    else:
        print("Please Select 1 or 2 !!!")


