from sklearn import tree 

x = [[0,0],[1,1]]
y = [0,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[2., 2.]])
print("Prediction:", prediction)

prediction = clf.predict([[3, 3]])
print("Prediction:", prediction)

prediction = clf.predict([[0.5, 0.5]])
print("Prediction:", prediction)

prediction = clf.predict([[0,0], [1,1], [2,2], [3,1]])
print("Prediction:", prediction)