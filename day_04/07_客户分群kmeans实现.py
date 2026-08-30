import pandas as pd
from scipy.ndimage import label
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import os
os.environ["OMP_NUM_THREADS"] = "1"

# 1. 加载数据
data = pd.read_csv('customers.csv')
print(data.head())
data.info()

# 2. 肘方法和轮廓系数选择K值超参数
# 获取训练数据
X = data.iloc[:, [3, 4]]

# 3.训练聚类模型
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_pred = kmeans.predict(X)

# 4.绘制聚类结果
plt.scatter(X.values[y_pred==0,0],X.values[y_pred==0,1],s=100,c='r',label='Cluster 1')
plt.scatter(X.values[y_pred==1,0],X.values[y_pred==1,1],s=100,c='b',label='Cluster 1')
plt.scatter(X.values[y_pred==2,0],X.values[y_pred==2,1],s=100,c='g',label='Cluster 1')
plt.scatter(X.values[y_pred==3,0],X.values[y_pred==3,1],s=100,c='cyan',label='Cluster 1')
plt.scatter(X.values[y_pred==4,0],X.values[y_pred==4,1],s=100,c='magenta',label='Cluster 1')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='black',label='Centroids')
plt.title('customer clusters')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()