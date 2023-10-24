#Import the Pandas framework, defined as pd
import pandas as pd
 
#Define our color variable as a list
color = ['blue','green','red','yellow']
#Define our fruit variable as a list
fruit = ['blueberry','apple','cherry','banana']
 
#Define the df variable as formatted columns for color and fruit
df=pd.DataFrame(columns=['color', 'fruit'])
#Label our columns as color and fruit
df['color'],df['fruit']=color,fruit
 
#Print everything
#print(df)

n_tuple = ("kubernetes", "cloud native", [8, 6, 7, 5, 3, 0, 9])

print(n_tuple[0][3])



