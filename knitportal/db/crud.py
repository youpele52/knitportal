from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from knitportal.db import models, schemas


def create_product(session: Session, product_props: schemas.ProductCreate):
    print(product_props)
    db_product = models.Product(**product_props.dict())

    try:
        # try to add the new product to the database
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

    except IntegrityError as e:
        # In a production scenario, we'll decide what to do with duplicate products or handle other errors
        print("possibly duplicate product encountered")
        session.rollback()
