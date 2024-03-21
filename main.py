import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

#URL catcher for the website
try:
	URL ="https://www.amazon.com/dp/B0B727YMJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0" #input("Enter the URL of the blog you want to scrape: ")
	r = requests.get(URL, headers=header)
	soup = BeautifulSoup(r.content, "lxml")
	price = soup.find(name='span', class_='a-offscreen').getText()
	price_without_currency = price.split('$')[1]
	# print(soup.prettify())
	print(price)
except ValueError:
	print("Invalid URL! Please pay attention to the URL you entered.")

#EMAIL SENDER
MY_EMAIL = ""
MY_PASSWORD = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=MY_EMAIL, password=MY_PASSWORD)
	connection.sendmail(
		from_addr=MY_EMAIL,
		to_addrs="",
		msg="Subject:Amazon Price Alert🧨"
	)
