import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formatdate
import os
import csv  # Import the csv module
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your email credentials
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

# Read HR contacts from CSV file using pandas
df = pd.read_csv('hr_contacts.csv')

# Create a list to store successfully sent email IDs
sent_emails = []

# Iterate through each HR contact and send individual emails
for index, row in df.iterrows():
    # Create the email message for this HR contact
    subject = 'Application for full stack python developer'
    body = f"Hello,\n\n"
    body += "I am a full-stack Python developer, proficient in Python, Django, MySQL, and front-end technologies. "
    body += "I offer strong problem-solving and communication skills. Eager to contribute to the company's success "
    body += "and learn in a dynamic environment. My resume is attached. I look forward to discussing how I can add "
    body += "value to your team.\n\n"
    body += "Best regards,\nMilan Jakhaniya,\nCell: (+91) 8000097325,\nEmail: milanpatel1082@gmail.com\n"
    
    sender_name = "Milan Jakhaniya"
    resume_file = 'milan_cv.pdf'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = row['email']  # Send to the specific HR email for this iteration
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    with open(resume_file, 'rb') as resume:
        part = MIMEApplication(resume.read(), Name='milan_cv.pdf')
        part['Content-Disposition'] = f'attachment; filename="{resume_file}"'
        msg.attach(part)

    # Send the email for this HR contact
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        text = msg.as_string()
        smtp_server.sendmail(sender_email, row['email'], text)

        smtp_server.quit()
        print(f'Resume sent successfully to HR: {row["email"]}, Email: {row["email"]}')
        
        # Append the successfully sent email ID to the list
        sent_emails.append(row['email'])

    except Exception as e:
        print(f'An error occurred while sending to HR: {row["email"]}, Email: {row["email"]}: {e}')

# After sending all emails, open sentbox.csv in append mode and write the email IDs
with open('sentbox.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['Sent Emails'])  # Add a header if necessary
    for email in sent_emails:
        writer.writerow([email])







# import smtplib
# import pandas as pd
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.utils import formatdate
# import os
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv()

# # Your email credentials
# sender_email = os.getenv("SENDER_EMAIL")
# sender_password = os.getenv("SENDER_PASSWORD")

# # Read HR contacts from CSV file using pandas
# df = pd.read_csv('hr_contacts.csv')

# # Iterate through each HR contact and send individual emails
# for index, row in df.iterrows():
#     # Create the email message for this HR contact
#     subject = 'Application for full stack python developer'
#     body = f"Hello,\n\n"
#     body += "I am a full-stack Python developer, proficient in Python, Django, MySQL, and front-end technologies. "
#     body += "I offer strong problem-solving and communication skills. Eager to contribute to the company's success "
#     body += "and learn in a dynamic environment. My resume is attached. I look forward to discussing how I can add "
#     body += "value to your team.\n\n"
#     body += "Best regards,\nMilan Jakhaniya,\nCell: (+91) 8000097325,\nEmail: milanpatel1082@gmail.com\n"
    
#     sender_name = "Milan Jakhaniya"
#     resume_file = 'milan_cv.pdf'

#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = row['email']  # Send to the specific HR email for this iteration
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(body))

#     with open(resume_file, 'rb') as resume:
#         part = MIMEApplication(resume.read(), Name='milan_cv.pdf')
#         part['Content-Disposition'] = f'attachment; filename="{resume_file}"'
#         msg.attach(part)

#     # Send the email for this HR contact
#     try:
#         smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
#         smtp_server.starttls()
#         smtp_server.login(sender_email, sender_password)

#         text = msg.as_string()
#         smtp_server.sendmail(sender_email, row['email'], text)

#         smtp_server.quit()
#         print(f'Resume sent successfully to HR: {row["email"]}, Email: {row["email"]}')

#     except Exception as e:
#         print(f'An error occurred while sending to HR: {row["email"]}, Email: {row["email"]}: {e}')