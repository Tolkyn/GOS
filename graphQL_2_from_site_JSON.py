import requests
from datetime import datetime
import time
import json
start_time=datetime.now()


def run_query():

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
        print('data from data:', r)
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
                # for i in r['data']['Plans']:
                k=0
                with open('C:\\Users\\User\\Desktop\\main_data.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(r, ensure_ascii=False))

                next=r['extensions']['pageInfo']['hasNextPage']
                lastID = r['extensions']['pageInfo']['lastId']
                query = """query { Plans(limit: 200, after:""" + str(lastID) + """){id, rootrecordId, sysSubjectsId,subjectBiin , subjectNameRu ,subjectNameKz ,nameRu,nameKz, refTradeMethodsId,
                     refUnitsCode, count, price, amount, refMonthsId, refPlnPointStatusId, plnPointYear, refSubjectTypeId, 
                     refEnstruCode, refFinsourceId, refAbpCode, isQvazi, dateCreate, timestamp, refPointTypeId, descRu, 
                    descKz,extraDescKz, extraDescRu, sum1, sum2, sum3, supplyDateRu, prepayment,refJustificationId, refAmendmentAgreemTypeId, 
                    refAmendmAgreemJustifId, contractPrevPointId, disablePersonId, transferSysSubjectsId, transferType,
                    refBudgetTypeId, createdinActId, isActive, activeActId, systemId, indexDate, PlansKato {id, plnPointsId, 
                    refKatoCode, refCountriesCode, fullDeliveryPlaceNameRu, fullDeliveryPlaceNameKz, count, isActive, systemId, indexDate}}}"""
                print('done')
            except:
                time.sleep(5)
                continue




run_query()
end_time= datetime.now()

print('Running time is:', start_time-end_time)


