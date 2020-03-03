import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('data.csv')
#print(df.head())
#print(df.columns)


def func(x, delt, rd, v, a, tau):
    fx = ((math.exp(x)*((delt*delt)-(rd*rd)-v-math.exp(x)))/(2*((rd*rd)+v+math.exp(x))*((rd*rd)+v+math.exp(x)))) - ((x-a)/(tau*tau))
    return fx


for i in range(0, len(df)):
    df['Team 1 Rating'] = 1500
    df['Team 2 Rating'] = 1500

for i in range(0, len(df)):
    df['Team 1 Result'] = 99
    df['Team 2 Result'] = 99

dict_teams = {0: 'Royal Challengers Bangalore', 1: 'Kolkata Knight Riders', 2: 'Kings XI Punjab', 3: 'Chennai Super Kings', 4: 'Delhi Capitals/Delhi Daredevils', 5: 'Rajasthan Royals', 6: 'Sunrisers Hyderabad/Deccan Chargers', 7: 'Mumbai Indians', 8: 'Kochi Tuskers Kerala', 9: 'Pune Warriors India', 10: 'Rising Pune Supergiant(s)', 11: 'Gujarat Lions'}
no_of_teams = 12
ratings = [1500.0 for i in range(0, no_of_teams)]
rating_deviations = [50.0 for i in range(0, no_of_teams)]
volatility = [0.03 for i in range(0, no_of_teams)]
v = [0.0 for i in range(0, no_of_teams)]
delta = [0.0 for i in range(0, no_of_teams)]
tau = 0.2
team1_index = 0
team2_index = 0

for i in range(0, len(df)):
    if df['Team 1'].values[i] == df['Winner'].values[i]:
        df['Team 1 Result'].values[i] = 2
        df['Team 2 Result'].values[i] = 0
    elif df['Team 2'].values[i] == df['Winner'].values[i]:
        df['Team 1 Result'].values[i] = 0
        df['Team 2 Result'].values[i] = 2
    else:
        df['Team 1 Result'].values[i] = 1
        df['Team 2 Result'].values[i] = 1

df.to_csv('data1.csv')
df1 = pd.read_csv('data1.csv')

for i in range(0, len(df1)):
    for j in range(0, len(dict_teams)):
        if df1['Team 1'].values[i] == dict_teams[j]:
            ratings[j] = (ratings[j]-1500)/173.7178
            rating_deviations[j] = rating_deviations[j]/173.7178
            team1_index = j
        if df1['Team 2'].values[i] == dict_teams[j]:
            ratings[j] = (ratings[j] - 1500) / 173.7178
            rating_deviations[j] = rating_deviations[j] / 173.7178
            team2_index = j

    #print(ratings[team1_index])
    #print(ratings[team2_index])

    g2 = 1/(math.sqrt(1+(3*rating_deviations[team2_index]*rating_deviations[team2_index])/(math.pi*math.pi)))
    e2 = 1/(1+math.exp(-1*g2*(ratings[team1_index]-ratings[team2_index])))
    v[team1_index] = 1/(g2*g2*e2*(1-e2))
    #print (g2, e2, v[team1_index])

    g1 = 1 / (math.sqrt(1 + (3 * rating_deviations[team1_index] * rating_deviations[team1_index]) / (math.pi * math.pi)))
    e1 = 1 / (1 + math.exp(-1 * g1 * (ratings[team2_index] - ratings[team1_index])))
    v[team2_index] = 1 / (g1 * g1 * e1 * (1 - e1))
    #print (g1, e1, v[team2_index])

    delta[team1_index] = v[team1_index]*g2*(df1['Team 1 Result'].values[i]-e2)
    delta[team2_index] = v[team2_index] * g1 * (df1['Team 2 Result'].values[i] - e1)

    #print (delta[team1_index])
    #print (delta[team2_index])

    a1 = math.log(volatility[team1_index]*volatility[team1_index])
    epsilon = 0.000001
    A1 = a1
    if ((delta[team1_index]*delta[team1_index]) > (rating_deviations[team1_index]*rating_deviations[team1_index] + v[team1_index])):
        B1 = math.log(delta[team1_index]*delta[team1_index] - rating_deviations[team1_index]*rating_deviations[team1_index] - v[team1_index])
    if ((delta[team1_index] * delta[team1_index]) <= (rating_deviations[team1_index] * rating_deviations[team1_index] + v[team1_index])):
        k1 = 1
        while (func(a1 - k1*tau, delta[team1_index], rating_deviations[team1_index], v[team1_index], a1, tau) < 0):
            k1 = k1 + 1
        B1 = a1 - k1 * tau
    fA1 = func(A1, delta[team1_index], rating_deviations[team1_index], v[team1_index], a1, tau)
    fB1 = func(B1, delta[team1_index], rating_deviations[team1_index], v[team1_index], a1, tau)

    while (math.fabs(B1 - A1) > epsilon):
        C1 = A1 + ((A1 - B1)*fA1)/(fB1-fA1)
        fC1 = func(C1, delta[team1_index], rating_deviations[team1_index], v[team1_index], a1, tau)
        if ((fC1 * fB1) < 0):
            A1 = B1
            fA1 = fB1
        else:
            fA1 = fA1/2
        B1 = C1
        fB1 = fC1

    volatility[team1_index] = math.exp(A1/2)

    a2 = math.log(volatility[team2_index] * volatility[team2_index])
    A2 = a2
    if ((delta[team2_index] * delta[team2_index]) > (
            rating_deviations[team2_index] * rating_deviations[team2_index] + v[team2_index])):
        B2 = math.log(
            delta[team2_index] * delta[team2_index] - rating_deviations[team2_index] * rating_deviations[team2_index] -
            v[team2_index])
    if ((delta[team2_index] * delta[team2_index]) <= (
            rating_deviations[team2_index] * rating_deviations[team2_index] + v[team2_index])):
        k2 = 1
        while (func(a2 - k2 * tau, delta[team2_index], rating_deviations[team2_index], v[team2_index], a2, tau) < 0):
            k2 = k2 + 1
        B2 = a2 - k2 * tau
    fA2 = func(A2, delta[team2_index], rating_deviations[team2_index], v[team2_index], a2, tau)
    fB2 = func(B2, delta[team2_index], rating_deviations[team2_index], v[team2_index], a2, tau)

    while (math.fabs(B2 - A2) > epsilon):
        C2 = A2 + ((A2 - B2) * fA2) / (fB2 - fA2)
        fC2 = func(C2, delta[team2_index], rating_deviations[team2_index], v[team2_index], a2, tau)
        if ((fC2 * fB2) < 0):
            A2 = B2
            fA2 = fB2
        else:
            fA2 = fA2 / 2
        B2 = C2
        fB2 = fC2

    volatility[team2_index] = math.exp(A2 / 2)

    pre_rating_value1 = math.sqrt(rating_deviations[team1_index]*rating_deviations[team1_index] + volatility[team1_index]*volatility[team1_index])
    pre_rating_value2 = math.sqrt(rating_deviations[team2_index] * rating_deviations[team2_index] + volatility[team2_index] * volatility[team2_index])
    #print(df['Team 1 Result'].values[i])
    #print(df['Team 2 Result'].values[i])
    rating_deviations[team1_index] = 1/math.sqrt((1/(pre_rating_value1*pre_rating_value1)) + (1/v[team1_index]))
    #print(rating_deviations[team1_index])
    ratings[team1_index] = ratings[team1_index] + rating_deviations[team1_index]*rating_deviations[team1_index]*g2*((df['Team 1 Result'].values[i]-e2))
    #print(ratings[team1_index])
    rating_deviations[team2_index] = 1 / math.sqrt((1 / (pre_rating_value2 * pre_rating_value2)) + (1 / v[team2_index]))
    #print(rating_deviations[team2_index])
    ratings[team2_index] = ratings[team2_index] + rating_deviations[team2_index] * rating_deviations[team2_index] *g1* ((df['Team 2 Result'].values[i] - e1))
    #print(ratings[team2_index])

    ratings[team1_index] = 173.7178 * ratings[team1_index] + 1500
    rating_deviations[team1_index] = 173.7178 * rating_deviations[team1_index]
    ratings[team2_index] = 173.7178 * ratings[team2_index] + 1500
    rating_deviations[team2_index] = 173.7178 * rating_deviations[team2_index]

    df1['Team 1 Rating'].values[i] = ratings[team1_index]
    df1['Team 2 Rating'].values[i] = ratings[team2_index]

    print('Iteration no. ', i+1)
    print(ratings)
    print(rating_deviations)

df1.to_csv('data2.csv')
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
l10=[]
l11=[]
l12=[]
for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Royal Challengers Bangalore':
        l1.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Royal Challengers Bangalore':
        l1.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Delhi Capitals/Delhi Daredevils':
        l2.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Delhi Capitals/Delhi Daredevils':
        l2.append(df1['Team 2 Rating'].values[i])


for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Mumbai Indians':
        l3.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Mumbai Indians':
        l3.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Chennai Super Kings':
        l4.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Chennai Super Kings':
        l4.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Kolkata Knight Riders':
        l5.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Kolkata Knight Riders':
        l5.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Kings XI Punjab':
        l6.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Kings XI Punjab':
        l6.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Rajasthan Royals':
        l7.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Rajasthan Royals':
        l7.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Sunrisers Hyderabad/Deccan Chargers':
        l8.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Sunrisers Hyderabad/Deccan Chargers':
        l8.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Kochi Tuskers Kerala':
        l9.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Kochi Tuskers Kerala':
        l9.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Pune Warriors India':
        l10.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Pune Warriors India':
        l10.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Rising Pune Supergiant(s)':
        l11.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Rising Pune Supergiant(s)':
        l11.append(df1['Team 2 Rating'].values[i])

for i in range(0, len(df1)):
    if df1['Team 1'].values[i] == 'Gujarat Lions':
        l12.append(df1['Team 1 Rating'].values[i])
    if df1['Team 2'].values[i] == 'Gujarat Lions':
        l12.append(df1['Team 2 Rating'].values[i])

plt.plot([i for i in range(len(l1))],l1,sns.xkcd_rgb["pale red"],label="Royal Challengers Bangalore")
plt.plot([i for i in range(len(l2))],l2,sns.xkcd_rgb["darkish blue"],label="Delhi Capitals/Delhi Daredevils")
plt.plot([i for i in range(len(l3))],l3,sns.xkcd_rgb["blue"],label="Mumbai Indians")
plt.plot([i for i in range(len(l4))],l4,sns.xkcd_rgb["goldenrod"],label="Chennai Super Kings")
plt.plot([i for i in range(len(l5))],l5,sns.xkcd_rgb["purple"],label="Kolkata Knight Riders")
plt.plot([i for i in range(len(l6))],l6,sns.xkcd_rgb["steel grey"],label="Kings XI Punjab")
plt.plot([i for i in range(len(l7))],l7,sns.xkcd_rgb["sky blue"],label="Rajasthan Royals")
plt.plot([i for i in range(len(l8))],l8,sns.xkcd_rgb["orange"],label="Sunrisers Hyderabad/Deccan Chargers")
plt.plot([i for i in range(len(l9))],l9,sns.xkcd_rgb["light pink"],label="Kochi Tuskers Kerala")
plt.plot([i for i in range(len(l10))],l10,sns.xkcd_rgb["navy"],label="Pune Warriors India")
plt.plot([i for i in range(len(l11))],l11,sns.xkcd_rgb["pinkish purple"],label="Rising Pune Supergiant(s)")
plt.plot([i for i in range(len(l12))],l12,sns.xkcd_rgb["peach"],label="Gujarat Lions")



#sns.lineplot([i for i in range(len(l1))],l1)
#sns.lineplot([i for i in range(len(l2))],l2)
#sns.lineplot([i for i in range(len(l3))],l3)
print(l1)
print(l2)
print(l3)
plt.legend(loc="lower right",prop={'size': 6})
plt.xlabel("Match number")
plt.ylabel("Glicko2 rating")
plt.savefig("graph.png")
plt.show()