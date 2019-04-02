import pandas as pd
import numpy as np
import pandas_datareader as pdr


def Exercise_1():
    symbol = "SPY"
    start_date = "2016-01-01"
    end_date = "2018-08-20"
    data = pdr.get_data_stooq(symbol, start=start_date, end=end_date)
    data.sort_index(inplace=True)
    return data


def Exercise_2(data):
    filepath = "data.csv"
    data.to_csv(filepath)
    return


def Exercise_3():
    filepath = "data.csv"
    data2 = pd.read_csv(filepath, parse_dates=True, index_col=0)
    return data2


def Exercise_4(data):
    close_mean = data.Close.rolling(20).mean()
    data['MA'] = close_mean
    return data


def Exercise_5(data):
    std_dev = data.Close.rolling(20).std()
    data['BB_Up'] = data.Close + std_dev * 2
    data['BB_Dn'] = data.Close - std_dev * 2
    return data


def Exercise_6(data):
    # note you can also use: rets = data.Close.pct_change()
    rets = (data.Close - data.Close.shift(1)) / data.Close.shift(1)
    data['Returns'] = rets
    return data


def Exercise_7(data):
    # generate volume-weighted returns and store in our data
    data['VR'] = data.Returns * data.Volume

    # create the custom function that does steps b-d.
    def vmomentum(col_data: pd.Series):
        c_up = 0
        c_dn = 0
        best_up = 0
        best_dn = 0

        for x in col_data:
            if x > 0:
                c_up += x
                best_up = c_up if c_up > best_up else best_up
                best_dn = c_dn if c_dn < best_dn else best_dn
                c_dn = 0
            elif x < 0:
                c_dn += x  # adds a negative value
                best_dn = c_dn if c_dn < best_dn else best_dn
                best_up = c_up if c_up > best_up else best_up
                c_up = 0

        spread = best_up + best_dn
        total = np.abs(col_data).sum()
        ratio = spread / total
        return ratio

    # apply the custom function over a 20 day window for our data
    data['VMom'] = data.VR.rolling(20).apply(vmomentum, raw=False)

    return data


def unified_solution():
    data = Exercise_1()  # request data
    Exercise_2(data)     # store data to disk

    data = Exercise_3()  # load data from disk
    data = Exercise_4(data)  # append the moving average
    data = Exercise_5(data)  # append the Bollinger bands
    data = Exercise_6(data)  # append the returns
    data = Exercise_7(data)  # append our momentum indicator
    return data
