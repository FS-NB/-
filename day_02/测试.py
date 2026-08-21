from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score

def knniris():
    # 1. 导入数据集
    iris = load_iris()
    print("Iris data shape:", iris.data.shape)
    # 2. 数据预处理->数据集划分
    # test_size=0.3 数据集划分比例: 7: 3, random_state=22, 每个种子对应一个随机结果
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=22)
    print("X_train shape:", x_train.shape)
    print('X_test shape:', x_test.shape)
    # 3. 特征工程-->特征预处理(标准化)
    scalar = StandardScaler()
    # 训练集标准化
    x_train = scalar.fit_transform(x_train)
    # 测试集标准化, 直接套用训练集fit的结果, 转换测试集
    x_test = scalar.transform(x_test)
    # 4. 训练模型
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train, y_train)
    # 5. 模型评估
    # ① 使用model.score --> 获取准确率
    acc = knn.score(x_test, y_test)  # 两个参数依次: 测试集特征, 测试集标签
    print("knn.Score Accuracy:", acc)
    # ② 使用accuracy_score 获取准确率
    y_pred = knn.predict(x_test)
    acc = accuracy_score(y_test, y_pred)  # 两个参数依次: 真实值, 预测值
    print("Accuracy Score:", acc)

    # 6. 模型预测
    mydata =  [[5.1, 3.5, 1.4, 0.2],
                [4.6, 3.1, 1.5, 0.2]]
    # 预测特征标准化(预测数据要保持和训练数据格式一样)
    mydata = scalar.transform(mydata)
    # 模型预测
    # 预测标签
    y_pred = knn.predict(mydata)
    print("Predicted labels:", y_pred)
    # 预测概率
    y_prob = knn.predict_proba(mydata)
    print("Predicted probabilities:", y_prob)


if __name__ == '__main__':
    knniris()
