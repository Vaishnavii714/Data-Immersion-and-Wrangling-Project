# Data-Immersion-and-Wrangling-Project
Data immersion and wrangling using Python and Pandas
Project Objective
The objective of this project is to perform data preprocessing by:

Understanding the dataset structure
Creating a data dictionary
Identifying data quality issues
Cleaning and transforming data
Performing feature engineering
Removing outliers
Preparing the final dataset for analysis
Dataset Description
The dataset contains customer demographic and purchase information.

Column Name	Description
Customer_ID	Unique customer identifier
Name	Customer name
Date_of_Birth	Customer birth date
Purchase_Date	Date of purchase
Purchase_Amount	Amount spent by customer
City	Customer location
Gender	Customer gender
Data Quality Issues Identified
During data profiling, the following issues were found:

Missing values in City and Purchase Amount
Duplicate customer records
Inconsistent Gender formatting
Outliers in Purchase Amount
Date format inconsistencies
Data Cleaning and Transformation Steps
Duplicate Removal
Duplicate rows were removed to maintain data accuracy and uniqueness.

Missing Value Handling
Missing City values were replaced with "Unknown"
Missing Purchase Amount values were replaced using mean value
Categorical Data Standardization
Gender column values were standardized to maintain consistency.

Date Conversion
Date_of_Birth and Purchase_Date columns were converted into datetime format.

Feature Engineering
A new column "Customer_Age" was created using Date_of_Birth.

Outlier Removal
Outliers in Purchase Amount were removed using the Interquartile Range (IQR) method.

Final Output
The final cleaned dataset is stored as:

cleaned_customer_sales.csv

This dataset is ready for analysis and machine learning applications.

Tools and Technologies Used
Python
Pandas
NumPy
Jupyter Notebook
Project Files
customer_sales_dataset.csv – Raw dataset
cleaned_customer_sales.csv – Clean dataset
data_dictionary.csv – Column description
data_cleaning.ipynb – Project implementation

Learning Outcomes
This project helped in understanding:

Real-world data cleaning techniques
Handling missing values and duplicates
Feature engineering methods
Statistical outlier detection
Data preprocessing workflow
#Author
Duddala Vaishnavi

This project was completed as part of internship training in data preprocessing and analysis.
