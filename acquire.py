import pandas as pd
import requests
import os



def get_items_data():
    '''This function will connect to thehttps://python.zach.lol/api/v1/items. It will then cache a local copy to the computer to use for later
        in the form of a CSV file.'''
    filename = "items.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
    #empty list for holding items
        items_list = []
        response = requests.get('https://python.zach.lol/api/v1/items')
        data = response.json()
        n = data['payload']['max_page']
        #from items in json, turn into a list
        for i in range(1,n+1):
            url = 'https://python.zach.lol/api/v1/items?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['items']
            items_list += page_items
        #turn items from list into a dataframe
        items = pd.DataFrame(items_list)
        return items



def get_stores_data():
    '''This function will connect to thehttps://python.zach.lol/api/v1/stores. It will then cache a local copy to the computer to use for later
        in the form of a CSV file.'''
    filename = "stores.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
    #empty list for holding items
        items_list = []
        response = requests.get('https://python.zach.lol/api/v1/stores')
        data = response.json()
        n = data['payload']['max_page']
        #from items in json, turn into a list
        for i in range(1,n+1):
            url = 'https://python.zach.lol/api/v1/stores?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_stores = data['payload']['stores']
            stores_list += page_stores
        #turn items from list into a dataframe
        stores = pd.DataFrame(stores_list)
        return stores




def get_sales_data():
    '''This function will connect to thehttps://python.zach.lol/api/v1/sales. It will then cache a local copy to the computer to use for later
        in the form of a CSV file.'''
    filename = "sales.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
    #empty list for holding items
        items_list = []
        response = requests.get('https://python.zach.lol/api/v1/sales')
        data = response.json()
        n = data['payload']['max_page']
        #from items in json, turn into a list
        for i in range(1,n+1):
            url = 'https://python.zach.lol/api/v1/ale?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_sales = data['payload']['salees']
            sales_list += page_sales
        #turn items from list into a dataframe
        sales = pd.DataFrame(sales_list)
        return sales



def make_one_df():
    items = pd.read_csv('items.csv', index_col=0)
    stores = pd.read_csv('stores.csv', index_col=0)
    sales= pd.read_csv('sales.csv', index_col=0)
    # Merge sales with stores
    complete_df = sales.merge(stores, left_on='store', right_on='store_id')
    # Merge sales and stores on items
    complete_df = complete_df.merge(items, left_on='item', right_on='item_id')
    # Make complete dataframe to a csv
    complete_df.to_csv('complete_df.csv')
    return complete_df


def read_url_csv(url):
    df = pd.read_csv(url, index_col=0)
    df = pd.DataFrame(df)
    return df