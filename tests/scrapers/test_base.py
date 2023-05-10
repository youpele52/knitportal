import unittest
from unittest.mock import Mock, patch

from httpx import Response, RequestError
from bs4 import BeautifulSoup

from knitportal.scrapers.base import WebScraper


class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scrape_map = [
            {
                "url": "http://example.com",
                "handler": Mock(return_value={"name": "Product1", "price": 10.0}),
            },
            {
                "url": "http://example.com",
                "handler": Mock(return_value={"name": "Product2", "price": 20.0}),
            },
        ]
        self.db_session = Mock()
