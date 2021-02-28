#데이터마이닝 12주차
#60181912 유성연

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

digits = load_digits()
X=digits.data
y=digits.target
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,random_state=0)
model = tree.DecisionTreeClassifier()
model.fit(Xtrain,ytrain)
y_model = model.predict(Xtest)
print("정확도",accuracy_score(ytest, y_model))
