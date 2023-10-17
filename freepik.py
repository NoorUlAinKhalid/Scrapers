from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
import pandas as pd

def get_card_links(driver):
    card_links = []
    for i in range(1, 16):
        driver.get(f'https://www.freepik.com/search?format=search&page={i}&query=bedroom+set&selection=1&type=photo')
        elements = driver.find_elements(By.CLASS_NAME, 'showcase__content')
        for element in elements:
            card = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            card_links.append(card)
    return card_links

def get_image_links(driver, card_links):
    page_url = []
    image_url = []
    image_title = []
    for card in card_links:
        try:

            driver.get(card)
            image = driver.find_element(By.XPATH, '//*[@id="main"]/div/header/div/div[1]/div').find_element(By.TAG_NAME, 'img').get_attribute('srcset')
            title = driver.find_element(By.XPATH, '//*[@id="main"]/div/header/div/div[1]/div').find_element(By.TAG_NAME, 'img').get_attribute('alt')
            new = image.split(" ")[-2]
            page_url.append(card)
            image_url.append(new)
            image_title.append(title)
        except:
            print("Invalid Link")
    return page_url, image_url, image_title


def generate_uuids(image_url):
    uuids = [uuid.uuid4() for _ in range(len(image_url))]
    return uuids

def create_and_save_dataframe(uuids, page_url, image_url, image_title):
    df = pd.DataFrame(columns=['UUID', 'PAGE_URL', 'IMAGE_URL', 'TITLE/Desc'])
    df['UUID'] = uuids
    df['PAGE_URL'] = page_url
    df['IMAGE_URL'] = image_url
    df['TITLE/Desc'] = image_title
    df.to_csv('freepik1.csv')


def main():
    driver = webdriver.Chrome()
    card_links = get_card_links(driver)
    page_url, image_url, image_title = get_image_links(driver, card_links)
    uuids = generate_uuids(image_url)
    create_and_save_dataframe(uuids, page_url, image_url, image_title)
    driver.quit()

if __name__ == "__main__":
    main()
