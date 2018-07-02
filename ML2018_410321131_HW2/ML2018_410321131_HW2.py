import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn import ensemble, svm, metrics

def fetch_data():
    # Fetching dataset
    data = fetch_mldata('MNIST original')
    X, y= data['data'], data["target"]

    # Normalize preprocessing
    X = X / 255

    # Split train data and test data
    n = 60000
    X_train = X[:n]
    y_train = y[:n]
    X_test = X[n:]
    y_test = y[n:]

    X_train = X_train.astype("float32")
    X_test = X_test.astype("float32")

    #Randomize train data
    shuffle_index = np.random.permutation(60000)
    X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]

    return X_train, y_train, X_test, y_test 

def RandomForest_model(X_train, y_train, X_test, y_test):
    # RandomForest model
    forest = ensemble.RandomForestClassifier(n_estimators = 100)
    forest_fit = forest.fit(X_train, y_train)

    # Predict
    y_test_predict = forest.predict(X_test)

    # Accuracy and AUC
    accuracy = metrics.accuracy_score(y_test, y_test_predict)
    print("RandomForest model accuracy:",accuracy)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_test_predict, pos_label=2)
    auc = metrics.auc(fpr, tpr, reorder=False)
    print("RandomForest model AUC:",auc)

def SVM_model(X_train, y_train, X_test, y_test):
    # SVM model
    svc = svm.SVC()
    svc_fit = svc.fit(X_train, y_train)

    # Predict
    y_test_predict = svc.predict(X_test)

    # Accuracy and AUC
    accuracy = metrics.accuracy_score(y_test, y_test_predict)
    print("SVM model accuracy:",accuracy)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_test_predict, pos_label=2)
    auc = metrics.auc(fpr, tpr, reorder=False)
    print("SVM model AUC:",auc)

def main():

    print("Fetching dataset...")
    X_train, y_train, X_test, y_test = fetch_data()
    print("RandomForest model training...")
    RandomForest_model(X_train, y_train, X_test, y_test)
    print("SVM model training...")
    SVM_model(X_train, y_train, X_test, y_test)

if __name__ == "__main__":
    main()