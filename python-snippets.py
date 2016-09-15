# write or append dataframe to csv file
# adapted from here http://stackoverflow.com/questions/30991541/pandas-write-csv-append-vs-write

import os
if not os.path.isfile('filename.csv'):
        df.to_csv('filename.csv', header=True, encoding='utf-8')
    else:  
        # else the file exists so ignore the header
        df.to_csv('filename.csv', mode='a', header=False, encoding='utf-8')

# save dataframe in a pickle that's compatible with python 2
pickle.dump(df , open( "dataframe_pickle.p", "wb" ) , protocol = 2)
df = pickle.load( open( "dataframe_pickle.p", "rb" ))

# make a deep copy
import copy
new_var = copy.deepcopy(old_var)
# OR
new_var = old_var.copy(deep=True)

# strip column headings before punctuation (this method will only strip first instance)
# from table_name-column_name -> column_name
# use [0] to select first part, and [1] for the '-', not that you would ever want that..
my_dataframe.columns = [i.rpartition('-')[2] for i in my_dataframe.columns.values]
