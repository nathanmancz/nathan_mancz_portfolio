# Packages used
import pandas as pd


# Read from csv - Stock data from Amazon, Apple, Google & Tesla 
amazon_stock_all_data = pd.read_csv('analysing_stock_data/AMZN.csv')
apple_stock_all_data = pd.read_csv('analysing_stock_data/AAPL.csv')
google_stock_all_data = pd.read_csv('analysing_stock_data/GOOG.csv')
tesla_stock_all_data = pd.read_csv('analysing_stock_data/TSLA.csv')

# Read from csv - Retrieve only the Dates and the Adj Close for Amazon, Apple, Google & Tesla 
amazon_stock_data = pd.read_csv('analysing_stock_data/AMZN.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date', 'Adj Close'])
apple_stock_data = pd.read_csv('analysing_stock_data/AAPL.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date', 'Adj Close'])
google_stock_data = pd.read_csv('analysing_stock_data/GOOG.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date', 'Adj Close'])
tesla_stock_data = pd.read_csv('analysing_stock_data/AMZN.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date', 'Adj Close'])


# Functions
def set_date_range(start_date: str, end_date: str):
    """
    This function sets the date range that the data will be read from
    :param start_date: The start date in the date range
    :param end_date: The end date in the date range
    :return: list, of all dates between the given start date and given end date
    """
    dates = pd.date_range(start_date, end_date)
    return dates


# Main code
def main():
    # Rename stock columns to specific company name
    amazon_stock = amazon_stock_data.rename(columns = {'Adj Close' : 'Amazon'})
    apple_stock = apple_stock_data.rename(columns = {'Adj Close' : 'Apple'})
    google_stock = google_stock_data.rename(columns = {'Adj Close' : 'Google'})
    tesla_stock = tesla_stock_data.rename(columns = {'Adj Close' : 'Tesla'})

    # Add stocks to the data frame between the dates chosen
    dates = set_date_range('2021-01-01', '2023-02-08')
    all_stocks = pd.DataFrame(index = dates)
    all_stocks = all_stocks.join(amazon_stock)
    all_stocks = all_stocks.join(apple_stock)
    all_stocks = all_stocks.join(google_stock)
    all_stocks = all_stocks.join(tesla_stock)
    
    # Analyse stock
    print(f"{all_stocks.describe()} \n")

    # Remove NaN from data frame
    all_stocks.isnull().sum()
    all_stocks.dropna(axis = 0, inplace = True)

    # Print the mean, median, standard deviation, and correlation of Amazon, Apple, Google & Tesla stocks
    print(f"The average stock price for the stocks are: \n {all_stocks.mean()} \n")
    print(f"The median stock price for the stocks are: \n {all_stocks.median()} \n")
    print(f"The standard deviation for the stocks are: \n {all_stocks.std()} \n")
    print(f"The correlation between stocks is: \n {all_stocks.corr()} \n")


if __name__ == "__main__":
    main()