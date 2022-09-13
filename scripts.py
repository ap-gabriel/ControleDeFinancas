from datetime import date as dt
import calendar as cl

# DATE REGISTRATION #
def DateInput():
    
    # VARIABLES #
    global date
    i = 0
    l_date = []
    date_type = ["Year", "Month", "Day"]
    date_limit = [dt.today().year, 12, 31]
    i_date = 0

    # DATE INPUT #
    print("")
    while i == 0:
        try:
            # LIMIT DAY TO CURRENT MONTH #
            if i_date == 2:
                days_month = cl.monthrange(l_date[0], l_date[1])
                date_limit[2] = days_month[1]
            # FUTURE DATE LIMITER #
            if i_date == 1 and l_date[0] == dt.today().year:
                date_limit[1] = dt.today().month
            elif i_date == 2 and l_date[0] == dt.today().year and l_date[1] == dt.today().month:
                date_limit[2] = dt.today().day
            # INPUT DATE LOOP #
            input_date = int(input(f"Input {date_type[i_date]}: "))
            # INVALID VALUE #
            if not input_date >= 1 or not input_date <= date_limit[i_date] or not isinstance(input_date, int):
                raise ValueError
            else:
                # ADD INPUT TO DATE LIST #
                l_date.append(input_date)
                i_date += 1
                # LEAVE LOOP AFTER D/M/Y INPUT #
                if i_date > 2:
                    date = f"{l_date[2]}/{l_date[1]}/{l_date[0]}"
                    return date
        except ValueError:
            print("\nInvalid Value.\n")

# PROFIT EXPENSE REGISTRATION #
def ValueInput(pointer):

    # VARIABLES #
    global value
    i = 0
 
    # VALUE INPUT #
    while i == 0:
        try:
            # INPUT VALUE IN R$ #
            input_value = float(input(f"\nTo add centavos, use . (Ex: 0.40, 20.70)\nType {pointer} value: "))
            # INVALID VALUE #
            if not isinstance(input_value, float):
                raise ValueError
            # INPUT PROFIT/EXPENSE VALUE #
            else:
                value = input_value
                print(f"{pointer.capitalize()} succesfully registered.\n")
                return value
        except ValueError:
            print("\nInvalid Value.\n")

# BUILD ARRAYS #
def RegisterData():

    # VARIABLE #
    global profit
    global expense
    profit = []
    expense = []

    # REGISTER PROFIT #
    pointer_text = "profit"
    DateInput()
    ValueInput(pointer_text)
    profit.append(int(value))
    
    # REGISTER EXPENSE #
    pointer_text = "expense"
    ValueInput(pointer_text)
    expense.append(-value)

    return (profit, expense)