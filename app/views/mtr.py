##Single tenant retail - General
import os
from xlrd import *
from flask import Blueprint, render_template
from flask import request
import pandas as pd

from functions import *
from app.settings import APP_STATIC

mtr = Blueprint('mtr', __name__)

def mtr_output(parcel):
  
    hotels = read_excel(os.path.join(APP_STATIC, 'Copy of MASTER INCOME DATA.xlsx'))
    if any(hotels.Parcel_ID == parcel):
        row = search_row(hotels, parcel)

        headers = row.dtypes.index

        info = get_golf_info(row)
        if "Center" not in row['Sub_Category']:
            revenue = get_str_revenue(row)
        else:
            revevnue = mtr_center_revenue(row)
        expenses = get_str_expenses(row)
        NOI = get_NOI(row)
        cap_rate = get_cap_rate(row)
        results = get_str_results(row)
        children = get_child_parcels(row)
        return render_template("output/mtr.html", info=info,
                                                  revenue=revenue,
                                                  expenses=expenses,
                                                  NOI=NOI,
                                                  result=results,
                                                  cap_rate=cap_rate,
                                                  children=children)

    return "Parcel Number wasn't found"
