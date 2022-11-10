import csv
import pandas as pd
import matplotlib.pyplot as plt
# D:\Downloads\dwm\data_visual.csv
df = pd.read_csv("data_visual.csv")
data = df.values.tolist()

df = pd.DataFrame(
    data, columns=['Id', 'Gender', 'Age', 'Sales', 'Bmi', 'Income'])
df.hist()
plt.show()
