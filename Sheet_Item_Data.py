import pandas as pd
## Department_data
def Department_data(df):
    unique_Department_En = df['Department_En'].dropna().unique()
    unique_Department_Cn = df['Department_Cn'].dropna().unique()
    unique_Department_ID = df['Department_ID'].dropna().unique()
    
    ## name	sort status	en	cn
    Department_data = [list(unique_Department_En),
                  list(unique_Department_ID),          # Sort
                  [1] * len(unique_Department_En),     # One row/ status
                  list(unique_Department_En),
                  list(unique_Department_Cn)]
    
    # Convert to DataFrame
    Department_data = pd.DataFrame(list(zip(*Department_data)))
    return Department_data

## Category_data
def Category_data(df):
    filter_condition = df['Cate_En'].notna()
    filtered_data = df[filter_condition]

    department_id = filtered_data['Department_ID']
    unique_Category_En = filtered_data['Cate_En']
    unique_Category_Cn = filtered_data['Cate_Cn']
    unique_Category_ID = filtered_data['Cate_ID']
    unique_Category_is_tax_free = filtered_data['Cate_Is_Tax_Free'].copy()
    # Replacing NaN values with 0
    unique_Category_is_tax_free = unique_Category_is_tax_free.fillna(0)

    ## department_id	name	is_tax_free	font_color	bg_color	font_size	font_weight	sort	status	en	cn
    Category_data = [list(department_id),  ## department_id
                     list(unique_Category_En),  ## Name
                     list(unique_Category_is_tax_free), ## is_tax_free
                     ['#00000'] * len(unique_Category_En), ## font_color
                     ['#FFFFFF'] * len(unique_Category_En), ## bg_color
                     [None] * len(unique_Category_En), ## font_size
                     [None] * len(unique_Category_En), ## font_weight sort
                     list(unique_Category_ID),   ## sort
                     [1] * len(unique_Category_En),    ## One row/ status
                    list(unique_Category_En),
                    list(unique_Category_Cn)]
    # Convert to DataFrame
    Category_data = pd.DataFrame(list(zip(*Category_data)))
    return Category_data

## MenuItems_data
def MenuItems_data(df):
    item_is_tax_free_copy = df['Item_Is_Tax_Free'].copy()
    item_is_tax_free = item_is_tax_free_copy.fillna(0)
    ## name	upc	Abbreviation	item_type	bottle_deposit_id	bg_color	is_discountable	is_ebt	is_taxfree	is_check_id	Description	sort	status	en	cn
    MenuItems_data = [df['Item_En'],  ## name
                     df['UPC/Barcode'],  ## upc
                     [None] * len(df['Item_En']),  #### Abbreviation
                     df['Item_Type'], ## item_type
                     [0] * len(df['Item_En']), ## bottle_deposite
                     ['#FFFFFF'] * len(df['Item_En']), ## bg_color
                     [1] * len(df['Item_En']), ## is_discountable
                     [0] * len(df['Item_En']), ## is_ebt
                     list(item_is_tax_free), ## is_taxfree
                     [0] * len(df['Item_En']), ## is_check_id
                     [None] * len(df['Item_En']), ## Description
                     df['Item_ID'], ## sort
                     [1] * len(df['Item_En']), ## status
                    df['Item_En'],
                    df['Item_Cn'],]
    # Convert to DataFrame
    MenuItems_data = pd.DataFrame(list(zip(*MenuItems_data)))
    return MenuItems_data

if __name__ == "__main__":
    # Read the Excel file
    file_path =  r"C:\Users\UPCA02\Desktop\retail.xlsx"
    df = pd.read_excel(file_path, engine='openpyxl')
    # Call function
    result1 = Department_data(df)
    result2 = MenuItems_data(df)
    result3 = Category_data(df)
    print(result1)
    print(result2)
    print(result3)
