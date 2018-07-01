import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata

def load_data():
    # Fetching dataset
    print("Fetching dataset...")
    data = fetch_mldata('MNIST original')
    X, Y= data['data'], data["target"]

    # Normalize preprocessing
    X = X / 255

    # Split train data and test data
    n_train = 60000
    X_train = X[:n_train]
    Y_train = Y[:n_train]
    n_test = 10000
    X_test = X[n_test:]
    Y_test = Y[n_test:]

    return X_train, X_test, Y_train, Y_test 

def main():
    load_data()

if __name__ == "__main__":
    main()