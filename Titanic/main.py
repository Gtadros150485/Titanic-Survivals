import pandas as pd
import numpy as np
import matplotlib as mpl
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("../Titanic/Data/train.csv")
test = pd.read_csv("../Titanic/Data/test.csv")
test_ids = test["PassengerId"]

def clean(data):
    data = data.drop(["Ticket","Cabin","Name","PassengerId"], axis = 1)

    cols = ["SibSp", "Parch", "Fare", "Age"]

    for col in cols:
        data[col].fillna(data[col].median(), inplace = True)

    data.Embarked.fillna("U", inplace = True)
    return data
data = clean(data)
test = clean(test)
le = preprocessing.LabelEncoder()
columns = ["Sex", "Embarked"]

for col in columns:
    data[col] = le.fit_transform(data[col])
    test[col] = le.transform(test[col])
    print(le.classes_)

y = data["Survived"]
X = data.drop("Survived", axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(random_state=0, max_iter=1000).fit(X_train, y_train)
predictions = clf.predict(X_val)

accuracy_score(y_val, predictions)
sumbission_preds = clf.predict(test)
df = pd.DataFrame({"PassengerId":test_ids.values, "Survived":sumbission_preds})
df.to_csv("answer.csv", index = False)
