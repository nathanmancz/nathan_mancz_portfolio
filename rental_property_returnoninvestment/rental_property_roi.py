# Functions
def decimal_to_percent(decimal):
    """
    This function converts decimals to percentages
    :param decimal: 
    :return:  
    """
    return "{:.2f}%".format(decimal * 100)


def monthly_to_annual_rent(monthly_rent):
    """
    This function returns the annual rent based on the monthly rent
    :param monthly_rent:
    :return:
    """
    return monthly_rent * 12


def return_on_investment(annual_rent, purchase_price):
    """
    This function works out the return on investment (roi) based on annual rent and purchase price
    :param annual_rent:
    :param house_price:
    :return: 
    """
    return (annual_rent / purchase_price)


# Variables
purchase_price = 250000.00
monthly_rent = 1200.00


# Main code
def main():
    annual_rent = monthly_to_annual_rent(monthly_rent)
    annual_roi_decimal = return_on_investment(annual_rent, purchase_price)
    annual_roi = decimal_to_percent(annual_roi_decimal)
    print(f"Based on a purchase price of £{purchase_price} and a monthly rental income of £{monthly_rent} achieves an annual roi of {annual_roi}")


if __name__ == "__main__":
    main()
