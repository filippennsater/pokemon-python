import pandas as pd

#df = pd.read_csv('pokemon_data.csv')


#df_xlsx = pd.read_excel('pokemon_data.xlsx')

#print(df.head(3))

#print(df_xlsx.head(3))

df = pd.read_csv('pokemon_data.txt', delimiter='\t') #when the information is separated by a tab in the txt file we specify the delimiter with just that.

#print(df.head(3))

#print(df.columns)



#print(df['Name'].head(5))
                            #same
#print(df['Name'][0:5])



#print(df[['Name', 'Type 1', 'HP']].head(5))  #choose certain columns

print(df.iloc[1])       #print specific rows, also works with [1:3] etc