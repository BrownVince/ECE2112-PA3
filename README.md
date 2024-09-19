<div align="center">

# Hi! <img src="https://github.com/user-attachments/assets/d21e6cd6-76a9-4934-8910-809aa4815251" alt="Wave" width="30"/>, I'm Vince Joriz E. Supsup  
From 2ECE-D, and this is my Programming Assignment #3 in ECE2112  
Submitted: Sept. 18, 2024 

</div>

# Version History
V1.0 (09-17-24) - Initial Release  
V1.1 (09-18-24) -  Finalization: Added Comments in the Notebook and Added Documentation in the Readme File 
V2.0 (09-19-24) - Edited the uploaded files in github  
V3.0 (09-19-24) - Submission of Github Link

# Software(s) Used
<img src="https://github.com/user-attachments/assets/32ea11b3-b4e5-4efa-a673-ce2b102ab4b5" alt="Jupyter Logo" width="80"/> <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="100"/>

# PROBLEM 1
### In problem #1, we are tasked to load the cars.csv file then print the first and last 5 rows
* In this problem, I only encountered little issues since I just loaded the file and saved it to the variable 'cars'
```
cars = pd.read_csv('cars.csv')
```
* I then loaded the first and last five rows using the .head() and .tail() function respectively.
```
cars.head()
cars.tail()
```
* When saving the problem 1 as a .py file, I used the write function to write the specific codes into the Supsup_Pandas-P1.py file as a whole string
```
prob1 = """
import pandas as pd #Call the pandas Library and import as pd for convention
cars = pd.read_csv('cars.csv') #Load the file cars.csv and save it to variable 'cars'
cars.head() #Load the first 5 Rows
cars.tail() #Load the last 5 rows
"""

p1 = open('SUPSUP_Pandas-P1.py', 'w')
p1.write(prob1)
p1.close()
```
And when I thought I wouldn't encounter any problems, here comes problem #2 where I encountered many minor issues  


# PROBLEM 2
### In this problem, we are tasked to extract the following information using subsetting, slicing and indexing operations using the dataframe cars in problem 1
* At part a, I first tried the .loc[] function and typed all the odd numbered columns manually, but I thought there must be a better way to get the same output without manually typing all the names of the odd numbered columns. That's when I used the .iloc[] function and set the increment value to 2 in the column in order to print every 2nd column starting from one, hence printing all the odd numbered columns.
```
#Before
cars.loc[:4,['Model',	'cyl',	'hp',	'wt',	'vs',	'gear']]

#After
cars.iloc[:5, ::2]
```
* For part b, using the .loc[] function, I displayed the entire row that contains the ‘Model’ of ‘Mazda RX4’
```
cars.loc[(cars['Model']=='Mazda RX4')]
```
* Furthermore, for part c, I also used the .loc[] function to display how many cylinders does the model 'Camaro Z28' have by restricting the displayed column to display only the 'cyl' column
```
cars.loc[(cars['Model']=='Camaro Z28'), ['Model', 'cyl']]
```
* Lastly, for part d, I encountered a major issue. At first I tried the Logical OR operation (or), but it resulted to an error. So I searched it up, then I found out that 'or' is only used for combining simple boolean expressions and it also operates on single boolean values such as x=true or y=false. Meanwhile, I also found out that Bitwise OR operation (|), works best for numpy and pandas since it is used for element-wise operations in arrays, series, or dataframes and is best used in data manipulation such as data filtering. Since the problem has multiple conditions, I tried using '|'(Bitwise OR) function and it worked like a charm.
```
#Before
cars.loc[(cars['Model']=='Mazda RX4 Wag') or (cars['Model']=='Ford Pantera L') or (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
#This syntax results to an error :(

#After
cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
#This syntax is all goods :)
```
* When saving the problem 2 again as a .py file, I used the write function to write the specific codes into the Supsup_Pandas-P2.py file as a whole string
```
prob2 = """
import pandas as pd
cars.iloc[:5, ::2] #using .iloc[rows, columns] function, set the ending index for rows as 5 to select the first 5 rows(index 0-4)
                    #as for the columns set the increment to 2 in order to select every 2nd column starting from column 1
cars.loc[(cars['Model']=='Mazda RX4')] #using the .loc[] function, find the row that has Mazda RX4 as the car model then print the entire row
cars.loc[(cars['Model']=='Camaro Z28'), ['Model', 'cyl']] #using again the .loc[] function, find the Camaro Z28 car model then print only cyl
cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
#using the .loc[] function, find the given 3 car models separated by the '|' (element-wise OR) function then print only columns Model, cyl, and gear
"""
p2 = open('SUPSUP_Pandas-P2.py', 'w')
p2.write(prob2)
p2.close()
```

