from pydantic import BaseModel
from typing import List, Optional


"""BLOG SCHEMAS"""
class ProductBase(BaseModel):
    product_name: str
    product_type: str
    price: float
    user_id: int


class Product(ProductBase):
    class Config():
        orm_mode = True



"""ATTRIBUTE SCHEMAS"""
class AttributeBase(BaseModel):
    attribute_name: str
    content: str
    eligible_for: str
    user_id: int


class Attribute(AttributeBase):
    class Config():
        orm_mode = True


"""USER SCHEMAS"""
class User(BaseModel):
    name: str
    email: str
    password: str


"""LOGIN SCHEMAS"""
class Login(BaseModel):
    username: str
    password: str



"""TOKEN SCHEMAS"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


"""SHOW SCHEMAS"""
class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


class ShowProduct(Product):
    product_name: str
    product_type: str
    price: float
    creator: ShowUser
    class Config():
        orm_mode = True


class ShowAttribute(Attribute):
    attribute_name: str
    content: str
    creator: ShowUser
    class Config():
        orm_mode = True