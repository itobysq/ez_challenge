"""
Module for adding to and visualizing delivery data
"""

import pandas as pd

class DeliveryTableError(Exception):
    def __init__(self):
        Exception.__init__(self, "Expected common column order_id, did not\
                                  find it")

class DeliveryTable(object):
    """
    Class for building a table of delivery data and visualizing it
    Args:
        geo_fn (string): a filepath pointing to a csv of delivery geography.
        delivery_fn (string): a filepath pointing to a csv of delivery data.
    """
    def __init__(self, geo_fn, delivery_fn):
        geo_df = pd.read_csv(geo_fn)
        delivery_df = pd.read_csv(delivery_fn)

        #Check to ensure that we do have orderid in both columns before merge
        if ('orderid' not in geo_df.columns) | ('orderid' not in delivery_df.columns):
            raise DeliveryTableError
        self.delivery_info = pd.merge(geo_df, delivery_df, on='orderid',
                                      how='outer', index_col=0)

if __name__ == "__main__":
    mytable = DeliveryTable('delivery_geography.csv', 'delivery_prices.csv')
    print(mytable.delivery_info.head())
