'''
selection
'''
#select the first row
df.loc[0,:]

#select the rows with column 'column_value' > 5
df.loc[ df['column_value'] >5]

#select the rows based on multiple conditions
df.loc[ (df['column_value1'] >5) & ( df['column_value2'] <10 ) ]

#select the column
df['column_name']

#select the columns
df[ ['column1','column2']]


'''
unique
''' 
#list unique value in a column 
df.column_name.unique()

#count unique values in a column
df.column_name.unique().shape

'''
replace value based on condition
'''
df.loc[df['gender']=='male', 'salary'] = 10000
