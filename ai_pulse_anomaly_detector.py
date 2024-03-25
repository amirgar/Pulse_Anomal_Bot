import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree


def ai(arr):
    # 81 - женщина, 213 - мужчины
    # 28 - мин. возраст, 66 - макс. возраст
    """
    Если диабетик, то нужны параметры холестерин в крови и уровень сахара в крови натощак
    """

    # formating of data base
    data = pd.read_csv('heart-disease.csv', delimiter=',')
    data.pop('thal')
    data.pop('ca')
    data.pop('slope')
    data.pop('oldpeak')
    data.pop('chol')
    data.pop('restecg')
    data.pop('fbs')

    array_trestbps = list(np.array(data[data['trestbps'] == '?'].index))
    data = data.drop(labels=array_trestbps)
    data['trestbps'] = data['trestbps'].astype('int64')

    array_thalach = list(np.array(data[data['thalach'] == '?'].index))
    data = data.drop(labels=array_thalach)

    data['thalach'] = data['thalach'].astype('int64')

    array_exang = list(np.array(data[data['exang'] == '?'].index))
    data = data.drop(labels=array_exang)

    data['exang'] = data['exang'].astype('int64')
    data['age'] = data['age'].astype('int64')

    data.rename(columns={'num       ': 'num'}, inplace=True)

    y = data['num']
    x = data.drop(columns=['num'])
    data = data.drop(columns=['num'])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10, shuffle=True)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    # print(f1_score(y_test, y_pred, average='binary'))

    # In test data: age, sex, cp, trestbps, thalach, exang
    user_data = pd.Series(arr).values.reshape(1, -1)
    if clf.predict(user_data) == [0]:
        return 'Аномалии не обнаружены'
    else:
        return 'Обнаружена аномалия, рекомендуется обратиться к врачу'
