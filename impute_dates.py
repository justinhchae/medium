import pandas as pd


col1 = 'event_date'
col_new = str(col1 + '_new')
col2 = 'received_date'
curr_year = 2020
past_year = 2010

# given a dataframe df with col1 and col2 as datetime columns
# store the lambda function as an object
impute = lambda x: \
                x[col1].replace(year=x[col2].year) \
                    if x[col1].year > curr_year \
                    else x[col1].replace(year=x[col2].year) \
                    if x[col1].year < past_year \
                    else x[col1]

# apply the lambda function
df[col_new] = df.apply(impute, axis=1)