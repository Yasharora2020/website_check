import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


url = "https://www.dnypractice.com.au"
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

r = requests.get(url, timeout=10)

if r.status_code !=200:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS, msg="Subject:Website Down")







