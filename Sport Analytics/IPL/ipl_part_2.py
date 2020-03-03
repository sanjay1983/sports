import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv(r"ball_by_ball_details.csv")


'''
for i in range(len(df)):
    df['bowling_team']=''

for i in range(len(df)):
    if df['batting_team'].values[i]==df['teams'].values[i][0]:
        df['bowling_team'].values[i]=df['teams'].values[i][1]
    if df['batting_team'].values[i]==df['teams'].values[i][1]:
        df['bowling_team'].values[i]=df['teams'].values[i][0]
df.to_csv("balls_2.csv")
df=pd.read_csv(r"balls_2.csv")
'''

dff=df.groupby(['over','batsman'])['batsman_runs'].sum().reset_index(name='total')
dff2=df.groupby(['over','batsman'])['batsman_runs'].count().reset_index(name='count')

#dff3=df.groupby(['over','batsman'])


#dff=df.groupby(['over','bowler','bowling_team'])['total'].sum().reset_index(name='total')
#dff2=df.groupby(['over','bowler','bowling_team'])['total'].count().reset_index(name='count')

dff['count']=dff2['count']
dff['SR']=(dff['total']/dff['count'])*100
#dff3['count']=dff2['count']
#dff3['SR']=(dff['total']/dff['count'])*100

#dff=df.groupby(['over','bowler'])['batsman_runs'].apply(lambda x: (x==6).sum()).sort_values(ascending=False).reset_index(name='count')
dff=dff.sort_values(['batsman','over'])
#bm=['AB de Villiers','V Kohli','AJ Finch','PA Patel','CH Morris']

#dff=dff[(dff['batsman'] == 'AB de Villiers') | (dff['batsman'] == 'V Kohli') | (dff['batsman'] == 'AJ Finch') | (dff['batsman'] == 'PA Patel') | (dff['batsman'] == 'CH Morris')]
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(dff)
    #print(dff2)
df=df[df['batsman']=='CH Gayle']
df=df[df['season']==2019]
x=[i for i in range(1,len(df)+1)]
img = plt.imread("111051.png")
fig, ax = plt.subplots()
ax.imshow(img)
ax=sns.scatterplot(x=x,y='batsman_runs',data=df)
plt.show()

'''
pal = sns.color_palette("Blues")
x=[i for i in range(1,21)]
y=[]
for i in range(len(bm)):
    dff3=dff[dff['batsman']==bm[i]]

    y.append((dff3['SR']))
for i in range(len(y)):
    y[i] = np.array(y[i], dtype=float)
    x=np.array(x,dtype=float)
print()
print()

plt.stackplot(x,y, labels=bm, colors=pal, alpha=0.4)
plt.legend(loc='upper right')
plt.xticks([i for i in range(1,21)])
plt.show()
'''

