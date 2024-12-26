import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix
import numpy as np

# 读取数据集
data = pd.read_csv('car_recommendation_dataset.csv')

# 划分特征和标签
X = data.drop('is_interested', axis=1)
y = data['is_interested']

# 划分训练集、验证集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# 数据预处理
# 对数值特征进行标准化，对分类特征进行独热编码
numeric_features = X.select_dtypes(include=['number']).columns
categorical_features = X.select_dtypes(include=['object']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

X_train_preprocessed = preprocessor.fit_transform(X_train)
X_val_preprocessed = preprocessor.transform(X_val)
X_test_preprocessed = preprocessor.transform(X_test)

# 训练 SVM 模型
svm_model = SVC(kernel='rbf', C=1.0)
svm_model.fit(X_train_preprocessed, y_train)

# 在验证集上进行评估
y_val_pred = svm_model.predict(X_val_preprocessed)
val_accuracy = accuracy_score(y_val, y_val_pred)
val_recall = recall_score(y_val, y_val_pred)
val_f1 = f1_score(y_val, y_val_pred)

print(f"验证集准确率: {val_accuracy}")
print(f"验证集召回率: {val_recall}")
print(f"验证集 F1 值: {val_f1}")

# 调整参数（例如使用网格搜索）
# from sklearn.model_selection import GridSearchCV
# param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly']}
# grid_search = GridSearchCV(SVC(), param_grid, cv=5)
# grid_search.fit(X_train_preprocessed, y_train)
# best_params = grid_search.best_params_
# print("最佳参数:", best_params)

# 使用最佳参数重新训练模型
# svm_model = SVC(**best_params)
# svm_model.fit(X_train_preprocessed, y_train)

# 在测试集上进行评估
y_test_pred = svm_model.predict(X_test_preprocessed)
test_accuracy = accuracy_score(y_test, y_test_pred)
test_recall = recall_score(y_test, y_test_pred)
test_f1 = f1_score(y_test, y_test_pred)
conf_matrix = confusion_matrix(y_test, y_test_pred)

print(f"测试集准确率: {test_accuracy}")
print(f"测试集召回率: {test_recall}")
print(f"测试集 F1 值: {test_f1}")
print("混淆矩阵:")
print(conf_matrix)
