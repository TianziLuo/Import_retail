import os
import pandas as pd
import subprocess
import mysql.connector
from mysql.connector import Error
from Sheet_Item_Data import Department_data, Category_data, MenuItems_data
from Sheet_Item_SKU import Item_SKU_data, CatalogyToItem_data, ItemToTax_data
from filedialog import select_excel_file, save_excel_file


## step 1
# Get the path to the desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# Create the full path for the SQL file
file_path_necessary = os.path.join(desktop, 'necessary.sql')

# Read the data from 'china.xlsx'
df_input = select_excel_file()
df_item = pd.read_excel(df_input, sheet_name='item')

# Process data using custom functions
processed_data = {
    'Department': Department_data(df_item),
    'Category': Category_data(df_item),
    'Menu_items': MenuItems_data(df_item),
    'attribute_type': pd.DataFrame(),
    'Attributes': pd.DataFrame(),
    'Attributes_value': pd.DataFrame(),
    'menu_item_sku': Item_SKU_data(df_item),
    'Category_to_item':  CatalogyToItem_data(df_item),
    'menu_item_to_tax': ItemToTax_data(df_item)
}

# Write processed data to a new Excel file 'china_final.xlsx'
# print(df_output)
with pd.ExcelWriter(save_excel_file(), engine='openpyxl') as writer:
    for sheet_name, table_data in processed_data.items():
        # Write each DataFrame to a separate sheet
        table_data.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Open the workbook and select the sheet to delete the first row
        workbook = writer.book
        worksheet = workbook[sheet_name]
        
        # Delete the first row (header)
        worksheet.delete_rows(1)

