

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
url = "https://www.google.co.jp/imghp?hl=ja"
browser.get(url)

kw_search = browser.find_element_by_css_selector("#sbtc > div > div.a4bIc > input")