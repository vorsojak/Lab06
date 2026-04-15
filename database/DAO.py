from database.DB_connect import DBConnect
from model.product import Product
from model.retailer import Retailer
from model.daily_sale import DailySale


class DAO():
    def __init__(self):
        pass


def getListaAnni():
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor()

    query = """select DISTINCT YEAR(Date)
            from go_sales.go_daily_sales gds"""

    cursor.execute(query)

    res = []
    for row in cursor:
        res.append(row[0])

    cursor.close()
    cnx.close()
    return res


def getListaBrand():
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor()

    query = """select DISTINCT Product_brand
                from go_sales.go_products gp"""

    cursor.execute(query)

    res = []
    for row in cursor:
        res.append(row[0])

    cursor.close()
    cnx.close()
    return res


def getListaRetailer():
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """select *
                from go_sales.go_retailers gr"""

    cursor.execute(query)

    res = []
    for row in cursor:
        res.append(Retailer(**row))

    cursor.close()
    cnx.close()
    return res


def topVendite(anno, brand, retailer_code):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """with yearly_summary as (
                select gr.Retailer_name, gp.Product, gds.Date, (gds.Quantity * gds.Unit_sale_price) as Ricavo
                from go_sales.go_daily_sales gds, go_sales.go_products gp, go_sales.go_retailers gr
                where gds.Retailer_code = gr.retailer_code and gds.Product_number = gp.Product_number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or gp.Product_brand = %s)
                and (%s is NULL or gds.Retailer_code = %s)
            )
            select * from yearly_summary
            order by Ricavo desc;"""

    params = (anno, anno, brand, brand, retailer_code, retailer_code)
    cursor.execute(query, params)

    res = []
    for row in cursor:
        res.append(DailySale(**row))

    cursor.close()
    cnx.close()
    return res


def getGiroAffari(anno, brand, retailer_code):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """select sum(gds.Quantity * gds.Unit_sale_price) as giro_affari
                from go_sales.go_daily_sales gds, go_sales.go_products gp, go_sales.go_retailers gr
                where gds.Retailer_code = gr.retailer_code and gds.Product_number = gp.Product_number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or gp.Product_brand = %s)
                and (%s is NULL or gds.Retailer_code = %s)"""

    params = (anno, anno, brand, brand, retailer_code, retailer_code)
    cursor.execute(query, params)

    res = []
    for row in cursor:
        res.append(row)

    cursor.close()
    cnx.close()
    return res[0]

def getNVendite(anno, brand, retailer_code):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """select count(*) as n_vendite
                from go_sales.go_daily_sales gds, go_sales.go_products gp, go_sales.go_retailers gr
                where gds.Retailer_code = gr.retailer_code and gds.Product_number = gp.Product_number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or gp.Product_brand = %s)
                and (%s is NULL or gds.Retailer_code = %s)"""

    params = (anno, anno, brand, brand, retailer_code, retailer_code)
    cursor.execute(query, params)

    res = []
    for row in cursor:
        res.append(row)

    cursor.close()
    cnx.close()
    return res[0]

def getNRetailers(anno, brand, retailer_code):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """WITH retailers AS (
                SELECT distinct gds.Retailer_code
                FROM go_sales.go_products gp, go_sales.go_daily_sales gds 
                WHERE gds.Product_number = gp.Product_number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or gp.Product_brand = %s)
                and (%s is NULL or gds.Retailer_code = %s)
                )
            SELECT COUNT(*) as n_retailers FROM retailers;"""

    params = (anno, anno, brand, brand, retailer_code, retailer_code)
    cursor.execute(query, params)

    res = []
    for row in cursor:
        res.append(row)

    cursor.close()
    cnx.close()
    return res[0]

def getTotNProdotti(anno, brand, retailer_code):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """WITH prodotti AS (
                SELECT distinct gds.Product_number
                FROM go_sales.go_products gp, go_sales.go_daily_sales gds 
                WHERE gds.Product_number = gp.Product_number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or gp.Product_brand = %s)
                and (%s is NULL or gds.Retailer_code = %s)
                )
            SELECT COUNT(*) as n_prodotti FROM prodotti;"""

    params = (anno, anno, brand, brand, retailer_code, retailer_code)
    cursor.execute(query, params)

    res = []
    for row in cursor:
        res.append(row)

    cursor.close()
    cnx.close()
    return res[0]