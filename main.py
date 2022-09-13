# IMPORTS #
import sys
import scripts as scr
import numpy as np
import pandas as pd

# VARIABLES #
option_pointer = 0
i = 0
data_ready = False

# GREETING MESSAGE #
print("\nWelcome to your finance control program.\n\nWhat do you need?")

# MAIN MENU #
while i == 0:
    try:
        # MENU INPUT #
        option_selection = int(input("1. Register profit\n2. Print Summary\n3. Convert Data\n4. Create Dataframe\n0. Exit\nOption: "))
        # CALL REGISTER DATA FUNCTION #
        if option_selection == 1:
            scr.RegisterData()
        # PRINT SUMMARY #
        elif option_selection == 2:
            if len(scr.profit) == 0 or len(scr.expense) == 0:
                print("\nNothing Registered\n")
            else:
                print(f"\n# HERE'S YOUR SUMMARY #\nProfits: {scr.profit}\nExpenses: {scr.expense}\nDate: {scr.date}\n")
        # CONVERT ARRAYS #
        elif option_selection == 3:
            if len(scr.profit) == 0 or len(scr.expense) == 0:
                print("\nNo Array to Convert.\n")
            else:
                np_data = np.array([[]])
                np_data = np.append(np_data,[[scr.profit[0], scr.expense[0]]], axis=1)
                data_ready = True
                print("\nArrays Converted!")
                print(f"{np_data}\n")
        # CREATE DATA FRAME #
        elif option_selection == 4:
            if not data_ready:
                print("\nData Isn't Ready.\n")
            else:
                #CREATE DATA FRAME
                df = pd.DataFrame(np_data, index=[scr.date], columns=['Profits', 'Expenses'])
                print("\nData Frame Created.\n")
                df.head()
                print(f"\n{df}\n")
        # EXIT #
        elif option_selection == 0:
            print("\nProgram finished.\n")
            sys.exit()
        # INVALID VALUE #
        else:
            raise ValueError
    except ValueError:
        print("\nInvalid Value.\n")