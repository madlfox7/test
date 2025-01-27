import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

SMTP_SERVER = "smtp.gmail.com"  # For Gmail. Use the SMTP server for your email provider.
SMTP_PORT = 587
SENDER_EMAIL = "karsudz15@gmail.com"  # Replace with your email address
SENDER_PASSWORD = "dntk kcey gsxl wiuz"  # Replace with your email password or app password
RECEIVER_EMAIL = "karsudz15@gmail.com"  # Replace with the recipient's email address

def send_email_with_attachment(file_path):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = "Daily Report: p2.html"

        # Email body
        body = "Please find the attached p2.html file."
        msg.attach(MIMEText(body, "plain"))

        # Attach the file
        with open(file_path, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(file_path)}",
            )
            msg.attach(part)

        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

def file_contains_words(file_path, words):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        # Check if any of the words are present in the content
        return any(word in content for word in words)

if __name__ == "__main__":
    file_path = "p2.html"  # Ensure this file exists in the current directory
    words_to_check = ["Ձորաղբյուր", "ՁՈՐԱՂԲՅՈՒՐ"]

    if os.path.exists(file_path):
        if file_contains_words(file_path, words_to_check):
            send_email_with_attachment(file_path)
        else:
            print(f"The file {file_path} does not contain the specified words.")
    else:
        print(f"File not found: {file_path}")
