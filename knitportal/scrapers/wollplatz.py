import time
from sqlalchemy.orm import Session
from knitportal.scrapers.base import WebScraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WollPlatzScraper(WebScraper):
    urls = [
        "https://www.wollplatz.de/wolle/dmc/dmc-natura-xl",
        "https://www.wollplatz.de/wolle/drops/drops-safran",
        "https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix",
        "https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk",
    ]
    sel_driver_options = webdriver.ChromeOptions()
    sel_driver_options.add_argument("headless")

    def __init__(self, db_session: Session):
        self.driver = webdriver.Chrome(
            "/usr/local/bin/chromedriver", options=self.sel_driver_options
        )
        super().__init__(db_session)

    def start_scrape(self) -> None:
        for url in self.urls:
            st = self.driver.get(url)
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )
            print("Page loaded completely.")
            variant_group = self.driver.find_element(
                By.CLASS_NAME, "variants-group-container"
            )
            print("found variants")
            variants = variant_group.find_elements(By.XPATH, "./div")
            data_ids = []
            for variant in variants:
                data_id = variant.get_attribute("data-id")
                data_ids.append(data_id)

            # Use JavaScript to hide the cookie element
            cookiebanner = self.driver.find_element(By.ID, "cookiebanner")
            self.driver.execute_script(
                "arguments[0].style.display = 'none';", cookiebanner
            )

            for data_id in data_ids:
                el = self.driver.find_element(By.XPATH, f'//*[@data-id="{data_id}"]')
                try:
                    el.click()
                    print("clicked a variant div")
                    time.sleep(5)  # wait 5 secs for page to load
                except Exception as e:
                    print(e, variant.text)
                page_html = self.driver.page_source

                soup = self.get_soup(page_html)
                self.handleScrape(soup)

    def handleScrape(self, soup: BeautifulSoup) -> None:
        data = {}

        # get the product's name
        name_element = soup.find("h1", {"id": "pageheadertitle"})
        data["name"] = self.value_or_default(name_element)

        # get the product's price
        price_element = soup.find("span", {"itemprop": "price"})
        data["price"] = price_element["content"] if price_element else ""

        # get the product's availability
        availability_element = soup.find(
            "div", {"id": "ContentPlaceHolder1_upStockInfoDescription"}
        )
        data["availability"] = self.value_or_default(
            availability_element.contents[1], "nicht lieferbar"
        )

        # get the product's brand
        brand_element = soup.find("td", text="Marke").find_next_sibling("td")
        data["brand"] = self.value_or_default(brand_element)

        # get the product's needle_size
        needle_size_element = soup.find("td", text="Nadelstärke").find_next_sibling(
            "td"
        )
        data["needle_size"] = self.value_or_default(needle_size_element)

        # get the product's composition
        composition_element = soup.find(
            "td", text="Zusammenstellung"
        ).find_next_sibling("td")
        data["composition"] = self.value_or_default(composition_element)

        # Add more data extraction logic here depending on the website layout

        print(data)
        self.save_product(data)

    def value_or_default(self, element, default_str="") -> str:
        return element.string.strip() if element else default_str
