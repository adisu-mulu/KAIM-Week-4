#import necessary libraries
import pandas as pd


class EdaCustomerBehavior:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        # Code to analyze customer purchasing behavior
        return pd.read_csv(self.path)
    
    def get_sales_before_during_after_holidays(self, df, days=3):
        holiday_dates = df[df['StateHoliday'] != '0']['Date']
        
        # Create lists to store sales data
        sales_before, sales_during, sales_after = [], [], []
        
        for holiday in holiday_dates:
            # Filter sales during the holiday
            during_sales = df[df['Date'] == holiday]['Sales'].sum()
            
            # Filter sales for days before the holiday
            before_sales = df[(df['Date'] >= holiday - pd.Timedelta(days=days)) & 
                            (df['Date'] < holiday)]['Sales'].sum()
            
            # Filter sales for days after the holiday
            after_sales = df[(df['Date'] > holiday) & 
                            (df['Date'] <= holiday + pd.Timedelta(days=days))]['Sales'].sum()
            
            # Append results to lists
            sales_before.append(before_sales)
            sales_during.append(during_sales)
            sales_after.append(after_sales)
        
        return sales_before, sales_during, sales_after