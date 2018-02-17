# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:36:06 2018

@author: gizmo
"""
import os
import csv
csvpath1 = os.path.join('budget_data_1.csv')
csvpath2 = os.path.join('budget_data_2.csv')

with open(csvpath1,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) #this skips the header first row
    count1 = 0
    totalrev1 = 0
    revenue1 = []
    date1 = []
    for row in csvreader:
        revenue1.append(int(row[1])) #putting all revnue in list
        count1 +=1 #number of months - new month per row
        totalrev1+=int(row[1]) #total revenue -summing up
        date1.append(row[0])
    

max1 = max(revenue1)
min1 = min(revenue1)

#find the date corresponding to the max and min
for k in range(len(revenue1)):
    if revenue1[k]==max1:
        datemax1 = date1[k]
    elif revenue1[k]==min1:
        datemin1 = date1[k]

with open(csvpath2,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) #this skips the header first row
    count2 = 0
    totalrev2 = 0
    revenue2 = []
    date2 = []
    for row in csvreader:
        revenue2.append(int(row[1])) #putting all revnue in list
        count2 +=1 #number of months - new month per row
        totalrev2+=int(row[1]) #total revenue -summing up
        date2.append(row[0])
        
max2 = max(revenue2)
min2 = min(revenue2)

for l in range(len(revenue2)):
    if revenue2[l]==max2:
        datemax2 = date2[l]
    elif revenue2[l]==min2:
        datemin2 = date2[l]
        
    
totalavg = round((totalrev2+totalrev1)/(count1+count2),2)#average revenue for both
totalmonth = count1+count2
#average revenue change is not the same as average revenue
#summing the differences

differences1 = []

for i in range(len(revenue1)):
    if i < (len(revenue1)-1):
        differences1.append(revenue1[i+1]-revenue1[i])

differences2 = []

for j in range(len(revenue2)):
    if j < (len(revenue2)-1):
        differences2.append(revenue2[i+1]-revenue2[i])
        
#taking the average of the differences

totalavgchge = round((sum(differences1)+sum(differences2))/(len(differences1)+len(differences2)),2)


##print out the results    
print("Financial Analysis")  
print("----------------------")
print("Total Months (in both data sets): " +str(totalmonth))
print("Average Revenue: $"+str(totalavg))
print("Average Revenue Change: $"+str(totalavgchge))

if max(max1,max2)==max1:
    print("Greatest Increase in Revenue: " + datemax1 + " $" + str(max1))
elif max(max1,max2)==max2:
    print("Greatest Increase in Revenue: "+datemax2 + " $" +str(max2))
 
if min(min1,min2)==min1:
    print("Greatest Decrease in Revenue: " + datemin1 + " $" +str(min1))
elif min(min1,min2)==min2:
    print("Greatest Decrease in Revenue: " +datemin2 + " $" +str(min2))

##write results to file
    
output_path = os.path.join('Results','output.txt')

with open(output_path,'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months (in both data sets): " +str(totalmonth)+"\n")
    txtfile.write("Average Revenue: $"+str(totalavg)+"\n")
    txtfile.write("Average Revenue Change: $"+str(totalavgchge) +"\n")
    if max(max1,max2)==max1:
        txtfile.write("Greatest Increase in Revenue: " + datemax1 + " $" + str(max1) +"\n")
    elif max(max1,max2)==max2:
        txtfile.write("Greatest Increase in Revenue: "+datemax2 + " $" +str(max2) + "\n")
    if min(min1,min2)==min1:
        txtfile.write("Greatest Decrease in Revenue: " + datemin1 + " $" +str(min1) + "\n")
    elif min(min1,min2)==min2:
        txtfile.write("Greatest Decrease in Revenue: " +datemin2 + " $" +str(min2) + "\n")
    