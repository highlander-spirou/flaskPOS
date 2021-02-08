import numpy as np
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
from app import db
import xlwings as xw

query = """
SELECT """ + """bill_number, shipper_name, consignee_name, client_name""" + """FROM Input
WHERE invoice_value >= 200
"""


df = pd.read_sql_query(query, db.engine)
print(df)


# app = xw.App(visible=False)
# wbExcel = xw.Book('sth.xlsx')
# active_worksheet = wbExcel.sheets[0]

# active_worksheet.range('B3').options(index=False, header=False).value = df

# wbExcel.save()
# wbExcel.close()
# app.quit()