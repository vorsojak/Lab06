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
        res.append(row)

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
        res.append(row)

    cursor.close()
    cnx.close()
    return res


def getListaRetailer():
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor()

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
    cursor = cnx.cursor()

    query = """with yearly_summary as (
                select gr.Retail_name, gp.Product, gp.Product_brand, Date, (Quantity * Unit_sale_price) as Ricavo
                from go_daily_sales gds, go_products gp, go_retails gr
                where gds.Retailer_code = gr.retailer_code and gds.Product_number = gp.Product__number
                and (%s is NULL or YEAR(date) = %s)
                and (%s is NULL or Product_Brand = %s)
                and (%s is NULL or REtailer_code = %s)
            )
            select * from yearly_summary
            order by Ricavo desc;
            """

    cursor.execute(query, (anno, anno, brand, brand, retailer_code, retailer_code,))

    res = []
    for row in cursor:
        res.append(DailySale(**row))

    cursor.close()
    cnx.close()
    return res
