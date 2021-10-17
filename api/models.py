from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    product_type = Column(String)
    price = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="products")



class Attribute(Base):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True, index=True)
    attribute_name = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="attributes")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    products = relationship("Product", back_populates="creator")
    attributes = relationship("Attribute", back_populates="creator")