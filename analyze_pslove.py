import csv
import matplotlib.pyplot as plt
import numpy
from os import listdir
from os.path import isfile, join

class pslove:
    def __init__(self):
        self.list_tuple=1
    def readCSV(self, file_name):
        csv_file = open(file_name, mode='rU')
        data = csv.DictReader(csv_file)
        return data
    def date2days(self, date):
        if len(date) and '/' in date:
            date=date.strip('')
            date=date.split("/")
            #print int(date[0]) + int(date[1])*30 + int(date[2])*365
            return int(date[0]) + int(date[1])*30 + int(date[2])*365
        else:
            return len(date)
    def totalcoloumn(self,matrix):
        temp=[]
        for row in matrix:
            sum=0
            for i in range(len(row)):
                sum+=int(row[i])
            temp.append(sum)
        return temp
    def coloumn(self, matrix, i):
        temp=[]
        for row in matrix:
            if i<len(row):
                temp.append(row[i])
        return temp
    def parseVal(self):
        #onlyfiles = [f for f in listdir("/Users/abhishekmishra/Downloads/Hackathon/ECG_RR/bidmc_csv") if isfile(join("/Users/abhishekmishra/Downloads/Hackathon/ECG_RR/bidmc_csv", f))]
        mypath = "/Users/abhishekmishra/Downloads/Hackathon/pslovedata/"
        period = pslove()
        user = pslove()
        symptom = pslove()
        period_data = period.readCSV(mypath+"Period.csv")
        user_data = user.readCSV(mypath+"User.csv")
        symptom_data = symptom.readCSV(mypath+"Symptom.csv")
        user_id_array=set()
        user_dict={}
        for row in user_data:
            user_id_array.add(row["id"])
        for i in range(len(list(user_id_array))):
            user_dict[list(user_id_array)[i]]=[]
        user_data = user.readCSV(mypath+"User.csv")
        for row in user_data:
            user_dict[row["id"]].append(row)
        period_data = period.readCSV(mypath+"Period.csv")
        for row in period_data:
            user_dict[row["User_id"]].append(row)
        symptom_data = symptom.readCSV(mypath+"Symptom.csv")
        for row in symptom_data:
            user_dict[row["user_id"]].append(row)
        analyze_list=[]
        for key in user_dict.keys():
            flag=1
            index=1
            final_index=1
            if len(user_dict[key])>1:
                while(flag):
                    if "User_id" in user_dict[key][index].keys():
                        index+=1
                    else:
                        flag=0
                        final_index=index
                        index=final_index
                    if index==len(user_dict[key]):
                        break
                while(index<len(user_dict[key])):
                    temp=[]
                    temp.append(user_dict[key][0]['cycle_length_initial'])
                    temp.append(user_dict[key][0]['period_length_initial'])
                    val=self.date2days(user_dict[key][index]["date"])
                    flag=0
                    for i in range(1,final_index):
                        #print self.date2days(user_dict[key][i]["end_date"]) - self.date2days(user_dict[key][i]["start_date"])
                        if (val>=self.date2days(user_dict[key][i]["start_date"]) and val<=self.date2days(user_dict[key][i]["end_date"])):
                            if (val-self.date2days(user_dict[key][i]["start_date"]))>0 and (val-self.date2days(user_dict[key][i]["start_date"]))<15:
                                temp.append(val-self.date2days(user_dict[key][i]["start_date"]))
                                #print val-self.date2days(user_dict[key][i]["start_date"])
                            else:
                                temp.append(0)
                            flag=1
                            break
                    if flag==0:
                        temp.append(flag)
                    index+=1
                    if 'backache' in user_dict[key][index-1].keys():
                        temp.append(user_dict[key][index-1]['backache'])
                        temp.append(user_dict[key][index-1]['cramp'])
                        temp.append(user_dict[key][index-1]['mood'])
                        temp.append(user_dict[key][index-1]['bloating'])
                        temp.append(user_dict[key][index-1]['acne'])
                        temp.append(user_dict[key][index-1]['diarrhea'])
                        temp.append(user_dict[key][index-1]['sore'])
                        temp.append(user_dict[key][index-1]['dizzy'])
                        temp.append(user_dict[key][index-1]['nausea'])
                        temp.append(user_dict[key][index-1]['headache'])
                    analyze_list.append(temp)
            else:
                temp=[]
                temp.append(user_dict[key][0]['cycle_length_initial'])
                temp.append(user_dict[key][0]['period_length_initial'])
                analyze_list.append(temp)
        pain_dict={}
        pain_dict["1"]='backache'
        pain_dict["2"]='cramp'
        pain_dict["3"]='mood'
        pain_dict["4"]='bloating'
        pain_dict["5"]='acne'
        pain_dict["6"]='diarrhea'
        pain_dict["7"]='sore'
        pain_dict["8"]='dizzy'
        pain_dict["9"]='nausea'
        pain_dict["10"]='headache'
        """for i in range(10):
            string=pain_dict[str(i+1)]
            plt.figure(i+1)
            colors = (0,0,0)
            area = numpy.pi*3
            plt.scatter(self.coloumn(analyze_list,2),self.coloumn(analyze_list,3+i),s=area, c=colors, alpha=0.7)
            plt.xlabel("Days passed from start of period")
            plt.ylabel(string+" Score")
            plt.title(string + " variation with period onset")
            plt.yticks(numpy.arange(1,100,20))
            plt.savefig(string+".png")
            plt.show()"""
        """for i in range(1):
            plt.figure(i+1)
            colors = (0,0,0)
            area = numpy.pi*3
            plt.scatter(self.coloumn(analyze_list,1),self.totalcoloumn(analyze_list),s=area, c=colors, alpha=0.7)
            plt.xlabel("Initial period length")
            plt.ylabel("Total pain Score")
            plt.title("Pain variation with initial period length")
            plt.yticks(numpy.arange(1,1500,100))
            plt.savefig("Pain Initial Period.png")
            plt.show()
        for i in range(1):
            plt.figure(i+2)
            colors = (0,0,0)
            area = numpy.pi*3
            plt.scatter(self.coloumn(analyze_list,0),self.totalcoloumn(analyze_list),s=area, c=colors, alpha=0.7)
            plt.xlabel("Initial cycle length")
            plt.ylabel("Total pain Score")
            plt.title("Pain variation with initial cycle length")
            plt.yticks(numpy.arange(1,1500,100))
            plt.savefig("Pain Initial cycle.png")
            plt.show()"""
        #print self.coloumn(analyze_list,3)
        #print analyze_list[0]
        #print list(user_dict["252"])
inst = pslove()
inst.parseVal()
