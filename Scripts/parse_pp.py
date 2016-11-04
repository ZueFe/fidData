import re
import numpy as np

class Parse_pp:
    x = 'x="([\-\.0-9e]+)"'
    y = 'y="([\-\.0-9e]+)"'
    z = 'z="([\-\.0-9e]+)"'
    name = 'name="([0-9]+)"'

    """
    Method which takes .pp file opens it and returns tuples of parsed positions of landmarks
    """
    @staticmethod
    def parsePP(file):
        inputFile = open(file)

        fps = []
        for line in inputFile.readlines():
            fp_name = re.search(Parse_pp.name, line)
            fp_x = re.search(Parse_pp.x, line)
            fp_y = re.search(Parse_pp.y, line)
            fp_z = re.search(Parse_pp.z, line)

            if(fp_name == None):
                continue

            final_name = int(fp_name.group(1))
            final_x = float(fp_x.group(1))
            final_y = float(fp_y.group(1))
            final_z = float(fp_z.group(1))

            fps.append([final_name, final_x, final_y, final_z])

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
    Creates array containing model_name as first entry and dictionary (having landmark number for key)
    with landmark type and position as second entry.
    """
    @staticmethod
    def returnModel(pp_dic, model_name):
        dic = dict()

        for entry in pp_dic:
            dic[entry[0]] = tuple([entry[1], entry[2], entry[3]])

        final_model = [model_name, dic]
        return final_model

    """
    Method ditches name of the landmark and return only its position as numpy array
    """
    @staticmethod
    def returnNumVector(self, pp_tuple):
        if len(pp_tuple) != 4:
            return None #error

        return np.array(pp_tuple[1:])
