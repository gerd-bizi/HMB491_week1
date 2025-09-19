import pandas as pd
import matplotlib.pyplot as plt

df_teeth = pd.read_csv("mammal_teeth.csv")

plt.figure(figsize=(5, 10)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(False)

plt.title("plot for mammal_teeth dataset — Olivia")
plt.savefig("mammal_teeth_scatterplot.png", dpi=150) # save the figure