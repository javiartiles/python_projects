# ------------------------------------ #
# Javier Artiles Manrique de Lara
# MSBA 503 - Analytics Programming II
# Homework 5: API Crypto Exchange Rate
# ------------------------------------ #

# ----------------------- #
# Part 0: Import packages #
# ----------------------- #

import tkinter
from tkinter import messagebox
import numpy as np
import pandas as pd
import requests
import json

# ------------------------ #
# Part 1: Get the API link #
# ------------------------ #

API = "http://api.coinlayer.com/api/live?access_key=4aed50fefacd511a3da720e5ca2746e8"

# -------------------------------- #
# Part 2: Create GUI calculator #
# -------------------------------- #

GUI = tkinter.Tk()
GUI.title("Exchange Rate Calculator")
GUI.configure(background ="bisque")

# ------------------------------------- #
# Part 3: Create all labels and widgets #
# ------------------------------------- #

# 3.1 Bitcoin
btc_lbl = tkinter.Label(GUI, text ="BTC:", font = ("Arial Bold", 15), bg ="bisque")
btc_lbl.grid(column = 0, row = 0, padx = 5, pady = 5)
btc_box = tkinter.Entry(GUI, width=10)
btc_box.grid(column=1, row=0, pady=2)

# 3.2 Ethereum
eth_lbl = tkinter.Label(GUI, text ="ETH:", font = ("Arial Bold", 15), bg ="bisque")
eth_lbl.grid(column = 0, row = 1, padx = 5, pady = 5)
eth_box = tkinter.Entry(GUI, width=10)
eth_box.grid(column=1, row=1, pady=2)

# 3.3 BNB
bnb_lbl = tkinter.Label(GUI, text ="BNB:", font = ("Arial Bold", 15), bg ="bisque")
bnb_lbl.grid(column = 2, row = 0, padx = 5, pady = 5)
bnb_box = tkinter.Entry(GUI, width=10)
bnb_box.grid(column=3, row=0, pady=2)

# 3.4 XRP
xrp_lbl = tkinter.Label(GUI, text ="XRP:", font = ("Arial Bold", 15), bg ="bisque")
xrp_lbl.grid(column = 2, row = 1, padx = 5, pady = 5)
xrp_box = tkinter.Entry(GUI, width=10)
xrp_box.grid(column=3, row=1, pady=2)

# ----------------------------- #
# Part 4: Create convert button #
# ----------------------------- #

convertion_button = tkinter.Button(GUI, text ="Convert currency", bg ="pale green", fg ="black")
convertion_button.grid(column = 4, row = 0, padx=5, pady=5)

# --------------------------- #
# Part 5: Create close button #
# --------------------------- #

close_button = tkinter.Button(GUI, text ="Close converter", bg ="dark orange", fg ="black")
close_button.grid(column = 4, row = 1, padx=5, pady=5)

# ------------------------------------------ #
# Part 6: Create convert and close functions #
# ------------------------------------------ #

def convert_button():
    try:
        btc_answer = float(btc_box.get())
        bnb_answer = float(bnb_box.get())
        eth_answer = float(eth_box.get())
        xrp_answer = float(xrp_box.get())

        coins = [btc_answer, eth_answer, bnb_answer, xrp_answer]

        # 6.1 Get all the data from the API
        api_request = requests.get(API)
        data = json.loads(api_request.text)

        btc_rate = data["rates"]["BTC"]
        bnb_rate = data["rates"]["BNB"]
        eth_rate = data["rates"]["ETH"]
        xrp_rate = data["rates"]["XRP"]

        # 6.2 Calculations to storage in the future file
        prices = [btc_rate, bnb_rate, eth_rate, xrp_rate]
        prices = np.around(prices, decimals=2)

        conversion = list(np.multiply(coins, prices))
        conversion = np.around(conversion, decimals = 2)

        exchange_rate = np.divide(coins, conversion)
        exchange_rate = np.around(exchange_rate, decimals = 5)

        tkinter.messagebox.showinfo("Conversion Completed!",
                                    "Your conversion has been completed and saved to crypto_conversions.csv")

    except:
        tkinter.messagebox.showerror("Error!",
                                     "All boxes must be filled before conversion.")

    # 6.3 Create the .csv file and import all the data
    file = pd.DataFrame({"Currency": ["BTC", "BNB", "ETH", "XRP"],
                         "Unity Price": [prices[0], prices[1], prices[2], prices[3]],
                         "Quantity": [btc_answer, eth_answer, bnb_answer, xrp_answer],
                         "Total Price (USD)": [conversion[0], conversion[1], conversion[2], conversion[3]],
                         "Exchange Rate USD/CRYPTO": [exchange_rate[0], exchange_rate[1], exchange_rate[2], exchange_rate[3]]
                         })

    file.to_csv("crypto_currency.csv", index=False)

def close_window():
    GUI.destroy()
    exit()

# ----------- #
# Part 7: END #
# ----------- #

convertion_button.configure(command = convert_button)
close_button.configure(command = close_window)

GUI.mainloop()
