import pandas as pd
import matplotlib.pyplot as plt

# TODO: load the dataset as pandas dataframe
# test
plt.figure(figsize=(5, 10)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(False)

# TODO: change the title name to include your name
plt.title("plot for mammal_teeth dataset")
plt.savefig("mammal_teeth_scatterplot.png", dpi=150) # save the figure