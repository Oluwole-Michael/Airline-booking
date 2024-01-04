from email.message import EmailMessage
import ssl
import smtplib
import random

from dotenv import load_dotenv
import os
load_dotenv()


def OTGGenerator(receivers, email_subject, email_body):
    try:
        for receiver in receivers:
            OTP = random.randint(100000, 999999)

            email_sender = 'airlinebookingapps@gmail.com'
            email_password = 'zuvxffjkbaynrhab'
            email_receiver = receiver

            subject = email_subject
            body = email_body+ str(OTP)

            mail = EmailMessage()
            mail['From'] = email_sender
            mail['To'] = email_receiver
            mail['Subject'] = subject
            mail.set_content(body)

            contxt = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contxt) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, mail.as_string())
        return "Email sent successfully!!!"

    except Exception as ex:
        print(ex)
        return ex
