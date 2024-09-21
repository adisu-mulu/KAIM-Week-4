#import necessary libraries
import pandas as pd


class EdaCustomerBehavior:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        # Code to analyze customer purchasing behavior
        return pd.read_csv(self.path)