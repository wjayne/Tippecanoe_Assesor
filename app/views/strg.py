##Single tenant retail - General
import os
from xlrd import *
from flask import Blueprint, render_template
from flask import request
import pandas as pd

from functions import *
from app.settings import APP_STATIC

strg = Blueprint('strg', __name__)

@strg.route('/', methods=['POST'])
def strg_output():
    parcel = request.form['parcelNumber']

    hotels = read_excel(os.path.join(APP_STATIC, 'Copy of MASTER INCOME DATA.xlsx'))
    if any(hotels.Parcel_ID == parcel):
        row = search_row(hotels, parcel)

        headers = row.dtypes.index

        info = get_golf_info(row)
        revenue = get_str_revenue(row)
        expenses = get_str_expenses(row)
        NOI = get_NOI(row)
        cap_rate = get_cap_rate(row)
        results = get_str_results(row)
        return render_template("output/str.html", info=info,
                                                  revenue=revenue,
                                                  expenses=expenses,
                                                  NOI=NOI,
                                                  results=results,
                                                  cap_rate=cap_rate)

    return "Parcel Number wasn't found"
