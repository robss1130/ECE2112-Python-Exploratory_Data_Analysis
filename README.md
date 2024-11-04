# ECE2112-Python-Exploratory_Data_Analysis 📊📈🗂️🗃️🐍



## Write-up & Insights Gained 🔍
- When using data files in coding using python, I learned that not all files and encoding methods are compatible which leads to errors when reading files. Upon researching about it, it's because some data uses special characters that may cause issue to the programming language. An example is Python's Pandas lilbrary defaults to UTF-8 encoding, but the spreadsheet file that were using seems to not be compatible therefore I have to use an encoding compatible and chose 'cp1252' which made my code run as long as the data I'll be loading does not contain characters outside the Western European character set.

- Upon performing data cleaning, one of the issue that I stumbled upon is creating a line of code that would easily check entries of the data set at which it has a missing value. Prior to this, as I initially performed the activity with unaltered version of the spreadsheet containing some garbage values, I was able to see that 2 columns of the spreadsheet seems to contain missing values. I begun started with the 'in_shazam_carts' column and had no idea how identify missing values. Upon surfing the internet, I came to learn about the `.isna()` code which when used, basically checks for "NaN" values. Checking for "NaN" would be the logical thing to do since the column is specifically catered to numerical values. Hence: `dataset[dataset['in_shazam_charts'].isna()==1]`

- For the songs with duplicates, songs with the same track name and artist name, were simply dropped as they basically just cause issue on the data. Although, I kept the first occurence of the song as upon checking the numbers, it seems that the later occurence were just the outdated data of that songs performance. This was done using `.duplicated(subset=['track_name', 'artist(s)_name'], keep=False)]` where `.duplicated()` basically checks and returns a value of True when a row is duplicated and False if it is unique. `subset=['track_name', 'artist(s)_name']` is basically a parameter to specify which columns to look for duplicate. Lastly, `keep=False` is used in order to mark the first instance of a song with duplicate at later instances to be True, as without it, the compiler seems to instruct to mark songs as a duplicate once it had a first encounter but never include it as a 'duplicate'.
- `.drop_duplicates(subset=['track_name', 'artist(s)_name'], keep='first')` is used to finally drop the duplicates. `.drop_duplicates` will basically drop those songs that contain the same track name and artist name and to keep the first occurence where `keep='first'` comes into play.

- Prior to this line, it was stated that one of the actions I did in dealing with some unusable values in the spreadsheet was replacing it with a '0'. Moving to the 'key' column, it also contained some missing values. As some songs were missing some keys, I decided to just fill it up with "N/A" or "not applicable" so I ran this:
    ```javascript
    dataset['key'] = dataset['key'].fillna('N/A')
    ```
- Apparently, filling the entries with 'N/A' still resulted in the data containing once loaded from a different notebook but different output was printed once I changed it to '"N/A"'. Upon searching the web, 'N/A' and '"N/A"' should both be treated a non null value despite the other being a string value as 'NaN' is distinct from 'N/A'. What seems to be causing this issue is still unknown but is assumed to be due to the version of the spreadsheet file. ❗Note: This line is to be updated once a strong, credible, and appropriate/related information is stumbled upon.

- While trying to create and generate some graphs, I stumble an issue where it cannot be fixed. The only way I was able to fix it is by restarting my computer. According to some articles, this may be due to an issue in some of the states of the variable I've initialized. Sometimes, variables are not being reset properly or if previous computations have affected the current state, which can lead to NaN issues. By restarting the PC, the Python reloads all the libraries. It may also be due to the system resources becoming more strained. Hence, restarting the machine fixes the issue.


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

***Encountering non-numeric values***🤔💭
* Aside from missing values and duplicates, seems like I've skipped over some rows that contains non-numeric values on a column that is meant to only contain numerical values causing problems later on the coding. This issue causes ineffecient use of time, being forced to deal with setting up the spreadsheet once again.
* e.g.: ![image](https://github.com/user-attachments/assets/419da2ca-2665-4087-8833-22b15d682319)
  - Solution 🔧: Keeping the data cleaning notebook for quick fixes.

***Null values*** ¯\_(ツ)_/¯
* Upon filling the empty entries of 'key' column with 'N/A' whilst using the Data_Cleaning.ipynb notebook and running a `.isnull()` code to check if there are still null values, I was greeted with a display of false. But once after the spreadsheet was saved and loaded into the main notebook, the 'key' column tested positive for containing null values.
![image](https://github.com/user-attachments/assets/0f96fbe1-6ae2-4504-aae9-67ef558f7399)
  - Solution 🔧: filled the missing entries with '"N/A"' instead. Using string value seems to fix the issue.

***Random Error*** 💀
```javascript
C:\Users\PC\anaconda3\Lib\site-packages\seaborn\matrix.py:202: RuntimeWarning: All-NaN slice encountered
  vmin = np.nanmin(calc_data)
C:\Users\PC\anaconda3\Lib\site-packages\seaborn\matrix.py:207: RuntimeWarning: All-NaN slice encountered
  vmax = np.nanmax(calc_data)
```
* While creating a heatmap for to solve the problem dealing with correlation, I ran to the problem aboved. Despite trying to change the code multiple times, seems like the issue doesn't go away. And upon searching the internet, no solution was given to me.
  - Solution 🔧: Restart the PC.



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
  - Updated the main notebook by adding some graph to show mean, median, and standard deviation of the 'streams'.
  - Added the following line of code to deal with non-numeric values in the 'streams' column of row 574.
    ```javascript
    cleaned_dataset.loc[574, 'streams'] = 0
    ```
  - Uploaded the updated Data_Cleaning notebook and updated cleaned spreadsheet.
 
* Version 3.0 (11/05/24)
  - Major addition of codes.
  - Newly generated graphs were added to answer and present some questions of the guide question.
  - Simplified some codes to remove redundancy.
 
  ## References 🔗
  - Rubin, D. B. (1976). Inference and missing data. Biometrika, 63(3), 581-592. https://doi.org/10.1093/biomet/63.3.581
