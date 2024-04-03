import pandas as pd

train = pd.read_csv("../Titanic/Data/train.csv")
test = pd.read_csv("../Titanic/Data/test.csv")

def clean(data):
    data.drop(["PassengerId", "Name", "Cabin", "Ticket"], axis = 1)

    cols = ["SibSp", "Parch", "Fare", "Age"]
    for col in col:
        data[col].fillna(data[col].meadian(), inplace = True)

    data.Embarked.fillna