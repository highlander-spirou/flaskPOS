import numpy as np
from datetime import datetime
import pandas as pd
from app import db
import xlwings as xw
from file_template import get_file_template_dir
from create_table import table_for_sheet0_file1, table_for_sheet0_file1, table_for_sheet1_file1


template1_dir = get_file_template_dir()
today = datetime.now().strftime('%Y-%m-%d')
filename = "WORLD-MNF-" + today


def get_dbs():

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


    ####QUERY FROM HANSOLL #######################

    query_hansol_2 = "SELECT * FROM Hansoll"
    df_hansol_1 = pd.read_sql_query(query_hansol_2, db.engine)

    #########################################################


    return df_hansol, df_not_hansol, df_hansol_1


def concate_df(df1, df2):
    df = pd.concat([df1,df2],ignore_index=True)
    return df

# file 1 tên là WORLD-MNF-(2021-02-06)
def copy_template_file1(filename):
    app = xw.App(visible=False)
    wbExcel = xw.Book(template1_dir + '/template_file1.xlsx')
    file_dir = template1_dir + '/created_file/' + filename + '.xlsx'
    wbExcel.save(file_dir)
    wbExcel.close()
    app.quit()

    return file_dir

# file 1 tên là WORLD-MNF-(2021-02-06)
def copy_to_file_1(df, filename):

    file_dir = copy_template_file1(filename)
    df_complete = table_for_sheet0_file1(df)
    df_halves = table_for_sheet1_file1(df)

    app = xw.App(visible=False)
    wbExcel = xw.Book(file_dir)

    active_worksheet_0 = wbExcel.sheets[0]
    active_worksheet_0.range('A2').options(index=False, header=False).value = df_complete
  
    active_worksheet_1 = wbExcel.sheets[1]
    active_worksheet_1.range('A2').options(index=False, header=False).value = df_halves

    wbExcel.save()
    wbExcel.close()
    app.quit()
    
    print('done')


def tao_lao():
    column_names = ["id", "bill_number", "shipper_name", "cargo_item", "cargo_pcs", "cargo_weight", "consignee_name"]

    # df_hansol_2 = df_hansol.reindex(columns=column_names)

    # df_hansol_3 =  pd.concat([df_hansol_1,df_hansol_2],ignore_index=True)


df_hansol, df_not_hansol, df_hansol_1 = get_dbs()

df = concate_df(df_hansol,df_not_hansol)

copy_to_file_1(df, filename) 