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
    unique_Category_En = df['Cate_En'].dropna().unique()
    unique_Category_Cn = df['Cate_Cn'].dropna().unique()
    unique_Category_ID = df['Cate_ID'].dropna().unique()
    unique_Category_is_tax_free = df['Cate_is_tax_free'].dropna()

    num_categories = len(unique_Category_En)
    ## department_id	name	is_tax_free	font_color	bg_color	font_size	font_weight	sort	status	en	cn
    Category_data = [list(unique_Category_ID),  ## ID
                     list(unique_Category_En),  ## Name
                     list(unique_Category_is_tax_free), ## is_tax_free
                     ['#00000'] * len(unique_Category_En), ## font_color
                     ['#FFFFFF'] * len(unique_Category_En), ## bg_color
                     [None] * len(unique_Category_En), ## font_size
                     [None] * len(unique_Category_En), ## font_weight sort
                     [1] * len(unique_Category_En),     # One row/ status
                    list(unique_Category_En),
                    list(unique_Category_Cn)]
    # Convert to DataFrame
    Category_data = pd.DataFrame(list(zip(*Category_data)))
    return Category_data
   
# Read the Excel file
file_path = r"C:\Users\tianz\OneDrive\桌面\retail.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
# Call function
result1 = Department_data(df)
result2 = Category_data(df)
print(result1,result2)

'''
## MenuItems_data
def MenuItems_data(df):
    MenuItems_data = df.iloc[:, [7,9,10,6,6,7,8]]
    columns_to_insert = {
        'FontColor': pd.Series(['#FFFFFF'] * len(df), index=df.index),
        'BackgroundColor': pd.Series(['#355d6e'] * len(df), index=df.index),
        'OneCol1': pd.Series([1] * len(df), index=df.index),
        'OneCol2': pd.Series([1] * len(df), index=df.index)
    }

    insert_index = 4
    for col_name, col_data in columns_to_insert.items():
        MenuItems_data.insert(insert_index, col_name, col_data)
        insert_index += 1

    return MenuItems_data

## CategoryToItem_data
def CatalogyToItem_data(df):
    CatalogyToItem_data = df.iloc[:, [3,6,6]]
    return CatalogyToItem_data 
'''