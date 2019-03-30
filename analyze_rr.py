import csv
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join

class ECG_RR:
    def __init__(self):
        self.list_tuple=1
    def readCSV(self, file_name):
        csv_file = open(file_name, mode='r')
        data = csv.DictReader(csv_file)
        return data
    def parseVal(self):
        onlyfiles = [f for f in listdir("/Users/abhishekmishra/Downloads/Hackathon/ECG_RR/bidmc_csv") if isfile(join("/Users/abhishekmishra/Downloads/Hackathon/ECG_RR/bidmc_csv", f))]
        mypath = "/Users/abhishekmishra/Downloads/Hackathon/ECG_RR/bidmc_csv/"
        numerics_data_list=[]
        signals_data_list=[]
        breath_data_list=[]
        numerics = ECG_RR()
        signals = ECG_RR()
        breath = ECG_RR()
        for i in range(len(onlyfiles)):
            if onlyfiles[i][0]!=".":
                if onlyfiles[i].split("_")[2][0]=="N":
                    numerics_data = numerics.readCSV(mypath+onlyfiles[i])
                    numerics_data_list.append(numerics_data)
        for i in range(len(onlyfiles)):
            if onlyfiles[i][0]!=".":
                if onlyfiles[i].split("_")[2][0]=="S":
                    signals_data = numerics.readCSV(mypath+onlyfiles[i])
                    signals_data_list.append(signals_data)
        for i in range(len(onlyfiles)):
            if onlyfiles[i][0]!=".":
                if onlyfiles[i].split("_")[2][0]=="B":
                    breath_data = numerics.readCSV(mypath+onlyfiles[i])
                    breath_data_list.append(breath_data)
        #for row in signals_data_list[0]:
        #    print row.keys()
        for j in range(10):
            resp_array=[]
            time_series=[]
            for row in signals_data_list[j]:
                    resp_array.append(row[" RESP"])
                    time_series.append(row["Time [s]"])
            plt.figure(j+1)
            plt.autoscale(True)
            plt.plot(time_series,resp_array)
            plt.show()
        #personal = ECG_RR()
        #Spersonal_data = personal.readCSV("/bidmc_csv/")

inst = ECG_RR()
inst.parseVal()
