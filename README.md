# ECE2112-Python-Exploratory_Data_Analysis


# Insights Gained 🔍


# Challenges 🎯
***Missing Values and Duplicates***❓
* Since the Dataset contains duplicates and missing values, proceeding beyond "Basic Descriptive Statistics" becomes tricky. Must be able to find a way to find mean, mode, standard deviation whilst dealing with missing values.
  - Solution ✅: Perform a data cleaning to fix missing values and duplicates.
 
***Spreadsheet Loading Error***⁴⁰⁴
* Upon trying to load the spreadsheet, I was greeted with the following error:
![image](https://github.com/user-attachments/assets/e0d61703-32f5-4b8d-b5ab-4d0ab49f3118)
  - Solution ✅: Specify the encoding when loading the csv file into something that python would understand, in my case I used 'cp1252'.
    ![image](https://github.com/user-attachments/assets/00215df2-c981-460b-99e7-97e5f3077497)



# History 📜
* Version 1.0 (11/02/24)
  - Initial commit of the notebook
  - Overview of Dataset

* Version 2.0 (11/03/24)
  - Used a new and cleaned spreadsheet data
  - Also included the Data Cleaning notebook
* Version 2.1 (11/04/24)
  - Changed a line of code that replaces blank entries from the 'key' column due to issues by adding " ", right and before the 'N/A'.
  - originally was
    ```javascript
    dataset['key'] = dataset['key'].fillna('N/A')
    ```
