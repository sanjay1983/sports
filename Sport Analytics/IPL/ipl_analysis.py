import pandas as pd

df=pd.read_csv("C:/Users/sanjay/Desktop/Sports/ball_data_1.csv")
for i in range(len(df)):
    df['Out except Run-Out']=0
    df['Run-out']=0
for i in range(len(df)):
    if df['Result'].values[i]==10:
        df['Result'].values[i] = 0
        df['Out except Run-Out'].values[i] = 1
    if df['Result'].values[i]==50:
        df['Result'].values[i] = 0
        df['Run-out'].values[i] = 1
dff = df.groupby('Batsman')['Result'].sum().reset_index(name ='Total Runs')
dff2 = df.groupby('Batsman')['Result'].count().reset_index(name='Total balls faced')
dff['Total Balls Faced'] = dff2['Total balls faced']


for i in range(len(dff)):
    dff['SR']=0.0
for i in range(len(dff)):
    dff['SR'].values[i]=100*dff['Total Runs'].values[i]/dff['Total Balls Faced'].values[i]
dff = dff.sort_values(by='SR', ascending=False)

dff = dff.drop(dff[dff['Total Balls Faced'] < 150].index)
avg_sr=dff['SR'].mean()
for i in range(len(dff)):
    dff['SR_diff']=0.0
for i in range(len(dff)):
    dff['SR_diff'].values[i] = dff['SR'].values[i]-avg_sr

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(dff)

dff.to_csv("batsmen_summary.csv")


#-------------------------------------------------


b_dff = df.groupby('Bowler')['Total runs'].sum().reset_index(name ='Total Runs Conceded')
b_dff2 = df.groupby('Bowler')['Total runs'].count().reset_index(name='Total balls bowled')
b_dff['Total Balls Bowled'] = b_dff2['Total balls bowled']
b_dff3 = df[df['Out except Run-Out'] == 1]
b_dff_w = b_dff3.groupby('Bowler')['Out except Run-Out'].count().reset_index(name='Total wt')
#b_dff3 = df.groupby('Bowler')
#b_dff3.apply(lambda x: x[x['Out except Run-Out'] == 1]['Out except Run-Out'].sum()).reset_index(name='Total wickets taken')
#b_dff3 = df.groupby('Bowler')['Out except Run-Out'].count().reset_index(name='Total wickets taken')
l=[0 for i in range(len(b_dff))]
#l=b_dff3.apply(lambda x: x[x['Out except Run-Out'] == 1]['Out except Run-Out'].count()).to_list()
b_dff['Total Wickets Taken']=l
#b_dff['Total Wickets Taken'] = b_dff3['Total wickets taken']

for i in range(len(b_dff)):
    for j in range(len(b_dff_w)):
        if b_dff['Bowler'].values[i] == b_dff_w['Bowler'].values[j]:
            b_dff['Total Wickets Taken'].values[i] = b_dff_w['Total wt'].values[j]
            break

b_dff = b_dff[b_dff['Total Wickets Taken'] > 0]

for i in range(len(b_dff)):
    b_dff['SR']=0.0
for i in range(len(b_dff)):
    b_dff['SR'].values[i]=b_dff['Total Balls Bowled'].values[i]/b_dff['Total Wickets Taken'].values[i]

for i in range(len(b_dff)):
    b_dff['ER']=0.0
for i in range(len(b_dff)):
    b_dff['ER'].values[i]=6*b_dff['Total Runs Conceded'].values[i]/b_dff['Total Balls Bowled'].values[i]
b_dff = b_dff.sort_values(by='ER', ascending=False)

b_dff = b_dff.drop(b_dff[b_dff['Total Balls Bowled'] < 150].index)
avg_er=b_dff['ER'].mean()
for i in range(len(b_dff)):
    b_dff['ER_diff']=0.0
for i in range(len(b_dff)):
    b_dff['ER_diff'].values[i] = b_dff['ER'].values[i]-avg_er

avg_sr_b=b_dff['SR'].mean()
for i in range(len(b_dff)):
    b_dff['SR_diff']=0.0
for i in range(len(b_dff)):
    b_dff['SR_diff'].values[i] = b_dff['SR'].values[i]-avg_sr_b



with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(b_dff)

b_dff.to_csv("bowlers_summary.csv")



#'-----------------------'


df = pd.read_csv("C:/Users/sanjay/Desktop/Sports/batsmen_summary_final.csv")
db = pd.read_csv("C:/Users/sanjay/Desktop/Sports/bowlers_summary_final.csv")
dff = df.groupby('Team')['SR_diff'].mean().reset_index(name ='Batting_index')

dff2 = db.groupby('Team')['ER_diff'].mean().reset_index(name ='Team_ER_diff_avg')
dff3 = db.groupby('Team')['SR_diff'].mean().reset_index(name ='Team_SR_diff_avg_b')
dff['Bowling_index'] = dff3['Team_SR_diff_avg_b'] + dff2['Team_ER_diff_avg']
dff['Team_index'] = dff['Batting_index'] - dff['Bowling_index']
dff.sort_values(by='Team_index',ascending=False)

dff = dff[dff['Team']!='NP']
import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure()

plt.style.use('dark_background')
fig.set_facecolor("black")
ax = sns.barplot(x='Batting_index',y='Team',data=dff,linewidth=2.5,errcolor=".2",edgecolor=".2",palette=['yellow','royalblue','mediumpurple','tomato','blue','red','hotpink','darkorange'])
plt.show()







