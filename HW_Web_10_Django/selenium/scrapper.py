import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless=chrome')
driver = webdriver.Chrome(service=service, options=options)


# Вхід до сайту
def login():
    driver.get("http://localhost:8000/users/login/")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "id_password")))
    username = driver.find_element(by=By.ID, value="id_username")
    password = driver.find_element(by=By.ID, value="id_password")
    username.send_keys("user")
    password.send_keys("piromankod")
    submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
    submit.click()


# Заповнюємо теги
def tags_seed(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        quotes_data = json.load(f)

    for quote_data in quotes_data:
        tags = quote_data['tags']
        for tag in tags:
            driver.get("http://localhost:8000/tag/")
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "id_name")))
            tag_form = driver.find_element(by=By.ID, value="id_name")
            tag_form.send_keys(tag)
            submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
            submit.click()
            print(f"tag {tag} published")


# Заповнюємо авторів
def authors_seed(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        authors = json.load(f)
    for author_data in authors:
        fullname = author_data["fullname"]
        born_date = author_data["born_date"]
        born_location = author_data["born_location"]
        description = author_data["description"]
        driver.get("http://localhost:8000/author/")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "id_bio")))
        fullname_form = driver.find_element(by=By.ID, value="id_fullname")
        fullname_form.send_keys(fullname)
        born_date_form = driver.find_element(by=By.ID, value="id_born_date")
        born_date_form.send_keys(born_date)
        born_location_form = driver.find_element(by=By.ID, value="id_born_location")
        born_location_form.send_keys(born_location)
        description_form = driver.find_element(by=By.ID, value="id_bio")
        description_form.send_keys(description)
        submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
        submit.click()
        print(f"Author {fullname} published")


# Заповнюємо цитати
def quotes_seed(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        quotes = json.load(f)
    for quotes_data in quotes:
        quote = quotes_data["quote"]
        tags = quotes_data["tags"]
        author = quotes_data["author"]
        driver.get("http://localhost:8000/quote/")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        quote_form = driver.find_element(by=By.ID, value="id_quote")
        quote_form.send_keys(quote)
        author_form = driver.find_element(by=By.NAME, value="author")
        author_form.send_keys(author)
        tags_form = driver.find_element(by=By.NAME, value="tags")
        select = Select(tags_form)
        for tag_name in tags:
            select.select_by_visible_text(tag_name)
        submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
        submit.click()
        print(f"Quote {quote} published")


def seeds_all():
    login()
    tags_seed("quotes.json")
    authors_seed("authors.json")
    quotes_seed("quotes.json")
    driver.quit()


if __name__ == '__main__':
    seeds_all()

