import numpy as np
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
from app import db
import xlwings as xw

df = pd.read_sql_query('select * from Input', db.engine)
# print(df)

app = xw.App(visible=False)
wbExcel = xw.Book('sth.xlsx')
active_worksheet = wbExcel.sheets[0]

active_worksheet.range('B3').options(index=False, header=False).value = df

wbExcel.save()
wbExcel.close()
app.quit()