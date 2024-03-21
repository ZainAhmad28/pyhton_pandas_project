#dictionary in pandas using python

import pandas as pd
val = {"1stinings": 200 , "2ndinings": 300 , "3rdinings": 400}
results = pd.Series(val)
print(results)

#series with only data of 1st , 2nd inings
import pandas as pd
val = {"1stinings": 200 , "2ndinings": 300 , "3rdinings": 400}
results = pd.Series(val, index=["1stinings","2ndinings"])
print(results)

#data frame:data sets in pandas are usually multi-dimenstionals tables , called data frame.
#series are columns but data frame is whole table.

import pandas as pd
val= {"speed":[20,30,40],"ac":[50,60,70]}
result=pd.DataFrame(val)
print(result)

#basically dataframe is a 2D st. like 2D array with table including rows and columns.

import pandas as pd
data = {"items":[1,2,3],"price":[20,30,40]}
output=pd.DataFrame(data)
print(output)

#locate rows : pandas use loc attribute to sepicify a row

import pandas as pd
data = {"items":[1,2,3],"price":[20,30,40]}
output=pd.DataFrame(data)
print(output.loc[1])

#for 2 rows in series
import pandas as pd
data = {"items":[1,2,3],"price":[20,30,40]}
output=pd.DataFrame(data)
print(output.loc[[0,1]])

#we can also name our own index
import pandas as pd
data = {"items":[1,2,3],"price":[20,30,40]}
output=pd.DataFrame(data, index=["day1","day2","day3"])
print(output)

