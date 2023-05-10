from sqlalchemy import Column, Float, Integer, String, UniqueConstraint

from knitportal.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    name = Column(String)
    price = Column(Float)
    availability = Column(String)
    needle_size = Column(String)
    composition = Column(String)

    __table_args__ = (UniqueConstraint("brand", "name", name="_brand_name_uc"),)
