
#!/usr/bin/env python
# encoding: utf-8

"""
.. module:: visualize_wealth.test_module.test_construct_portfolio.py

.. moduleauthor:: Benjamin M. Gross <benjaminMgross@gmail.com>

"""
import os
import pytest
import numpy
import pandas
import tempfile
import datetime
from pandas.util import testing
from visualize_wealth import construct_portfolio

@pytest.fixture
def load_panel_sheet():
    f = './test_data/panel from weight file test.xlsx'
    return pandas.ExcelFile(f)
    """

    >>> weight_df = xl_file.parse('rebal_weights', index_col = 0)
    >>> tickers = ['EEM', 'EFA', 'IYR', 'IWV', 'IEF', 'IYR', 'SHY']
    >>> d = {}
    >>> for ticker in tickers:
    ...     d[ticker] = xl_file.parse(ticker, index_col = 0)
    >>> panel = panel_from_weight_file(weight_df, pandas.Panel(d), 
    ...     1000.)
    >>> portfolio = pfp_from_weight_file(panel)
    >>> manual_calcs = xl_file.parse('index_result', index_col = 0)
    >>> put.assert_series_equal(manual_calcs['Close'], 
    ...     portfolio['Close'])
    """

def test_funs():
    """
    >>> import pandas.util.testing as put
    >>> xl_file = pandas.ExcelFile('../tests/test_splits.xlsx')
    >>> blotter = xl_file.parse('blotter', index_col = 0)
    >>> cols = ['Close', 'Adj Close', 'Dividends']
    >>> price_df = xl_file.parse('calc_sheet', index_col = 0)
    >>> price_df = price_df[cols]
    >>> split_frame = calculate_splits(price_df)

    >>> shares_owned = blotter_and_price_df_to_cum_shares(blotter, 
    ...     split_frame)
    >>> test_vals = xl_file.parse(
    ...     'share_balance', index_col = 0)['cum_shares']
    >>> put.assert_almost_equal(shares_owned['cum_shares'].dropna(), 
    ...     test_vals)
    True
    >>> f = '../tests/panel from weight file test.xlsx'
    >>> xl_file = pandas.ExcelFile(f)
    >>> weight_df = xl_file.parse('rebal_weights', index_col = 0)
    >>> tickers = ['EEM', 'EFA', 'IYR', 'IWV', 'IEF', 'IYR', 'SHY']
    >>> d = {}
    >>> for ticker in tickers:
    ...     d[ticker] = xl_file.parse(ticker, index_col = 0)
    >>> panel = panel_from_weight_file(weight_df, pandas.Panel(d), 
    ...     1000.)
    >>> portfolio = pfp_from_weight_file(panel)
    >>> manual_calcs = xl_file.parse('index_result', index_col = 0)
    >>> put.assert_series_equal(manual_calcs['Close'], 
    ...     portfolio['Close'])
    """
    return None