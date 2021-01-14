# Import necessary libraries
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Load the Iris data
data = pd.read_csv("data/Iris_data.csv")


# Split the data int X and y
X = data.drop(['Species'], axis=1)
y = data['Species']



# Split the data for training and testing at a ratio of 80/20
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size = 0.2)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Run prediction and print acuracy score
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))


# Save the model (serialize)
import pickle
pickle.dump(model, open("iris_model_jan_2020_v1.pkl", "wb"))