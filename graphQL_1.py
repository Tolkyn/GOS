import requests
import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                          'Server=LAPTOP-QHTHN2FI\MSSQLSERVER01;'
                          'Database=master;'
                          'Trusted_Connection=yes;')

def run_query():

    query = """ query{ TrdBuy {id, nameRu, nameKz, numberAnno,}} """
    next=True

    while next is True:
        URL = 'https://ows.goszakup.gov.kz/v3/graphql'
        token = ('Bearer' + ' ' + 'f309ecc15d574833c45713da702049e2')
        headers_1 = {'Content-Type': 'application/json', 'Authorization': 'none'}
        headers_1['Authorization'] = token

        r = requests.post(URL, json={"query": query}, headers=headers_1, verify=False).json()

        for item in r["data"]["TrdBuy"]:
            q = 'insert into TrdBuy (id, nameRu, nameKz, namberAnno) values (?,?,?,?)'
            a = (item['id'], item['nameRu'], item['nameKz'], item['numberAnno'])
            conn.execute(q, a)
            conn.commit()

        next=r['extensions']['pageInfo']['hasNextPage']
        lastID = r['extensions']['pageInfo']['lastId']
        query = """ query{ TrdBuy (limit: 200, after:"""+ str(lastID)+"""){id, nameRu, nameKz, numberAnno,}} """

run_query()


