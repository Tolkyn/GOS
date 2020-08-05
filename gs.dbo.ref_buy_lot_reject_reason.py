import requests
import pyodbc

conn = pyodbc.connect(driver="SQL Server Native Client 11.0",
                       host="10.10.101.4", database="GS",
                       uid="sa", pwd="P@ssw0rd@2020", autocommit=True)

def GS_DBO_1():
    token = ('Bearer' + ' ' + 'f309ecc15d574833c45713da702049e2')
    headers_1 = { 'Content-Type' : 'application/json','Authorization':'none' }
    headers_1['Authorization'] = token
    next_page = 'none'
    URL_n = 'https://ows.goszakup.gov.kz/v3/refs/ref_buy_lot_reject_reason'
    while next_page != '':
        r_n = requests.get(URL_n, headers=headers_1, verify=False).json()
        print(r_n)
        next_page = r_n['next_page']
        item = r_n['items']
        for i in item:
            query = 'insert into gs.dbo.ref_buy_lot_reject_reason( item_id, item_name_ru , item_name_kz) values (?,?,?)'
            args = (i['id'], i['name_ru'], i['name_kz'])
            conn.execute(query, args)
        URL_n = 'https://ows.goszakup.gov.kz' + next_page

    print('end of iteration ')

GS_DBO_1()










