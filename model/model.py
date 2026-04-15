from database import DAO
from model.retailer import Retailer

class Model:
    def __init__(self):
        self.DAO = DAO

    def get_lista_anni(self):
        lista_anni = self.DAO.getListaAnni()
        lista_anni.sort(reverse=False)
        return lista_anni

    def get_lista_brand(self):
        lista_brand = self.DAO.getListaBrand()
        lista_brand.sort(reverse=False)
        return lista_brand

    def get_lista_retailer(self):
        lista_retailer: list[Retailer] = self.DAO.getListaRetailer()
        lista_retailer.sort(key=lambda x: x.Retailer_name)
        return lista_retailer

    def top_vendite(self, anno: int, brand: str, retailer: int):
        if brand == "Nessun filtro":
            brand = None
        if anno is not None:
            anno = int(anno)
        if retailer is not None:
            retailer = int(retailer)
        lista_daily_sales = self.DAO.topVendite(anno, brand, retailer)[0:4]
        res = ""
        for i in lista_daily_sales:
            res += (i.__str__()+"\n")
        return res

    def analizza_vendite(self, anno: int, brand: str, retailer: int):
        if brand == "Nessun filtro":
            brand = None
        if anno is not None:
            anno = int(anno)
        if retailer is not None:
            retailer = int(retailer)
        res = []
        giro_affari = self.DAO.getGiroAffari(anno, brand, retailer)
        n_vendite = self.DAO.getNVendite(anno, brand, retailer)
        n_retailers = self.DAO.getNRetailers(anno, brand, retailer)
        n_prodotti = self.DAO.getTotNProdotti(anno, brand, retailer)
        res.extend([giro_affari, n_vendite, n_retailers, n_prodotti])
        return res

