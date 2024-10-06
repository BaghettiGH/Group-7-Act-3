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
from mpl_toolkits.mplot3d import Axes3D
from io import StringIO""")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import squarify
from mpl_toolkits.mplot3d import Axes3D
from io import StringIO

st.markdown(""" ### `Initializing and describing the data set`  """)

st.code(""" df = pd.read_csv("datasets/Electronic_sales_Sep2023-Sep2024.csv")""")
df = pd.read_csv("datasets/Electronic_sales_Sep2023-Sep2024.csv")
st.code("df.info()")

buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()

st.text(df_info_as_string)

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
# Code here
st.markdown("#### `Box plot`")
# Code here

st.markdown("""
### `Hojilla`  
#### Graphs and Observations(Line chart and Histogram)
         """)
st.markdown("#### `Line chart`")
# Code here
st.write("Ratio of product type bought per gender")
df[['Gender', 'Product Type']].head(20)
st.write("Gender and product type ratio line chart")
def Gender_ProductType_Ratio ():
 gender_stats = df['Gender'].head(20)
 productType_stats = df['Product Type'].head(20)

 plt.plot(productType_stats, gender_stats, marker = 'o', linestyle = '-', color = 'b')
 plt.title('Gender to Product type bought ratio (20 Transactions)')
 plt.xlabel('Product Type')
 plt.ylabel('Gender')
 plt.xticks(rotation=45)
 plt.grid(True)
 plt.show()

Gender_ProductType_Ratio ()
st.markdown("#### `Histogram`")
# Code here

st.write("Payment methods count")
df['Payment Method']
st.write("Payment method histogram")
def PaymentMethod_histogram():
  Payment_method = df['Payment Method']

  plt.hist(Payment_method, bins=50, color='orange', edgecolor='black')
  plt.title('Payment methods used')
  plt.xlabel('Payment method')
  plt.ylabel('Count')
  plt.show()
PaymentMethod_histogram()

st.markdown("""
### `Jaso`            
#### Graphs and Observations(Tree map and Area Chart)  
            """)
st.markdown("#### `Tree map`")
# Code here
st.markdown("#### `Area chart`")
# Code here

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
st.markdown("#### `Bubble chart`")
# Code here s

st.markdown("""
### `Conclusion`
Insights from Data Visualization and Analysis per member:

1. ### `Dizon`
*   
*   
2. ### `Hojilla`
*   
*   
3. ### `Jaso`
*   
*  
4. ### `Molina`
*   Most of the transactions made are by smartphones contributing to **29.9%** of the data set. Other product types such as Smartwatch, Laptop, Tablet, Headphones contribute **20.5%**, **19.9%**, **19.7%**, and **10.1%** respectively  
*   **Smartphones** has the highest number of completed and cancelled transactions while **Headphones** has the lowest number of transactions in product types
5. ### `Nanwani`
*   
*              
       """)



