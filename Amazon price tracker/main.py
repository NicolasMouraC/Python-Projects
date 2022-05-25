import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79",
           "Accept-Language" : "en-US,en;q=0.9"}

response = requests.get("https://www.amazon.com.br/GTO-1-Toru-Fujisawa/dp/8583621209/ref=sr_1_97?__mk_pt_BR=ÅMÅŽÕÑ&crid=24BZAS4M8V52U&keywords=new+pop&qid=1652972342&sprefix=new+pop%2Caps%2C303&sr=8-97",
                        headers=headers)
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, "lxml")
price = soup.find(name="span", id="price")
formatted_price = int(price.get_text().split()[1].split(sep=",")[0])

if formatted_price <= 20:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user="email_to_send_message"
                         , password="email_password")
        connection.sendmail(from_addr="email_to_send_message",
                            to_addrs="email_to_receive_the_message",
                            msg="GTO is below 20 BRL in amazon. It's time to buy it!")
