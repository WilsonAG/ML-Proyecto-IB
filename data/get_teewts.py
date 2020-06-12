import pandas as pd
import random


if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    new=data.values.tolist()
    new=[i for i in new if i[1]!='neutro']
    con=0
    long=len(new)
    ran=[]
    while con!=1000:
         num = random.randrange(long)
         if num not in ran:
             ran.append(num)
             con+=1
    new_data=[new[i] for i in ran]
    new_data=pd.DataFrame(new_data,columns=['tweets','status'])
    new_data.to_csv ('./data./tweets/tweets.csv',index=False)
    #print(new_data)
    
