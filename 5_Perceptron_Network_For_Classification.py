# pip install scikit-learn

from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X , y = make_classification(n_samples=1000, n_features=10, n_redundant=0, random_state=1)
print("X => ", X)
print("y => ", y)
print("X[1] => ", X[1])
print("y[0] => ", y[0])
model = Perceptron()
xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size=0.8,random_state=1)
print("xtrain.shape,xtest.shape,ytrain.shape,ytest.shape => ",xtrain.shape,xtest.shape,ytrain.shape,ytest.shape)
model.fit(xtrain,ytrain)
predictions = model.predict(xtest)
accuracy_score(ytest,predictions)
