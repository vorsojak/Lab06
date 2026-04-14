from dataclasses import dataclass
from datetime import date


@dataclass
class DailySale:
    Retailer_name: str
    Product: str
    Date: date
    Ricavo: float


    def __str__(self):
        return f"Data: {self.Date}, Ricavo: {self.Ricavo}, Retailer: {self.Retailer_name}, Prodotto: {self.Product}"