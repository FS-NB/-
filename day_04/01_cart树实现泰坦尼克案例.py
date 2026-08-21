"""
实现泰坦尼克案例:
    1. 数据加载
    2. 数据预处理
    3. 特征工程
    4. 模型训练
    5. 模型评估
    6. 模型预测
    7. 绘制图像
"""
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. 数据加载
titanic = pd.read_csv('train.csv')
print(titanic.head())
titanic.info()

# 2. 数据预处理
x = titanic[['Pclass','Sex','Age']].copy()
y = titanic['Survived']
x['Age'] = x['Age'].fillna(value=x['Age'].mean())

# 3. 特征工程
x = pd.get_dummies(x)
print(x.head())

# 数据集划分
x_train,x_text,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=22)

# 4. 模型训练
dtc = DecisionTreeClassifier(criterion='gini')
dtc.fit(x_train,y_train)

# 5. 模型评估
accuracy = dtc.score(x_text,y_test)

# 指标报告
y_pred = dtc.predict(x_text)
report = classification_report(y_test,y_pred)
print(report)

# 7. 绘制图像
plt.figure(figsize = (30,20))
plot_tree(
    dtc,
    max_depth=10,
    filled=True,
    feature_names=x.columns,
    class_names=['died','survived']
)
plt.show()