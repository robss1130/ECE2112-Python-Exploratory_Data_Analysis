# ECE2112-Python-Exploratory_Data_Analysis



## Insights Gained 🔍
- When using data files in coding using python, I learned that not all files and encoding methods are compatible which leads to errors when reading files. Upon researching about it, it's because some data uses special characters that may cause issue to the programming language. An example is Python's Pandas lilbrary defaults to UTF-8 encoding, but the spreadsheet file that were using seems to not be compatible therefore I have to use an encoding compatible and chose 'cp1252' which made my code run as long as the data I'll be loading does not contain characters outside the Western European character set.


## Challenges 🎯
***Missing Values and Duplicates***❓
* Since the Dataset contains duplicates and missing values, proceeding beyond "Basic Descriptive Statistics" becomes tricky. Must be able to find a way to find mean, mode, standard deviation whilst dealing with missing values.
  - Solution 🔧: Perform a data cleaning to fix missing values and duplicates.
 
***Spreadsheet Loading Error***⁴⁰⁴
* Upon trying to load the spreadsheet, I was greeted with the following error:
![image](https://github.com/user-attachments/assets/e0d61703-32f5-4b8d-b5ab-4d0ab49f3118)
  - Solution 🔧: Specify the encoding when loading the csv file into something that python would understand, in my case I used 'cp1252'.
    ```javascript
    # Load the spreadhsheet
    new_path = r"C:\Users\PC\Documents\Python Codes\Modules\Incentives\Top Spotify Music Incentives\spotify-2023.csv"

    # Specify the encoding
    dataset = pd.read_csv(new_path, encoding='cp1252')
    ```

***Encountering non-numeric values***
* Aside from missing values and duplicates, seems like I've skipped over some rows that contains non-numeric values on a column that is meant to only contain numerical values causing problems later on the coding. This issue causes ineffecient use of time, being forced to deal with setting up the spreadsheet once again.
* e.g.: ![image](https://github.com/user-attachments/assets/419da2ca-2665-4087-8833-22b15d682319)
  - Solution 🔧: Keeping the data cleaning notebook for quick fixes.



## History 📜
* Version 1.0 (11/02/24)
  - Initial commit of the notebook.
  - Overview of Dataset.

* Version 2.0 (11/03/24)
  - Used a new and cleaned spreadsheet data.
  - Also included the Data Cleaning notebook.
  - Also included the spreadsheet used.
* Version 2.1 (11/04/24)
  - Changed a line of code that replaces blank entries from the 'key' column due to issues by adding " ", right and before the 'N/A'.
  - Changed to:
    ```javascript
    dataset['key'] = dataset['key'].fillna('"N/A"')
    ```
  - Originally was:
    ```javascript
    dataset['key'] = dataset['key'].fillna('N/A')
    ```
* Version 2.2 (11/04/24)
  - Added the following line of code to deal with non-numeric values in the 'streams' column of row 574.
    ```javascript
    cleaned_dataset.loc[574, 'streams'] = 0
    ```
  - Uploaded the updated Data_Cleaning notebook and updated cleaned spreadsheet.
