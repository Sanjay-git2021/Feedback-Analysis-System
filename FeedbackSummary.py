#databse and matplotlib
import pandas as pd
import sqlite3
#import matplotlib.pyplot as plt
import seaborn as sns
con = sqlite3.connect('feedback.db')
df = pd.read_sql_query("SELECT * FROM FEED WHERE STAFFNAME='staff1' ",con)
print(df.head(13))
#plt.bar(df['VOTE'],50)
print(sns.countplot(x="Q1",data=df))
print()
print(sns.countplot(x="Q2",data=df))
print()
print(sns.countplot(x="Q3",data=df))
con.close()
