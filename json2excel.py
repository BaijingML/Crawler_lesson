import json
import xlrd
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def data_write(data_list, original_data_path, companies, info_types):
    df = pd.read_excel(original_data_path)
    for i, company_name in enumerate(companies):
        company_data = data_list[i]['info']
        for j in range(len(info_types)):
            df.iloc[i, j + 1] = company_data[info_types[j]]
    df.to_excel(original_data_path, index=False)


def data_read(original_data_path):
    data_workbook = xlrd.open_workbook(original_data_path)
    sheet_names = data_workbook.sheet_names()
    company_names = []
    for sheet_name in sheet_names:
        sheet = data_workbook.sheet_by_name(sheet_name)
        company_names.extend(sheet.col_values(0)[1:])
    return company_names


def json_read(json_path):
    with open(json_path, 'r', encoding = 'utf-8') as f:
        data_str = f.read()
        data = json.loads(data_str)
    return data


def json2excel(json_path, excel_path, info_types):
    companies = data_read(excel_path)
    json_data = json_read(json_path)
    data_write(json_data, excel_path, companies, info_types)





info_types = ['BS_PERSON', 'BS_REG_CONDITION', 'BS_START', 'BS_CONTACT', 'BS_ADDR', 'BS_LOGIN_STATE', 'BS_REG_NUM', 'BS_CODE', 'BS_END', 'BS_LOGIN', 'BS_AREA', 'BS_PROP', 'BS_MONEY', 'BS_REG', 'BS_WEB']
json_path = "C:/Users/26708/Desktop/高新区.json"
excel_path = "C:/Users/26708/Desktop/高新区企业信息改.xlsx"
json2excel(json_path, excel_path, info_types)
