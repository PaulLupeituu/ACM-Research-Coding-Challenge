from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

input_data = pd.read_csv("ClusterPlot.csv")

x = input_data.copy()

kmeans = KMeans(3)
kmeans.fit(x)

clusters = x.copy()
clusters['cluster_pred'] = kmeans.predict(x)

plt.scatter(clusters['V1'], clusters['V2'], c = clusters['cluster_pred'], cmap = 'rainbow')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()