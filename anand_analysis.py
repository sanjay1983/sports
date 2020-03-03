import pandas as pd

df=pd.read_csv("chess_player_data_anand.csv")
eval=[]
move=[]
evals=[]
moves=[]
colour=[]
anand_move=[]
anand_moves=[]
anand_eval=[]
anand_evals=[]
optimal_king=0
sub_optimal_king=0
balanced_king=0
optimal_queen=0
sub_optimal_queen=0
balanced_queen=0
optimal_rook=0
sub_optimal_rook=0
balanced_rook=0
optimal_bishop=0
sub_optimal_bishop=0
balanced_bishop=0
optimal_knight=0
sub_optimal_knight=0
balanced_knight=0
optimal_pawn=0
sub_optimal_pawn=0
balanced_pawn=0
total_king=0
total_queen=0
total_rook=0
total_bishop=0
total_knight=0
total_pawn=0

total_moves=0
total_moves_2=0
prev=0
player1='Anand,V'
player2='Mamedyarov,S'
for i in range(len(df)):
    if "#-" in df['Evaluation'].values[i]:
        df['Evaluation'].values[i]=(str)(-100)
for i in range(len(df)):
    if "#" in df['Evaluation'].values[i]:
        df['Evaluation'].values[i] = 100
    df['Evaluation'].values[i]=(float)(df['Evaluation'].values[i])
    if df['Player 1'].values[i]==player1 and df['Player 2'].values[i]==player2:
        eval.append(df['Evaluation'].values[i])
        move.append(df['Move'].values[i])
    else:
        if player1 == 'Anand,V':
            colour.append('W')
            for j in range((int)((1+len(move))/2)):
                anand_move.append(move[2*j])
                anand_eval.append(eval[2*j]-prev)
                if (j!=(int)(len(move)/2)):
                    prev=eval[2*j+1]
        if player2 == 'Anand,V':
            colour.append('B')
            for j in range((int)(len(move)/2)):
                if (len(move)%2==0):
                    prev_b=eval[2*j]
                    anand_move.append(move[2*j+1])
                    anand_eval.append(eval[2*j+1]-prev_b)
                if (len(move)%2!=0):
                    for p in range(1,(int)(len(move)/2)):
                        anand_move.append(move[2*p-1])
                        anand_eval.append(eval[2*p-1]-eval[2*p-2])
        anand_evals.append(anand_eval)
        anand_eval=[]
        anand_moves.append(anand_move)
        anand_move=[]
        evals.append(eval)
        eval=[]
        moves.append(move)
        move=[]
        player1=df['Player 1'].values[i]
        player2=df['Player 2'].values[i]
        eval.append(df['Evaluation'].values[i])
        move.append(df['Move'].values[i])
#print(evals)
#print(moves)
#print(colour)
print(anand_moves)
#print(anand_evals)

for i in range(len(anand_evals)):
    for j in range(len(anand_evals[i])):
        if anand_moves[i][j][0]=='K':
            if anand_evals[i][j]>0.0:
                optimal_king+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_king+=1
            if anand_evals[i][j]==0.0:
                balanced_king+=1
            total_king+=1
        if anand_moves[i][j][0]=='Q':
            if anand_evals[i][j]>0.0:
                optimal_queen+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_queen+=1
            if anand_evals[i][j]==0.0:
                balanced_queen+=1
            total_queen+=1
        if anand_moves[i][j][0]=='R':
            if anand_evals[i][j]>0.0:
                optimal_rook+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_rook+=1
            if anand_evals[i][j]==0.0:
                balanced_rook+=1
            total_rook+=1
        if anand_moves[i][j][0]=='B':
            if anand_evals[i][j]>0.0:
                optimal_bishop+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_bishop+=1
            if anand_evals[i][j]==0.0:
                balanced_bishop+=1
            total_bishop+=1
        if anand_moves[i][j][0]=='N':
            if anand_evals[i][j]>0.0:
                optimal_knight+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_knight+=1
            if anand_evals[i][j]==0.0:
                balanced_knight+=1
            total_knight+=1
        if anand_moves[i][j][0].islower():
            if anand_evals[i][j]>0.0:
                optimal_pawn+=1
            if anand_evals[i][j]<0.0:
                sub_optimal_pawn+=1
            if anand_evals[i][j]==0.0:
                balanced_pawn+=1
            total_pawn+=1



print("Optimal king moves: ", optimal_king)
print("Sub-optimal king moves: ", sub_optimal_king)
print("Balanced king moves: ", balanced_king)
print("Total king moves: ", total_king)
print("________________________________")
print("Optimal queen moves: ", optimal_queen)
print("Sub-optimal queen moves: ", sub_optimal_queen)
print("Balanced queen moves: ", balanced_queen)
print("Total queen moves: ", total_queen)
print("________________________________")
print("Optimal rook moves: ", optimal_rook)
print("Sub-optimal rook moves: ", sub_optimal_rook)
print("Balanced rook moves: ", balanced_rook)
print("Total rook moves: ", total_rook)
print("________________________________")
print("Optimal bishop moves: ", optimal_bishop)
print("Sub-optimal bishop moves: ", sub_optimal_bishop)
print("Balanced bishop moves: ", balanced_bishop)
print("Total bishop moves: ", total_bishop)
print("________________________________")
print("Optimal knight moves: ", optimal_knight)
print("Sub-optimal knight moves: ", sub_optimal_knight)
print("Balanced knight moves: ", balanced_knight)
print("Total knight moves: ", total_knight)
print("________________________________")
print("Optimal pawn moves: ", optimal_pawn)
print("Sub-optimal pawn moves: ", sub_optimal_pawn)
print("Balanced pawn moves: ", balanced_pawn)
print("Total pawn moves: ", total_pawn)
print("________________________________")