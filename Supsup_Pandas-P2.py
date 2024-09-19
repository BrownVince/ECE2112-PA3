
import pandas as pd
cars.iloc[:5, ::2] #using .iloc[rows, columns] function, set the ending index for rows as 5 to select the first 5 rows(index 0-4)
                    #as for the columns set the increment to 2 in order to select every 2nd column starting from column 1
cars.loc[(cars['Model']=='Mazda RX4')] #using the .loc[] function, find the row that has Mazda RX4 as the car model then print the entire row
cars.loc[(cars['Model']=='Camaro Z28'), ['Model', 'cyl']] #using again the .loc[] function, find the Camaro Z28 car model then print only cyl
cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
#using the .loc[] function, find the given 3 car models separated by the '|' (element-wise OR) function then print only columns Model, cyl, and gear
