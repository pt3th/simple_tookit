from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = svm.SVC()
cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=0)
clf = GridSearchCV(svc, parameters, scoring='balanced_accuracy', cv=cv)
clf.fit(iris.data, iris.target)
print(clf.best_score_)
print(clf.best_params_)
