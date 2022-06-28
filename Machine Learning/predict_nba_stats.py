import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model

PATH = "C:\\Users\\avash\\Documents\\Python\\"

data = pd.read_csv(PATH+"lebron_stats.csv",)
data = data.drop(['Lg', 'Tm', 'Season', 'Pos', 'GS'], axis=1)
data = data[data.columns]

target = "PTS"

X = np.array(data.drop([target], 1))
y = np.array(data[target])

X_train, X_test, y_train, y_test = train_test_split(X, y)

linear = linear_model.LinearRegression()

linear.fit(X_train, y_train)

predictions = linear.predict(X_test)
for i in range(len(predictions)):
    print(f"Predicted value: {predictions[i]}\nActual value: {y_test[i]}")
    print("-"*20)

accuracy = linear.score(X_test, y_test)
print("Accuracy:", str(round(accuracy*100, 2)) + "%")
