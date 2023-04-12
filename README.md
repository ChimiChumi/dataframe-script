
## Description
This script can be used to make an accounting task easier and quicker, instead of struggling with Excel.
- it uses the 'pandas' dataframe library to access useful commands
- the input needs two excel tables named: `1.xlsx` and `2.xls` *(.xls or .xlsx, indifferent)*
- after running the app, it generates two files: 
	-	`final.xlsx`: contains the results after merging the required data based on a unique id. It ignores all the additional, not mutual id-s. Those are saved to the other output
	-	`extra.xlsx`: contains all the values which don't appear in the first table (1.xlsx)

In my example, the accounting task was to fetch all the required data from both tables for the current employees. The inactive employees (not present in the first table) should be ignored.

Although the task could be done in Excel too, it's more convenient to run this in Google Colaboratory. After drag and dropping the input tables, it generates the ready-to-go files instantly, making it easy to download and pass to the recipient.
