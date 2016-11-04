import numpy as np
import json

class Matrix(object):
    """
    Creates Matrix object for given model_name, storing FP
    with given ID as (ID-1)th index in numpy array
    """
    def __init__(self, fps, model_name, ignore=(-1)):
        self.model_name = model_name
        self.ignore = ignore
        self.fps = self.create_fps(fps, ignore)


    def create_fps(self, fps, ignore):
        a = np.zeros(shape=(len(fps), 3))

        for i in range(0, len(fps)):
            #if i not in fps or
            if (i + 1) not in fps or (i + 1) in ignore:
                a[i] = [0, 0, 0]
            else:
                a[i] = list(fps[i+1])

        return a

    def save_fps(self, path):
        b = self.fps.tolist()

        file_path = path + self.model_name + '.json'
        with open(file_path, 'w') as fp:
            json.dump(b, fp)
