
import pandas as pd

# file 1 tên là WORLD-MNF-(2021-02-06)

def table_for_sheet0_file1(df):

    df['A1'] = 'WLDSEL'
    df['B1'] = 'data 1'
    df['C1'] = 'data 2'
    df['Date'] = pd.to_datetime('today').strftime("%m/%d/%Y")
    df['F1'] = 'SGN'
    df['G1'] = 'ICN'
    df['J1'] = 'N'
    df['R1'] = ''
    df['S1'] = ''
    df['U1'] = ''
    df['V1'] = ''
    df['X1'] = ''
    df['Y1'] = ''
    df['Z1'] = '2'
    

    column_names = ["A1", "B1", "C1", "Date", "bill_number", 
    "F1", "G1", "cargo_pcs", "cargo_weight", "J1", 
    "pp_cc", "hs_code", "cargo_item", "invoice_value", 
    "shipper_name", "consignee_name","consignee_address", "R1", "S1",
    "consignee_telephone", "U1", "V1","zipcode", "X1", "Y1","Z1"]

    df = df.reindex(columns=column_names)
    return df

def table_for_sheet1_file1(df):
    column_names = ["bill_number", "hs_code", "cargo_item", "cargo_pcs", "invoice_value"]
    df = df.reindex(columns=column_names)
    return df