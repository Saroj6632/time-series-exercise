import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

from acquire import get_stores_data, get_sales_data, get_items_data, make_one_df



def prep_store_df():
    """
    Function acquires dataframe from acquire and prepares the dataframe for time series analysis
    """
    df = make_one_df()
    df=df.drop(columns=['sale_id', 'store_id','item_id'])
    # Convert sale_date to DateTimeIndex
    df['sale_date'] = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    
    # Create date part columns
    df['month'] = df.index.month
    df['weekday'] = df.index.day_name()
    
    # Create calculated columns
    df = df.assign(sales_total = df.sale_amount * df.item_price)
    df = df.assign(sales_diff = df.sales_total.diff(periods=1))
    
    # Change dtypes of numeric columns to object and category
    df = (df.astype({'sale_id': object, 'store_id': object, 
                     'store_zipcode': object, 'item_id': object, 
                     'item_upc12': object, 'item_upc14': object, 
                     'month': 'category', 'weekday': 'category'}))
    return df




def prep_energy_df():
    """
    Function to acquires the csv from acquire and prepares the dataframe for time series analysis
    """
    df= make_opsd_csv()
    # Convert sale_date to DateTimeIndex
    df['Date'] = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    
    # Create date part columns
    df['month'] = df.index.month
    df['weekday'] = df.index.day_name()
    
    # Fill NaN
    df = df.fillna(0)
    
    # Display distributions of numeric columns
    numeric_hists(df)
    return df