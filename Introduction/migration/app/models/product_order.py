from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models.base import Base

product_order = Table(
    "product_order",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
    Column("order_id", Integer, ForeignKey("customer_order.id"), primary_key= True)
)