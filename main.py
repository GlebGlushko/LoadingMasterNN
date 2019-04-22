import preprocess
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


def learn(data):
    X = list()
    Y = list()
    for loading in data:
        X.append(loading.models_ids)
        Y.append(loading.result)

    train_x, check_y, val_x, val_y = train_test_split(X, Y, random_state=1)
    model = DecisionTreeRegressor()
    model.fit(train_x, val_x)
    predictions = model.predict(check_y)
    error = mean_absolute_error(val_y,predictions)
    for i in range(0,len(predictions)):
        print("Prediction:{0}, Real:{1}".format(bool(predictions[i]),val_y[i]))
    print(val_y)
    print(error)


if __name__=="__main__":
    data = preprocess.get_data()
    models_info = preprocess.get_models_info()
    data7 = list()
    data8 = list()
    for x in data:
        if sum(x.models_ids) == 7:
            data7.append(x)
        else:
            data8.append(x)

    learn(data)