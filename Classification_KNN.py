import pandas as pd
import pandas as pd
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from math import sqrt
import math

class KNN:
    def findDistance(self, x_test):#find distance of x_test from all the training data
        distance=[]
        for j in range(len(x_train)):
            a=(x_train[j][0]-x_test[0])
            b=(x_train[j][1]-x_test[1])
            c=(x_train[j][2]-x_test[2])
            d=(x_train[j][3]-x_test[3])
            summ=a*a+b*b+c*c+d*d
            dist=math.sqrt(summ)
            distance.append((x_train[j],y_train[j],dist))
        return distance
    def findClass(self,neighbors):
        pred_class={}
        neigh=[]
        for g in range(len(neighbors)-1):
            neigh.append(neighbors[g][-1])
		
        for h in range(len(neigh)-1):  
            if(neigh[h] in pred_class):
                pred_class[neigh[h]]=pred_class[neigh[h]]+1
            else:
                pred_class[neigh[h]]=1 
       
	   #sort the dict in descending order by value
        sorting=sorted(pred_class.items(), key=lambda pred_class:pred_class[1])
        fin_cl=sorting[0][0]
        return fin_cl

#iris dataset with 3 classes  
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df=pd.read_csv(url, names=names)
array=df.values
x=list(array[:,0:4])
y=list(array[:, 4])
print("dataset loaded")
validation_size=0.40
print("spliting into training and testing dataset")
x_train, x_test,y_train, y_test=model_selection.train_test_split(x,y, test_size=validation_size)
kn=KNN()

#Neighbors should not be in multiple of number of classes (3,6,..) in order to avoid confusion to classifier
print("enter the number of neighbors")
k=input()
k=int(k)
predictions=[]
for i in range(len(x_test)):
    distance=kn.findDistance(x_test[i])
    distance.sort(key=lambda elem: elem[2]) #sort the elements according to distance
    neighbors = []
    for x in range(k): 
        neighbors.append((distance[x][0],distance[x][1]))
    predict_class=kn.findClass(neighbors)
    predictions.append(predict_class)
print("accuracy score")	
print(accuracy_score(y_test,predictions))
print("classification report")
print(classification_report(y_test, predictions))
   
  

