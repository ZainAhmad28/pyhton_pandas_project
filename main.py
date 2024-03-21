import pandas as pd
val = [9,9,0]
new  = pd.Series(val)
print (new)

 # here we have pandas series with indexing.
 # labeling = label can be used to access a specified value .

import pandas as pd
val = [9,9,0]
new  = pd.Series(val)
print (new[2])

#indexing
import pandas as pd
val = [9,9,0]
new = pd.Series(val, ["x", "y", "z"])
print(new)