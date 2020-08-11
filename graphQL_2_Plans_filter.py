import requests
import time
import pyodbc
import datetime
from datetime import datetime
import time
start_time=datetime.now()

conn = pyodbc.connect(driver="SQL Server Native Client 11.0",
                       host="10.10.101.4", database="expDB",
                       uid="sa", pwd="P@ssw0rd@2020", autocommit=True)
cursor = conn.cursor()
def run_query():
    l1=[]
    l2=[]
    query = """query { Plans{id, rootrecordId, sysSubjectsId,subjectBiin , subjectNameRu ,subjectNameKz ,nameRu,nameKz, refTradeMethodsId,
     refUnitsCode, count, price, amount, refMonthsId, refPlnPointStatusId, plnPointYear, refSubjectTypeId, 
     refEnstruCode, refFinsourceId, refAbpCode, isQvazi, dateCreate, timestamp, refPointTypeId, descRu, 
    descKz,extraDescKz, extraDescRu, sum1, sum2, sum3, supplyDateRu, prepayment,refJustificationId, refAmendmentAgreemTypeId, 
    refAmendmAgreemJustifId, contractPrevPointId, disablePersonId, transferSysSubjectsId, transferType,
    refBudgetTypeId, createdinActId, isActive, activeActId, systemId, indexDate, PlansKato {id, plnPointsId, 
    refKatoCode, refCountriesCode, fullDeliveryPlaceNameRu, fullDeliveryPlaceNameKz, count, isActive, systemId, indexDate}}}"""
    next = True
    k = 0
    while next is True:
        URL = 'https://ows.goszakup.gov.kz/v3/graphql'
        token = ('Bearer' + ' ' + 'f309ecc15d574833c45713da702049e2')
        headers_1 = {'Content-Type': 'application/json', 'Authorization': 'none'}
        headers_1['Authorization'] = token
        r = requests.post(URL, json={"query": query}, headers=headers_1, verify=False).json()

        if 'name' in r:
            print('Error:')
            print('string with error: ', r)
            k=k+1
            if k >10:
                break
                print('big amount of error, we should break')
            else:
                continue
        else:
            try:
                for i in r['data']['Plans']:
                    k=0
                    q = 'insert into PlnPoint (id, rootrecordId,sysSubjectsId, subjectBiin, subjectNameRu, subjectNameKz, ' \
                        'nameRu, nameKz, refTradeMethodsId, refUnitsCode, count_ , price, amount, refMonthsId, refPlnPointStatusId,' \
                        ' plnPointYear, refSubjectTypeId, refEnstruCode, refFinsourceId, refAbpCode, isQvazi, dateCreate, timestamp_, refPointTypeId, descRu,' \
                        'descKz, extraDescKz, extraDescRu, sum1, sum2, sum3, supplyDateRu, prepayment, refJustificationId, refAmendmentAgreemTypeId, ' \
                        ' refAmendmAgreemJustifId, contractPrevPointId, disablePersonId, transferSysSubjectsId, transferType, refBudgetTypeId, createdinActId, isActive, activeActId, systemId, indexDate) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                    a = (i['id'], i['rootrecordId'], i['sysSubjectsId'], i['subjectBiin'], i['subjectNameRu'], i['subjectNameKz'], i['nameRu'], i['nameKz'], i['refTradeMethodsId'], i['refUnitsCode'], i['count'], i['price'],
                         i['amount'], i['refMonthsId'], i['refPlnPointStatusId'],i['plnPointYear'],i['refSubjectTypeId'],i['refEnstruCode'],i['refFinsourceId'],i['refAbpCode'],i['isQvazi'],i['dateCreate'],i['timestamp'],
                         i['refPointTypeId'],i['descRu'],i['descKz'], i['extraDescKz'],i['extraDescRu'], i['sum1'], i['sum2'], i['sum3'],i['supplyDateRu'], i['prepayment'], i['refJustificationId'], i['refAmendmentAgreemTypeId'],
                         i['refAmendmAgreemJustifId'], i['contractPrevPointId'],i['disablePersonId'],i['transferSysSubjectsId'], i['transferType'], i[ 'refBudgetTypeId'], i['createdinActId'], i['isActive'],
                         i['activeActId'], i['systemId'], i['indexDate'])
                    l1.append(a)

                    q_2 = 'insert into PlansKato (id, plnPointsId, refKatoCode, refCountriesCode,fullDeliveryPlaceNameRu, fullDeliveryPlaceNameKz,' \
                          ' count_, isActive, systemId, indexDate) values (?,?,?,?,?,?,?,?,?,?)'

                    a_2 = (i['PlansKato'][0]['id'], i['PlansKato'][0]['plnPointsId'], i['PlansKato'][0]['refKatoCode'], i['PlansKato'][0]['refCountriesCode'], i['PlansKato'][0]['fullDeliveryPlaceNameRu'], i['PlansKato'][0]['fullDeliveryPlaceNameKz'],
                    i['PlansKato'][0]['count'], i['PlansKato'][0]['isActive'], i['PlansKato'][0]['systemId'], i['PlansKato'][0]['indexDate'])
                    l2.append(a_2)
                    cursor.fast_executemany = True
                    cursor.executemany(q, l1)
                    cursor.executemany(q_2, l2)


                    # print(i['PlansKato'][0]['id']) работает !


                next=r['extensions']['pageInfo']['hasNextPage']
                lastID = r['extensions']['pageInfo']['lastId']
                query = """query { Plans(limit: 200, after:""" + str(lastID) + """){id, rootrecordId, sysSubjectsId,subjectBiin , subjectNameRu ,subjectNameKz ,nameRu,nameKz, refTradeMethodsId,
                     refUnitsCode, count, price, amount, refMonthsId, refPlnPointStatusId, plnPointYear, refSubjectTypeId, 
                     refEnstruCode, refFinsourceId, refAbpCode, isQvazi, dateCreate, timestamp, refPointTypeId, descRu, 
                    descKz,extraDescKz, extraDescRu, sum1, sum2, sum3, supplyDateRu, prepayment,refJustificationId, refAmendmentAgreemTypeId, 
                    refAmendmAgreemJustifId, contractPrevPointId, disablePersonId, transferSysSubjectsId, transferType,
                    refBudgetTypeId, createdinActId, isActive, activeActId, systemId, indexDate, PlansKato {id, plnPointsId, 
                    refKatoCode, refCountriesCode, fullDeliveryPlaceNameRu, fullDeliveryPlaceNameKz, count, isActive, systemId, indexDate}}}"""
            except:
                time.sleep(5)
                continue




run_query()
end_time= datetime.now()

print('Running time is:', start_time-end_time)


