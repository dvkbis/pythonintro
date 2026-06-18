from app.models.product import Product
from app.repositories.product_repository import ProductRepository
def main():
    product = Product(id=5, name= "Keyboard Logitech", description= "Mecanic Keyboard", price= 59.99)
    """    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable= False)
    description = Column(String(255))
    price = Column(Float, nullable= False)"""
    product_repo = ProductRepository()

if __name__ == "__main__":
    main()  