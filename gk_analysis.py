import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')
df=pd.read_csv("goalkeepers.csv",encoding="ISO-8859-1")
df=df[df['90s']>10]
ax=sns.barplot(x='AvgLen_2',y='Player',data=df,linewidth=2.5
                 , edgecolor=".2",color='cornflowerblue')
plt.show()


x = df['Stp%'].tolist()
y = df['GA'].tolist()
n=df['Player'].tolist()
plt.xlabel("% of crosses into Penalty Area successfully stopped by keeper")
plt.ylabel("Goals Conceded")
#fig, ax = plt.subplots()
ax=sns.scatterplot(x,y,color='r')

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))


plt.show()