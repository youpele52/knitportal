from typing import List
from pydantic import BaseModel


class BaseProduct(BaseModel):
    brand: str
    name: str
    price: float
    availability: str
    needle_size: str
    composition: str


class ProductCreate(BaseProduct):
    brand: str
    name: str
    price: float
    availability: str
    needle_size: str
    composition: str


class ProductUpdate(BaseModel):
    id: int
    price: float
    availability: str
    needle_size: str
    composition: str


class Product(BaseProduct):
    id: int

    class Config:
        orm_mode = True


class ProductList(BaseModel):
    items: List[Product]

    class Config:
        orm_mode = True
