import csv
import numpy as np

class Parse_CSV:

    """
    Takes CSV file and CSV separator and returns array, where first entry is name of the model
    and second entry is dictionary containing ID of landmark as the key and tuple with coordinates as values
    """
    @staticmethod
    def parse_csv(file, sep):
        final_model = []

        with open(file, newline='\n') as f:
            reader = csv.reader(f, delimiter=sep)
            next(reader, None)      #ignore the header

            dic = dict();
            name = ""
            counter = 0
            fp_coord = []

            for row in reader:
                for entry in row:
                    if counter == 0:
                        name = entry          #name of the model
                    else:
                        fp_coord.append(float(entry))
                        if counter % 3 == 0:        #take three values that mark position of single FP
                            dic[counter // 3] = tuple(fp_coord)
                            fp_coord = []

                    counter += 1

            final_model.append([name, dic])

        return final_model

        
