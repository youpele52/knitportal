from typing import Dict
import httpx

from bs4 import BeautifulSoup
from knitportal.db.crud import create_product
from knitportal.db.schemas import Product, ProductCreate
from sqlalchemy.orm import Session


class WebScraper:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_product(self, product: ProductCreate) -> Product:
        productInstance = ProductCreate(**product)
        saved_product = create_product(self.db_session, productInstance)
        print(saved_product)

    def get_soup(self, html_content: str) -> BeautifulSoup:
        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        return soup
