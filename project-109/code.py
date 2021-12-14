import plotly.express as px
import statistics 
import pandas as pd
import csv
df=pd.read_csv("StudentsPerformance.csv")
MSList=df["mathscore"].to_list()
RSList=df["readingscore"].to_list()
WSList=df["writingscore"].to_list()

MSMean=statistics.mean(MSList)
MSMedian=statistics.median(MSList)
MSMode=statistics.mode(MSList)
standerdDiviationMS = statistics.stdev(MSList)
RSMean=statistics.mean(RSList)
RSMedian=statistics.median(RSList)
RSMode=statistics.mode(RSList)
standerdDiviationRS = statistics.stdev(RSList)
WSMean=statistics.mean(WSList)
WSMedian=statistics.median(WSList)
WSMode=statistics.mode(WSList)
standerdDiviationWS = statistics.stdev(WSList)
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(MSMean, MSMedian, MSMode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(RSMean, RSMedian, RSMode))
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(WSMean, WSMedian, WSMode))

fSMMStart = MSMean-standerdDiviationMS
fSMMEnd = MSMean+standerdDiviationMS
sSMMStart = MSMean-2*standerdDiviationMS
sSMMEnd = MSMean+2*standerdDiviationMS
tSMMStart = MSMean-3*standerdDiviationMS
tSMMEnd = MSMean+3*standerdDiviationMS
list_of_data_within_1_std_deviation = [result for result in MSList if result > fSMMStart and result < fSMMEnd]
list_of_data_within_2_std_deviation = [result for result in MSList if result > sSMMStart and result < sSMMEnd]
list_of_data_within_3_std_deviation = [result for result in MSList if result > tSMMStart and result < tSMMEnd]
m1 = len(list_of_data_within_1_std_deviation)*100.0/len(MSList)
m2 = len(list_of_data_within_2_std_deviation)*100.0/len(MSList)
m3 = len(list_of_data_within_3_std_deviation)*100.0/len(MSList)
fSMRStart = MSMean-standerdDiviationRS
fSMREnd = MSMean+standerdDiviationRS
sSMRStart = MSMean-2*standerdDiviationRS
sSMREnd = MSMean+2*standerdDiviationRS
tSMRStart = MSMean-3*standerdDiviationRS
tSMREnd = MSMean+3*standerdDiviationRS
list_of_data_within_1_std_deviation = [result for result in RSList if result > fSMRStart and result < fSMREnd]
list_of_data_within_2_std_deviation = [result for result in RSList if result > sSMRStart and result < sSMREnd]
list_of_data_within_3_std_deviation = [result for result in RSList if result > tSMRStart and result < tSMREnd]
r1 = len(list_of_data_within_1_std_deviation)*100.0/len(RSList)
r2 = len(list_of_data_within_2_std_deviation)*100.0/len(RSList)
r3 = len(list_of_data_within_3_std_deviation)*100.0/len(RSList)
fSMWStart = MSMean-standerdDiviationRS
fSMWEnd = WSMean+standerdDiviationWS
sSMWStart = WSMean-2*standerdDiviationWS
sSMWEnd = WSMean+2*standerdDiviationWS
tSMWStart = WSMean-3*standerdDiviationWS
tSMWEnd = WSMean+3*standerdDiviationWS
list_of_data_within_1_std_deviation = [result for result in WSList if result > fSMWStart and result < fSMWEnd]
list_of_data_within_2_std_deviation = [result for result in WSList if result > sSMWStart and result < sSMWEnd]
list_of_data_within_3_std_deviation = [result for result in WSList if result > tSMWStart and result < tSMWEnd]
w1 = len(list_of_data_within_1_std_deviation)*100.0/len(WSList)
w2 = len(list_of_data_within_2_std_deviation)*100.0/len(WSList)
w3 = len(list_of_data_within_3_std_deviation)*100.0/len(WSList)
print(m1,m2,m3)
print(r1,r2,r3)
print(w1,w2,w3)


