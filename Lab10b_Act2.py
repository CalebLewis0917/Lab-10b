# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab10b_Act1
# Date:         11 14 2021

import numpy as np
import matplotlib.pyplot as plt
file1 = open("CLLWeatherData.csv","r")
file_list = []
x = 1
x_list = []

for next_line in file1:
    day = next_line.strip("\n").split(",")
    file_list.append(day)

file_list = file_list[1:]

######PART A#####
ave_wind_list = []
ave_temp_list = []
fig = plt.figure()
ax = fig.add_subplot()
for i in file_list:
    ave_wind_list.append(float(i[1]))
    ave_temp_list.append(int(i[3]))
    x_list += [x]
    x += 1
plt.title("Average Temperature and Wind Speed")
ax.set_xlabel("Date")
ax.set_ylabel("Average Temperature (F)")
ax.plot(x_list,ave_temp_list,'r-')
ax2 = ax.twinx()
ax2.set_ylabel("Average Wind Speed (mph)")
ax2.plot(x_list,ave_wind_list,'b-')
plt.show()

#####PART B#####
prec_list = []
for i in file_list:
    if(i[2]!='0'):
        prec_list.append(float(i[2]))
plt.hist(prec_list,bins=50)
plt.title("Histogram of Precipitation")
plt.xlabel("Precipitation (in)")
plt.ylabel("Number of Days")
plt.show()

#####PART C#####
min_temp_list = []
for i in file_list:
    min_temp_list.append(float(i[5]))
plt.scatter(min_temp_list,ave_wind_list)
plt.title("Average Wind Speed vs. Minimum Temperature")
plt.xlabel("Minimum Temperature (F)")
plt.ylabel("Average Wind Speed (mph)")
plt.show()

#####PART D#####
month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
jan_list = []
feb_list = []
mar_list = []
apr_list = []
may_list = []
jun_list = []
jul_list = []
aug_list = []
sep_list = []
oct_list = []
nov_list = []
dec_list = []
ave_list = []
max_list = []
min_list = []
abs_ave_list = []
abs_max_list = []
abs_min_list = []
for i in file_list:
    date = i[0].split("/")
    if(date[0]=='1'):
        jan_list.append(i)
    elif(date[0]=='2'):
        feb_list.append(i)
    elif(date[0]=='3'):
        mar_list.append(i)
    elif(date[0]=='4'):
        apr_list.append(i)
    elif(date[0]=='5'):
        may_list.append(i)
    elif(date[0]=='6'):
        jun_list.append(i)
    elif(date[0]=='7'):
        jul_list.append(i)
    elif(date[0]=='8'):
        aug_list.append(i)
    elif(date[0]=='9'):
        sep_list.append(i)
    elif(date[0]=='10'):
        oct_list.append(i)
    elif(date[0]=='11'):
        nov_list.append(i)
    elif(date[0]=='12'):
        dec_list.append(i)
for i in jan_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in feb_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in mar_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in apr_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in may_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in jun_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in jul_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in aug_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in sep_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in oct_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in nov_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []
for i in dec_list:
    ave_list.append(float(i[3]))
    max_list.append(float(i[4]))
    min_list.append(float(i[5]))
abs_ave_list.append(sum(ave_list)/len(ave_list))
abs_max_list.append(max(max_list))
abs_min_list.append(min(min_list))
ave_list = []
max_list = []
min_list = []

plt.plot(month_list,abs_min_list,'b-',month_list,abs_max_list,'r-')
plt.bar(month_list,abs_ave_list,color='y')
plt.legend(labels=["Low T","High T"])
plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature (F)")
plt.show()