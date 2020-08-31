import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

qb = pd.read_csv("fantasy football - QB.csv")
wr = pd.read_csv("fantasy football - WR.csv")
te = pd.read_csv("fantasy football - TE.csv")
rb = pd.read_csv("fantasy football - RB.csv")

all_pos = [qb,wr,te,rb]
all_pos_fpts = []
names = {0:"QB",1:"WR", 2: "TE",3:"RB"}
every_ten_mean = {"QB": [],"WR": [],"TE": [],"RB": []}

for i in all_pos:
    fpts = np.asfarray(list(map(lambda y: float(y),list(filter(lambda x:x!="--" ,list(i['FPTS'])))))) #removes  "--"
    all_pos_fpts.append(fpts)
    print(f"Length: {fpts.shape[0]}")
    print(f"Mean: {np.mean(fpts)}")
    print(f"Standard Deviation: {np.std(fpts)}")

pos_counter = 0
for pos in all_pos_fpts:
    counter = 1
    a = []
    for j in range(pos.shape[0]):
        a.append(pos[j])
        if counter %10 == 0:
            every_ten_mean[names[pos_counter]].append(a)
            a = []
            counter = 1
        else: 
            counter += 1
    pos_counter+=1

pos_counter = 0
for v in every_ten_mean.values():
    lag_10_means = list(map(lambda x: sum(x)/len(x),v))
    print(f"{names[pos_counter]}: {lag_10_means}")
    plt.plot(range(len(lag_10_means)),lag_10_means)
    plt.title(f"{names[pos_counter]} means")
    plt.show()
    pos_counter+=1






