from dataclasses import dataclass

@dataclass
class Product:
    Product_number: int
    Product: str
    Product_type: str
    Product_brand: str


    def __hash__(self):
        return hash(self.Product_number)

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __str__(self):
        return f"{self.Product}, {self.Product_type} - {self.Product_brand}"