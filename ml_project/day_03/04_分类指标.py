
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# 绘制混淆矩阵
y_true = ['e','e','e','e','e','e','l','l','l','l']

# 指定标签类别以及显示名称
labels = ['e','l']
de_labels = ['e(正例)','l(返例)']

# 模型A的预测结果
y_pred_A = ['e','e','e','l','l','l','l','l','l','l']
cm = confusion_matrix(y_true,y_pred_A,labels=labels)
cm_df = pd.DataFrame(cm,index=de_labels,columns=de_labels)
print(cm_df)
# 计算A模型的准确率
acc_A = accuracy_score(y_true, y_pred_A)
# 计算A模型的精确率
prec_A = precision_score(y_true, y_pred_A, pos_label="恶性")
# 计算A模型的召回率
rec_A = recall_score(y_true, y_pred_A, pos_label="恶性")
# 计算A模型的F1分数
f1_A = f1_score(y_true, y_pred_A, pos_label="恶性")
print("A模型的准确率: {:.2f}".format(acc_A), "精确率: {:.2f}".format(prec_A),
      "召回率: {:.2f}".format(rec_A), "F1分数: {:.2f}".format(f1_A))

# 模型B的预测结果
y_pred_B = ['e','e','e','e','e','e','e','e','e','l']
cm = confusion_matrix(y_true,y_pred_B,labels=labels)
cm_df = pd.DataFrame(cm,index=de_labels,columns=de_labels)
print(cm_df)

# 计算B模型的准确率
acc_B = accuracy_score(y_true, y_pred_B)
# 计算A模型的精确率
prec_B = precision_score(y_true, y_pred_B, pos_label="e")
# 计算A模型的召回率
rec_B = recall_score(y_true, y_pred_B, pos_label="e")
# 计算A模型的F1分数
f1_B = f1_score(y_true, y_pred_B, pos_label="e")
print("B模型的准确率: {:.2f}".format(acc_B), "精确率: {:.2f}".format(prec_B),
      "召回率: {:.2f}".format(rec_B), "F1分数: {:.2f}".format(f1_B))