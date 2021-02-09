import numpy as np
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
from app import db
import xlwings as xw
from file_template import get_file_template_dir


template1_dir = get_file_template_dir()

# QUERY FROM INPUT

query_hansol = """
SELECT * from Input
WHERE consignee_name = "HANSOLL TEXTILE"
"""
df_hansol = pd.read_sql_query(query_hansol, db.engine)
df_hansol['consignee_name'] = df_hansol[['consignee_name', 'client_name']].agg('\n'.join, axis=1)


query_not_hansoll = """
SELECT * from Input
WHERE consignee_name != "HANSOLL TEXTILE"
"""
df_not_hansol = pd.read_sql_query(query_not_hansoll, db.engine)

#############################################################


####QUERY FROM HANSOLL

query_hansol_2 = "SELECT * FROM Hansoll"
df_hansol_1 = pd.read_sql_query(query_hansol_2, db.engine)

#########################################################



#### SHEET 1 (INDEX 0) LOGIC  #####################
df = pd.concat([df_hansol,df_not_hansol],ignore_index=True)

def sheet_0():

    app = xw.App(visible=False)
    wbExcel = xw.Book(template1_dir + '/new.xlsx')
    active_worksheet = wbExcel.sheets[0]


    active_worksheet.range('E3').options(index=False, header=False).value = df['bill_number']
    active_worksheet.range('H3').options(index=False, header=False).value = df['cargo_pcs']
    active_worksheet.range('I3').options(index=False, header=False).value = df['cargo_weight']
    active_worksheet.range('K3').options(index=False, header=False).value = df['pp_cc']
    active_worksheet.range('L3').options(index=False, header=False).value = df['hs_code']
    active_worksheet.range('M3').options(index=False, header=False).value = df['cargo_item']
    active_worksheet.range('N3').options(index=False, header=False).value = df['invoice_value']
    active_worksheet.range('O3').options(index=False, header=False).value = df['shipper_name']
    active_worksheet.range('T3').options(index=False, header=False).value = df['consignee_name']
    active_worksheet.range('U3').options(index=False, header=False).value = df['consignee_address']
    active_worksheet.range('X3').options(index=False, header=False).value = df['consignee_telephone']
    active_worksheet.range('AA3').options(index=False, header=False).value = df['zipcode']


    wbExcel.save()
    wbExcel.close()
    app.quit()





#### SHEET 2 (INDEX 1) LOGIC  #####################

column_names = ["id", "bill_number", "shipper_name", "cargo_item", "cargo_pcs", "cargo_weight", "consignee_name"]

df_hansol_2 = df_hansol.reindex(columns=column_names)

df_hansol_3 =  pd.concat([df_hansol_1,df_hansol_2],ignore_index=True)


print(df_hansol_3)