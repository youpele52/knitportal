from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from knitportal.db.database import get_db

from knitportal.db.models import Product
from knitportal.db.schemas import Product as ProductSchema

router = APIRouter()


def search_products(db: Session, name=None, brand=None):
    query = db.query(Product)
    if name and brand:
        query = query.filter_by(name=name, brand=brand)
    elif name:
        query = query.filter_by(name=name)
    elif brand:
        query = query.filter_by(brand=brand)
    print(query)
    return query.all()


@router.get("/products", tags=["products"])
async def get_products(
    brand: Optional[str] = None, name: Optional[str] = None, db: Session = Depends(get_db)
) -> List[ProductSchema]:
    print("got here")
    products = search_products(db, name, brand)

    if products:
        return products
    else:
        raise HTTPException(status_code=404, detail="Product not found")
