
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
#style.available



df = pd.read_csv(r"C:/Users/Sanjay/Desktop/Sports/ball_data_1.csv")
'''
for i in range(len(df)):
    df['Total runs']=0
for i in range(len(df)):
    if df['Result'].values[i]!=10 and df['Result'].values[i]!=50:
        df['Total runs'].values[i]=df['Result'].values[i]+df['Wides'].values[i]+df['No-balls'].values[i]+df['Byes'].values[i]+df['Leg-byes'].values[i]
    else:
        df['Total runs'].values[i]=df['Wides'].values[i]+df['No-balls'].values[i]+df['Byes'].values[i]+df['Leg-byes'].values[i]

df.to_csv("ball_data_1.csv")
'''


df1 = df.groupby(["Bowler Team","Year"]).size().reset_index(name='counts')
dff = df.groupby(["Bowler Team","Year"])['Total runs'].sum().reset_index()
dff['counts']=df1['counts']
dff['RPO']=dff['Total runs']*6/dff['counts']
print(dff)

indexnames=dff[dff['Bowler Team'] == 'PWI'].index
dff.drop(indexnames, inplace=True)
indexnames=dff[dff['Bowler Team'] == 'KTK'].index
dff.drop(indexnames, inplace=True)
indexnames=dff[dff['Bowler Team'] == 'DCG'].index
dff.drop(indexnames, inplace=True)
indexnames=dff[dff['Bowler Team'] == 'GL'].index
dff.drop(indexnames, inplace=True)
indexnames=dff[dff['Bowler Team'] == 'RPS'].index
dff.drop(indexnames, inplace=True)

print(dff)
dfff = pd.pivot_table(data=dff, index='Bowler Team',values='RPO', columns='Year')
#print(dfff)
#dfff.fillna(0)
#matplotlib.rcParams['font.family']="serif"

#sns.set_context("talk")
#ax = sns.heatmap(dfff,cmap='Reds',cbar_kws={'label':'Economy Rate in Powerplay'},linewidths=1, linecolor='black')
#hfont = {'fontname':'Helvetica'}
#plt.title('Powerplay Analysis',**hfont)
#plt.title('YR',**hfont)
#plt.savefig("Teams_heatmap.png")
#plt.show()

boundary_percentage=[14.869281045751634, 19.825708061002178, 16.199756394640684, 20.5982905982906, 21.21212121212121, 16.38316920322292, 18.898240244835502, 25.096525096525095, 21.40921409214092, 19.762258543833582, 23.582089552238806, 19.322033898305083, 18.845500848896435, 15.090543259557345, 27.45098039215686, 17.6875, 22.12566844919786, 21.02728731942215, 33.23863636363637, 15.815485996705107, 20.193861066235865, 15.445719329214475, 20.293398533007334, 17.5177304964539, 20.17126546146527, 19.08006814310051, 17.142857142857142, 19.83640081799591, 17.55952380952381, 17.916666666666668, 22.281167108753316, 16.46706586826347, 14.139344262295081, 18.06282722513089, 17.414721723518852, 16.611295681063122, 18.432510885341074, 15.296052631578947, 19.82248520710059, 17.767653758542142]
dot_percentage=[51.1437908496732, 49.34640522875817, 56.02923264311815, 47.863247863247864, 49.24242424242424, 44.40465532676813, 45.447589900535576, 48.262548262548265, 46.68021680216802, 47.69687964338782, 48.35820895522388, 48.47457627118644, 45.04810413129598, 52.313883299798796, 46.3235294117647, 46.625, 55.213903743315505, 46.54895666131621, 47.15909090909091, 49.42339373970346, 46.52665589660743, 52.162400706090025, 50.36674816625917, 46.666666666666664, 52.14081826831589, 53.4923339011925, 49.89010989010989, 53.88548057259714, 52.083333333333336, 53.333333333333336, 48.93899204244032, 58.383233532934135, 53.278688524590166, 54.973821989528794, 53.3213644524237, 57.142857142857146, 55.87808417997097, 51.48026315789474, 49.112426035502956, 52.16400911161731]
batsmen_final=['Rayudu', 'Raina', 'Watson', 'Parthiv Patel', 'de Villiers', 'Kohli', 'Uthappa', 'Chris Lynn', 'Warner', 'de Kock', 'Suryakumar Yadav', 'Rohit', 'Dhawan', 'Shreyas Iyer', 'Buttler', 'Rahane', 'Gayle', 'Rahul', 'Narine', 'Samson', 'du Plessis', 'Vijay', 'Nair', 'Gambhir', 'Brendon McCullum', 'Finch', 'Vohra', 'Dwayne Smith', 'Shaun Marsh', 'Simmons', 'Sehwag', 'Bisla', 'Kallis', 'Mahela Jayawardene', 'Tendulkar', 'Dilshan', 'Dravid', 'Michael Hussey', 'Mandeep Singh', 'Gilchrist']

bowlers_final=['Chahal', 'Harbhajan', 'Chahar', 'Sandeep Sharma', 'Bhuvneshwar', 'Narine', 'Ishant', 'Boult', 'Bumrah', 'McClenaghan', 'Shami', 'D Kulkarni', 'SN Thakur', 'A Russell', 'Ashwin', 'Malinga', 'U Yadav', 'Mohit Sharma', 'Southee', 'Unadkat', 'Steyn', 'Aaron', 'Watson', 'Vinay Kumar', 'Johnson', 'Nehra', 'Aravind', 'Dinda', 'P Kumar', 'Zaheer', 'Munaf Patel', 'Coulter-Nile', 'Faulkner', 'Irfan Pathan', 'RP Singh', 'Balaji', 'Praveen Kumar', 'Morne Morkel', 'Albie Morkel']
wickets_taken=[13, 26, 26, 44, 45, 24, 31, 9, 12, 31, 7, 29, 10, 15, 27, 28, 36, 34, 10, 18, 27, 13, 14, 15, 9, 23, 20, 21, 12, 36, 19, 12, 13, 6, 16, 11, 17, 36, 13]
dots_bowled=[146, 318, 316, 564, 843, 371, 450, 209, 295, 345, 217, 354, 144, 144, 320, 488, 401, 377, 244, 226, 466, 176, 207, 176, 195, 352, 209, 260, 251, 519, 211, 171, 168, 181, 260, 210, 410, 515, 214]
bowl_sr=[24.846153846153847, 24.26923076923077, 22.53846153846154, 23.977272727272727, 31.755555555555556, 29.083333333333332, 26.870967741935484, 44.333333333333336, 47.75, 22.06451612903226, 66.85714285714286, 24.344827586206897, 30.1, 20.266666666666666, 25.333333333333332, 31.714285714285715, 21.055555555555557, 23.5, 50.4, 27.166666666666668, 29.185185185185187, 26.153846153846153, 29.428571428571427, 23.4, 45.333333333333336, 31.26086956521739, 22.1, 23.523809523809526, 38.0, 26.72222222222222, 19.473684210526315, 25.25, 27.23076923076923, 51.0, 29.3125, 33.72727272727273, 41.94117647058823, 25.1388888889, 34.23076923076923]
dot_percentage_bowled=[45.20123839009288, 50.396196513470684, 53.924914675767916, 53.459715639810426, 58.992302309307206, 53.15186246418338, 54.021608643457384, 52.38095238095238, 51.48342059336824, 50.43859649122807, 46.36752136752137, 50.141643059490086, 47.840531561461795, 47.36842105263158, 46.78362573099415, 54.95495495495496, 52.9023746701847, 47.18397997496871, 48.41269841269841, 46.21676891615542, 59.13705583756345, 51.76470588235294, 50.24271844660194, 50.142450142450144, 47.794117647058826, 48.95688456189151, 47.28506787330317, 52.63157894736842, 55.04385964912281, 53.95010395010395, 57.027027027027025, 56.43564356435643, 47.45762711864407, 59.150326797385624, 55.437100213219615, 56.60377358490566, 57.50350631136045, 56.906077348, 48.08988764044944]



sns.set_context("paper")
sns.set_style("dark")
clrs2=['red']
#ax = plt.scatter(boundary_percentage,dot_percentage,s=30,c="red")
ax = sns.scatterplot(dot_percentage_bowled,bowl_sr,palette=clrs2,s=70)
plt.xlabel('Dot percentage bowled')
plt.ylabel('Bowling Strike-Rate')
#plt.savefig("dot_bound.png")
for i, txt in enumerate(bowlers_final):
    ax.annotate(txt, (dot_percentage_bowled[i], bowl_sr[i]),size=7,ha="right",textcoords="offset points",xytext=(5,5))
#plt.savefig("dot_bound_2.png")
plt.show()

