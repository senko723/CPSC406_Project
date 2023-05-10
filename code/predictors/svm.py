# An SVM classifier

from sklearn.svm import SVC

def model(train_x, train_y):
    clf = SVC(kernel='linear')
    clf.fit(train_x, train_y)
    return clf
