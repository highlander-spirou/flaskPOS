import numpy as np
from datetime import datetime
import pandas as pd
from app import db
import xlwings as xw
from file_template import get_file_template_dir
from create_table import table_for_sheet0_file1, table_for_sheet1_file1, table_for_sheet0_file2, table_for_sheet1_file2


template1_dir = get_file_template_dir()
today = datetime.now().strftime('%Y-%m-%d')
filename1 = "WORLD-MNF-" + today
filename2 = filename1 + 'TO_KOREA'

def concate_df(df1, df2):
    df = pd.concat([df1,df2],ignore_index=True)
    return df

def get_dbs():


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
    df_not_hansol['consignee_name'] = df_not_hansol[['consignee_name', 'client_name']].agg('\n'.join, axis=1)

    return df_hansol, df_not_hansol


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
def copy_to_file_1(df, filename, data1, data2):

    
    file_dir = copy_template_file1(filename)
    df_complete = table_for_sheet0_file1(df, data1, data2)
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
    
    print('done 1')


def get_dbs_for_file2():

    query_hansol_2 = "SELECT * FROM Hansoll"
    df_hansol_1 = pd.read_sql_query(query_hansol_2, db.engine)

    query_enclosed = "SELECT * FROM Enclosed"
    df_enclosed = pd.read_sql_query(query_enclosed, db.engine)

    query_hansol_enclosed = """
    SELECT * FROM Enclosed 
    WHERE consignee_name LIKE "%HANSOLL TEXTILE%" 
    """
    df_hansol_enclosed = pd.read_sql_query(query_hansol_enclosed, db.engine)
    df_hansol_enclosed = df_hansol_enclosed.drop(['bill_number'], axis=1)
    df_hansol_enclosed = df_hansol_enclosed.rename(columns={'enclosed' : 'bill_number'})
    
    return df_hansol_1, df_enclosed, df_hansol_enclosed

def add_columns_enclosed(df):
    df['enclosed'] = ''
    return df


def copy_template_file2(filename):
    app = xw.App(visible=False)
    wbExcel = xw.Book(template1_dir + '/template_file2.xlsm')
    file_dir = template1_dir + '/created_file/' + filename + '.xlsm'
    wbExcel.save(file_dir)
    wbExcel.close()
    app.quit()

    return file_dir

def copy_to_file_2(df, df_hansol, filename, bag, message):

    file_dir = copy_template_file2(filename)

    df = add_columns_enclosed(df)
    df_hansol_1, df_enclosed, df_hansol_enclosed = get_dbs_for_file2()
    df_sheet0 = concate_df(df, df_enclosed)
    df_sheet1 = concate_df(df_hansol_1, df_hansol_enclosed)
    df_sheet1 = concate_df(df_sheet1, df_hansol)


    df_full_sheet0 = table_for_sheet0_file2(df_sheet0)
    df_full_sheet1 = table_for_sheet1_file2(df_sheet1)

    sum_pcs = df_full_sheet0['cargo_pcs'].sum()
    sum_weight = df_full_sheet0['cargo_weight'].sum()

    app = xw.App(visible=False)
    wbExcel = xw.Book(file_dir)

    active_worksheet_0 = wbExcel.sheets[0]
    active_worksheet_0.range('C2').value = "NO OF BAGS:  "+ str(bag) + " BAGS"
    active_worksheet_0.range('J4').value = datetime.now().strftime('%d-%b-%y')
    active_worksheet_0.range('K4').value = sum_pcs
    active_worksheet_0.range('M4').value = sum_weight
    active_worksheet_0.range('A6').options(index=False, header=False).value = df_full_sheet0
    
    last_row = active_worksheet_0.range('A6').end('down').row + 1
    active_worksheet_0.cells(last_row, "A").value = message


    active_worksheet_1 = wbExcel.sheets[1]
    active_worksheet_1.range('A6').options(index=False, header=False).value = df_full_sheet1


    wbExcel.save()
    wbExcel.close()
    app.quit()
    
    print('done 2')


def copy_template_file3(filename):
    app = xw.App(visible=False)
    wbExcel = xw.Book(template1_dir + '/template_file3.xlsx')
    file_dir = template1_dir + '/created_file/' + filename + '.xlsx'
    wbExcel.save(file_dir)
    wbExcel.close()
    app.quit()

    return file_dir

def copy_to_file_3(df, today):
    df_length = len(df.index)
    for i in range(df_length):
        df_series = df.iloc[i]
        filename= "Invoice " + df_series.bill_number
        file_dir = copy_template_file3(filename)
        app = xw.App(visible=False)
        wbExcel = xw.Book(file_dir)
        active_worksheet_0 = wbExcel.sheets[0]

        active_worksheet_0.range('A3').options(index=False, header=False).value = df_series.shipper_name
        active_worksheet_0.range('E4').options(index=False, header=False).value = df_series.gd
        active_worksheet_0.range('J4').options(index=False, header=False).value = today
        active_worksheet_0.range('A7').options(index=False, header=False).value = df_series.consignee_name
        active_worksheet_0.range('A8').options(index=False, header=False).value = df_series.consignee_address
        active_worksheet_0.range('G20').options(index=False, header=False).value = df_series.bill_number
        active_worksheet_0.range('H22').options(index=False, header=False).value = df_series.cargo_weight
        active_worksheet_0.range('C27').options(index=False, header=False).value = df_series.cargo_item
        active_worksheet_0.range('H27').options(index=False, header=False).value = df_series.invoice_value
        active_worksheet_0.range('H28').options(index=False, header=False).value = df_series.invoice_value

        wbExcel.save()
        wbExcel.to_pdf()
        wbExcel.close()
        app.quit()
        
        print('done 3 - ' + str(i))


###################################

data1 = input("MWAB NO")
data2 = input("FLT NO")
bag_number = input("Bag Number")
message = input("Message")



df_hansol, df_not_hansol = get_dbs()
df = concate_df(df_hansol, df_not_hansol)

df_more_10 = df[df["cargo_weight"]>=10]
df_more_10["gd"] = "GD-" + datetime.now().strftime('%d-%m-%Y')

file_final = get_file_template_dir() + r'\created_file'
print(file_final)

copy_to_file_1(df, filename1, data1, data2)
copy_to_file_2(df, df_hansol, filename2, bag_number,message)
copy_to_file_3(df_more_10, today)

