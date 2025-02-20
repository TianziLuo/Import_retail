import pandas as pd
## Department_data
def Item_SKU_data(df):
    cost_copy = df['Cost'].copy()
    cost = cost_copy.fillna(0)
    ## Key	item_id	barcode	sku_name	sku_code	sku_price	Sku_cost	is_stock	sku_stock	sort	status
    Item_SKU_data = [[None] * len(df['Item_En']),  ## Key
                        df['Item_ID'],   ## item_ID
                        df['UPC/Barcode'],  ## barcode
                        [None] * len(df['Item_ID']),   # sku_name
                        df['SKU'],  ## sku_code
                        df['Price'],  ## sku_price
                        list(cost), ## sku_cost
                        [1] * len(df['Item_ID']), ## is_stock
                        df['Item_Stock'], ## sku_stock
                        df['Item_ID'], ## sort
                        [1] * len(df['Item_ID'])] ##status

    # Convert to DataFrame
    Item_SKU_data = pd.DataFrame(list(zip(*Item_SKU_data)))
    return Item_SKU_data

def CatalogyToItem_data(df):
    ## Department_id	Category_id	item_id	sort
    CatalogyToItem_data = df.iloc[:, [0,3,7,7]]
    return CatalogyToItem_data

def ItemToTax_data(df):
    ## Item_id	Tax_id	Sort
    ItemToTax_data = [
        df['Item_ID'],
        [1] * len(df['Item_ID']),
        df['Item_ID']]
    ItemToTax_data = pd.DataFrame(list(zip(*ItemToTax_data)))
    return ItemToTax_data 

if __name__ == "__main__":
    # Read the Excel file
    file_path = r"C:\Users\UPCA02\Desktop\retail.xlsx"
    df = pd.read_excel(file_path, engine='openpyxl')
    # Call function
    result1 = ItemToTax_data(df)
    result2 = CatalogyToItem_data(df)
    result3 = Item_SKU_data(df)
    print(result1)
    print(result2)
    print(result3)
