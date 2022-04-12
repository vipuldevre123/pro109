import pandas as pd
import statistics

df=pd.read_csv("data.csv")
studentlist=df['reading score'].to_list()

#mean of height
studentmean=statistics.mean(studentlist)
studentmedian=statistics.median(studentlist)

print("mean=",studentmean)
print("median=",studentmedian)

studentsd=statistics.stdev(studentlist)
print(studentsd)

studentfsds,studentfsde=studentmean-studentsd,studentmean+studentsd
studentssds,studentssde=studentmean-(2*studentsd),studentmean+(2*studentsd)
studenttsds,studenttsde=studentmean-(3*studentsd),studentmean+(3*studentsd)

studentdatainfsd=[result for result in studentlist if result>studentfsds and result<studentfsde]
studentdatainssd=[result for result in studentlist if result>studentssds and result<studentssde]
studentdataintsd=[result for result in studentlist if result>studenttsds and result<studenttsde]

print("{}% of data for student lies whithin first standard division".format(len(studentdatainfsd)*100.0/len(studentlist)))
print("{}% of data for student lies whithin second standard division".format(len(studentdatainssd)*100.0/len(studentlist)))
print("{}% of data for student lies whithin third standard division".format(len(studentdataintsd)*100.0/len(studentlist)))
