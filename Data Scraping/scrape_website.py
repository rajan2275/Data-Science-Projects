# ------------------------------------------------
# Code uses BeautifulSoup and selenium to scrape data
#  from multiple sites.
# ------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver

urls=["https://rajan2275.github.io/Python-Design-Patterns",
      'https://github.com/rajan2275/Python-Design-Patterns',
      'https://github.com/rajan2275/Data-Science-Projects',
      'https://github.com/rajan2275/Python-Test-Driven-Development',
      'https://www.google.co.uk/search?biw=1517&bih=707&ei=pUdjWpr0FYjZwQKH3qP4Ag&q=python+design+patterns+github+rajan2275&oq=python+design+patterns+github+rajan2275&gs_l=psy-ab.3...5874.10000.0.10333.11.11.0.0.0.0.84.813.11.11.0....0...1c.1.64.psy-ab..0.6.457...33i21k1j33i160k1.0.swmQ8Vhyv7Q']

for n in range(0, 50):
    for url in urls:
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup= BeautifulSoup(html)

        for tag in soup.find_all('title'):
            print(tag.text)

    driver.quit()

