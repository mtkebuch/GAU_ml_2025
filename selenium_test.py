from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time

service = Service(r"C:\Users\Mylaptop.ge\Documents\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com")

time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

data = []

for q in quotes:
    text = q.find_element(By.CLASS_NAME, "text").text
    author = q.find_element(By.CLASS_NAME, "author").text
    data.append([text, author])

cleaned = [[t.strip(), a.strip()] for t, a in data]

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(cleaned)

print("Done! Data has been saved to quotes.csv")

driver.quit()


