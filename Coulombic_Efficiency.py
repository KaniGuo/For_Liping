import pandas as pd
import matplotlib.pyplot as plt

filename = "1"
precision = 0.0001
cycle = 200


df = pd.read_table(filename +".txt", delimiter="\s")

time_list = [df.iloc[0, 0]]
q_list = [df.iloc[0, 1]]
ratio_list = []

times = df["time/s"]
q_value = df["(Q-Qo)/C"]

row_num = len(times)

for i in range(1, row_num):
    if (q_value[i+1]-q_value[i])*(q_value[i-1]-q_value[i])>=0:
        if abs(q_value[i] - q_list[-1]) > (abs(q_value[i])*precision):
            time_list.append(times[i])
            q_list.append(q_value[i])
            print(i, "\t", times[i], "\t", q_value[i])
            if len(time_list) >= 2*cycle + 2:
                break

for i in range(1, cycle+1):
    j = 2*i-1
    ratio = (q_list[j+1]-q_list[j])/(q_list[j-1]-q_list[j])*100
    ratio_list.append(ratio)

df2 = pd.DataFrame(ratio_list)
df2.index += 1
df2.index.name = "Cycle number"
df2.columns = ["Coulombic Efficiency (%)"]
df2.to_csv(filename + ".csv")

x = range(len(ratio_list))
print(len(ratio_list), " Cycles")
plt.scatter(x, ratio_list, label=filename)
plt.xlabel("Cycle number (n)")
plt.ylabel("Coulombic efficiency (%)")
plt.legend()
plt.savefig(filename+".png")
plt.show()

        
        





