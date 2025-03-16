from django.db import models
import joblib
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import cross_val_score

# Create your models here.
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ai', 'log_reg.pkl')

mnist = fetch_openml("mnist_784", as_frame=False)
X, y = mnist.data, mnist.target
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

def main():
    print(f"log_reg | pred: {predict(X_test[0])}, proba: {predict(X_test[0])}, acc: {accuracy(X_test, y_test)}, cv: {cross_val(X_train, y_train)}")

def load_model():
    try:
        return joblib.load(path)
    except Exception:
        print(f"Error {Exception}")
        return None

def predict(X_test):
    log_reg = load_model()
    return log_reg.predict([X_test])

def proba(X_test):
    log_reg = load_model()
    return log_reg.predict_proba([X_test])

def accuracy(X_test, y_test):
    log_reg = load_model()
    return log_reg.score(X_test, y_test)

def cross_val(X_train, y_train):
    log_reg = load_model()
    return cross_val_score(log_reg, X_train, y_train, cv=3, scoring="accuracy")

if __name__ == "__main__":
    main()