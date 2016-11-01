import re
import numpy as np

class Parse_pp:
    def __init__(self):
        self.x = 'x="([\-\.0-9]+)"'
        self.y = 'y="([\-\.0-9]+)"'
        self.z = 'z="([\-\.0-9]+)"'
        self.name = 'name="([0-9]+)"'

    """
    Method which takes .pp file opens it and returns tuples of parsed positions of landmarks
    """
    @staticmethod
    def parsePP(self, file):
        inputFile = open(file)

        fps = []
        for line in inputFile.readlines():
            fp_name = re.search(self.name, line)
            fp_x = re.search(self.x, line)
            fp_y = re.search(self.y, line)
            fp_z = re.search(self.z, line)

            if(fp_name == None):
                continue

            fps.append((fp_name.group(1), fp_x.group(1), fp_y.group(1), fp_z.group(1)))

        return fps


    """
    Method ditches name of the landmark and returns only its position
    """
    @staticmethod
    def returnVector(pp_tuple):
        if len(pp_tuple) != 4:
            return None     #error

        return tuple(pp[1], pp[2], pp[3])


    """
    Method ditches name of the landmark and return only its position as numpy array
    """
    @staticmethod
    def returnNumVector(pp_tuple):
        if len(pp_tuple) != 4:
            return None #error

        return np.array(pp_tuple[1:])
