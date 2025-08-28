import smtplib #Simple Mail Transer Protocol for sending emails
import os
import csv
#For creating multipart email message
from email.mime.multipart import MIMEMultipart 
#For adding plain text to email body
from email.mime.text import MIMEText

SMTP_SERVER='smtp.gmail.com'
SMTP_PORT = 587 #port used for (TLS) "encryption".
SENDER_EMAIL='srasool6371@gmail.com'
SENDER_PASSWORD='ygyw yraa hnfh saox'

def send_email(to_email,subject,body):
    try:
        msg=MIMEMultipart()
        msg['From']=SENDER_EMAIL
        msg['To']=to_email
        msg['Subject'] =subject
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,to_email,msg.as_string())

        print(f'Email sent to {to_email}')
    
    except Exception as e:
        print(f'Error sending email to {to_email} : {e}')

def send_bulk_emails(csv_file,subject,body):
    try:
        csv_path=os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: csv file '{csv_file}' not found.")
            return
        
        with open(csv_path,newline="",encoding='utf-8') as file:
            reader=csv.reader(file)
            next(reader,None)
            print(reader,'reader')
            for row in reader:
                if row:
                    email=row[0]
                    send_email(email,subject,body)
    
    except Exception as e:
        print(f'Error reading csv file: {e}')