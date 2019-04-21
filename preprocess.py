import json


class Loading:
    def __init__(self, models, result):
        self.models_ids = models
        self.result = not int(result)

    def __str__(self):
        return "Models:{0}, Result: {1}".format(self.models_ids, self.result)


class Model:
    def __init__(self, name, height, width, weight):
        self.model_name = name
        self.height = height
        self.width = width
        self.weight = weight
    def __str__(self):
        return "{0}: height:{1}, width:{2}, weight:{3}".format(self.model_name, self.height, self.width, self.weight)


def get_data():
    file = open("./data")
    data = list()
    for line in file.readlines():
        data.append(Loading(list(line[:-5].split(' ')),line[-2:-1]))

    return data

def get_models_info():
    preferable_models = (33, 16, 10, 5, 4, 8, 11, 12, 1, 3, 15, 6, 13)
    models_info = list()
    file =json.load(open("./models_data"))
    for model_id in preferable_models:
        info = file[model_id-1]
        models_info.append(Model(info["brandName"]+" " +info["name"], info["height"], info["width"], info["weight"]))


    return models_info