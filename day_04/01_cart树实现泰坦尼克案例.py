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

# 1. 数据加载
titanic = pd.read_csv('train.csv')
print(titanic.head())
titanic.info()

# 2. 数据预处理
x = titanic[['Pclass','Sex','Age']]
y = titanic['Survived']
x['Age'] = x['Age'].fillna(value=x['Age'].mean())

# 3. 特征工程
x = pd.get_dummies(x)
print(x.head())
# 4. 模型训练
# 5. 模型评估
# 6. 模型预测
# 7. 绘制图像