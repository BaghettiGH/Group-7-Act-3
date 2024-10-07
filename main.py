import streamlit as st

st.title("Group 7 Activity 3 - CSS145-BM4")

st.subheader("Group Members:") 
st.markdown("""
* Ma. Sophia Dizon
* Guillan Hojilla
* Louis Patrick Jaso
* Patrick Lawrence Molina
* Pratik Nanwani
            """)
st.markdown(""" ### `Importing Libraries` """)
st.code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import squarify
from io import StringIO""")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import squarify
from io import StringIO

st.markdown(""" ### `Initializing and describing the data set`  """)

st.code(""" df = pd.read_csv("datasets/Electronic_sales_Sep2023-Sep2024.csv")""")
df = pd.read_csv("datasets/Electronic_sales_Sep2023-Sep2024.csv")
st.code("df.info()")

st.write(df.info())

st.code("df.isna().sum()")

st.write(df.isna().sum())
st.code("df.describe()")
st.write(df.describe())

st.markdown(""" 

Description of each column names according to the dataset provider:
            
`Customer ID` - Identifier for customers           
`Age` -  Customer's age     
`Gender` - Customer's gender (Male or Female)    
`Loyalty Member` - (Yes/No) (Value changes over time)    
`Product Type` - Type of product sold (Eg. Smartphone, Laptop, Tablet)   
`SKU` - unique code for each product  
`Rating` - Customer's rating for the product (1-5 stars)  
`Order Status` - Completed, Cancelled  
`Payment Method` - Method use to pay for product (Eg. Cash, Credit card, Paypal)  
`Total Price` - Total price of the transaction  
`Unit Price` - Price per unit of the product  
`Quantity` - Number of units purchased  
`Purchase Date` - Date of purchase  
`Shipping Type` - (Eg. Standard, Overnight, Express)  
`Add-ons Purchased` - List of any additional items purchased  
`Add-on Total` - Total price of add-ons purchased  
            
""")

st.markdown(""" 
### `Dizon`
#### Graphs and Observations(Scatter plot and Box plot)
            """)
st.markdown("#### `Scatter plot`")
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.scatterplot(x='Quantity', y='Total Price', hue='Product Type', data=df, palette='viridis')
plt.title('Scatter Plot of Quantity vs Total Price by Product Type')
plt.xlabel('Quantity')
plt.ylabel('Total Price')
plt.show()
st.pyplot(plt)
plt.clf()
st.markdown("#### `Box plot`")

plt.figure(figsize=(10, 8))
sns.boxplot(x='Rating', y='Total Price', data=df)
plt.title('Box Plot: Total Price by Rating', fontsize=16)
plt.xlabel('Rating')
plt.ylabel('Total Price')
plt.show()
st.pyplot(plt) 
plt.clf()
st.markdown("""
### `Hojilla`  
#### Graphs and Observations(Line chart and Histogram)
         """)
st.markdown("#### `Line chart`")
# Code here
st.write("Ratio of product type bought per gender")
age_rating= df[['Age', 'Rating']].head(20)
st.write(age_rating)
st.write("Age to rating given ratio line chart")
def Age_Rating_Ratio():
    Age_stats = df['Age'].head(20)
    Rating_stats = df['Rating'].head(20)
    
    sorted_data = df[['Age', 'Rating']].head(20).sort_values(by='Age')
    Age_stats_sorted = sorted_data['Age']
    Rating_stats_sorted = sorted_data['Rating']
    
    plt.plot(Age_stats_sorted, Rating_stats_sorted, marker='o', linestyle='-', color='b')
    plt.title('Ratings given per age')
    plt.xlabel('Age')
    plt.ylabel('Rating')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    st.pyplot(plt)
    plt.clf()
Age_Rating_Ratio()

st.markdown("#### `Histogram`")
# Code here
st.write("Payment methods count")
count_pay_method=df['Payment Method'].value_counts()
st.write(count_pay_method)
st.write("Payment method histogram")
def PaymentMethod_histogram():
  Payment_method = df['Payment Method']

  plt.hist(Payment_method, bins=50, color='orange', edgecolor='black')
  plt.title('Payment methods used')
  plt.xlabel('Payment method')
  plt.ylabel('Count')
  plt.show()
  st.pyplot(plt)
  plt.clf()
PaymentMethod_histogram()

st.markdown("""
### `Jaso`            
#### Graphs and Observations(Tree map and Area Chart)  
            """)
st.markdown("#### `Tree map`")



st.markdown("#### `Area chart`")


st.markdown("""
### `Molina`
#### Graphs and Observations(Pie chart and Bar chart)
            """)
st.markdown("#### `Pie chart`")
# Code here
st.write("Showing the count of each type of products")
count_product_type= df['Product Type'].value_counts()
st.write(count_product_type)
total_products=5978 +4104+ 3973 + 2011
st.write(f"Total number of Products transacted:{total_products}")

st.subheader("Transaction made per Product Type")
def product_type_pie ():
  plt.pie(count_product_type, labels = ['Smartphone', 'Smartwatch', 'Laptop','Tablet','Headphones'], autopct='%1.1f%%', colors=['cornsilk','darkgoldenrod','sandybrown','bisque','burlywood'])
  plt.title('Transaction made per Product Type')
  st.pyplot(plt)
  plt.clf()

product_type_pie()
st.markdown("""From the pie chart, we can observed that the percentage of transactions made per product type are: **29.9%** Smartphone, **20.5** Smartwatch,
            **19.9%** Laptop, **19.7%** Tablet, **10.1** Headphones""")

st.markdown("#### `Bar chart`")
# Code here
st.write("Showing count of Product Type and Order Status")
order_status_type_count = df[['Product Type','Order Status']].value_counts()
st.write(order_status_type_count)
def order_status_per_type():
  plt.title("Order Status of Product Types")
  sns.countplot(x='Product Type',hue='Order Status', data=df, palette=['lightcoral','limegreen'])
  plt.xlabel("Product Type")
  plt.ylabel("Count")
  st.pyplot(plt)
  plt.clf()
st.subheader("Order Status of Product Types")
order_status_per_type()
st.markdown(""" **Smartphones** have the highest completed and cancelled transactions while **Headphones** have the lowest number of completed and cancelled transactions.
            Versatility of the products could be a factor of the high count""")


st.markdown("""
### `Nanwani`
#### Graphs and Observations(Heatmap and Bubble chart)
            """)
st.markdown("#### `Heatmap`")
# Code here
numerical_df=df.select_dtypes(include=[float, int])
corr_matrix = numerical_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16)
plt.show()
st.pyplot(plt)
plt.clf()

st.markdown("#### `Bubble chart`")
# Code here 
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Age', y='Total Price', 
                size='Quantity', 
                sizes=(40, 400), 
                hue='Gender',     
                data=df, 
                alpha=0.6,        
                palette="viridis")  
plt.title('Bubble Chart: Age vs Total Price with Quantity as Bubble Size', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Total Price')
plt.show()
st.pyplot(plt)
plt.clf()
st.markdown("""
### `Conclusion`
Insights from Data Visualization and Analysis per member:

1. ### `Dizon`
*  The scatter plot visualizes the relationship between Quantity and Total Price across different Product Types, revealing trends and clusters, aiding in understanding pricing dynamics based on quantity sold.
*  The box plot reveals that higher ratings generally correspond to varied total prices, indicating a wider price range for lower-rated products and more consistency in prices for higher-rated items.*   
2. ### `Hojilla`
*  The line chart shows the line fluctuating on the reviews given per age, based on the data from 20 transactions, though it mostly fluctuates between 2 stars, 3 stars, and 5 stars. 
*  According to the data shown by the histogram, credit card is the most used mode of payment, towering over the other payment methods. 
3. ### `Jaso`
*  Indication permits that the data is skewed to the right, which suggests a higher concentration of higher entropy values in the distribution. This implies that most URLs have a higher level of complexity or randomness.
*  The analysis of the Boolean features within the dataset reveals that three key figures predominantly represent the primary features.
4. ### `Molina`
*   Most of the transactions made are by smartphones contributing to **29.9%** of the data set. Other product types such as Smartwatch, Laptop, Tablet, Headphones contribute **20.5%**, **19.9%**, **19.7%**, and **10.1%** respectively  
*   **Smartphones** has the highest number of completed and cancelled transactions while **Headphones** has the lowest number of transactions in product types
5. ### `Nanwani`
*   The heatmap reveals strong correlations between certain variables, such as "Total Price" and "Quantity," while highlighting weak or no relationships between others, offering insights for targeted data-driven decisions.
*   The bubble chart shows that higher quantities are generally purchased by middle-aged customers, with total prices varying widely across ages.           
       """)



