import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/sanjay/Desktop/Sports/england.csv")
for i in range(len(df)):
    df['Balls per Boundary']=0.0
    df['Non-boundary RPO']=0.0

for i in range(len(df)):
    df['Balls per Boundary'].values[i]=df['BF'].values[i]/(df['4s'].values[i]+df['6s'].values[i])
    df['Non-boundary RPO'].values[i]=(df['Runs'].values[i]-4*df['4s'].values[i]-6*df['6s'].values[i])*6/(df['BF'].values[i]-df['4s'].values[i]-df['6s'].values[i])
df.to_csv("england_1.csv")
plt.style.use('dark_background')
df=pd.read_csv("C:/Users/sanjay/Desktop/Sports/england_1.csv")
#ax=sns.barplot(y='Player',x='Balls per Boundary',data=df)

df.sort_values(by='Player',ascending=False).plot.barh(x="Player", y=['Balls per Boundary','Non-boundary RPO'],linewidth=1.5,edgecolor=".2",color=['cornflowerblue','slategray'])
plt.show()