#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd


def loadAndReadDataset(dataset):
    """
        Load and read a CSV dataset into a Pandas DataFrame.

        Parameters:
        - dataset (str): The path or URL of the CSV file to be loaded.

        Returns:
        - df (pd.DataFrame): The DataFrame containing the loaded dataset.
    """
    df = pd.read_csv(dataset)
    return df


def lineGraph(data):
    """
        Generate a line graph to visualize diesel sales over years for different countries.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the diesel sales data.
                              It should have 'Year' as the first column and sales data for each country in subsequent columns.

        Returns:
        - None
    """
    plt.figure(figsize=(12 , 8))
    for country in data.columns[1:]:
        plt.plot(data['Year'] , data[country] , label=country)

    plt.title('Diesel sales over years')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()


def piegraph(data):
    """
        Generate a pie chart to visualize the distribution of sales across different categories.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing sales data.
                              It should have 'Category' and 'Sales' columns.

        Returns:
        - None
        """
    category_sales = data.groupby('Category')['Sales'].sum()
    plt.figure(figsize=(8 , 8))
    plt.pie(category_sales , labels=category_sales.index ,
            autopct='%1.1f%%' , startangle=140)
    plt.title('Distribution of Categories')
    plt.show()


def barGraph(data):
    """
        Generate a bar chart to visualize category-wise sales.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing sales data.
                              It should have 'Sub-Category' and 'Sales' columns.

        Returns:
        - None
    """
    # Group by Category and calculate the total sales
    category_sales = data.groupby('Sub-Category')['Sales'].sum()
    # Plotting the bar chart
    plt.figure(figsize = (10 , 6))
    category_sales.plot(kind = 'bar' , color = 'skyblue')
    plt.title('Category-wise Sales')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation = 45 , ha = 'right')
    plt.show()


#diesel dataset
diselData = loadAndReadDataset('diesel_prices.csv')
salesData = loadAndReadDataset('train.csv')

lineGraph(diselData)
piegraph(salesData)
barGraph(salesData)