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

#print(df.iloc[1])       #print specific rows, also works with [1:3] etc

print(df.iloc[2,1])         #prints the one with index 2 with the info on row 1 = the name (Venusaur)


#for index, row in df.iterrows():
    #print(index, row["Name"])               #only "row" would print out all the info in every row, but now we only print out the Name info

#print(df.loc[df['Type 1'] == "Fire"])      #Prints out the firetypes

#print(df.sort_values('Name'))           #prints out in alphabetical order

#print(df.sort_values('Name', ascending=False)) #prints out in alphabetical order, but in descending order

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df.head(9))