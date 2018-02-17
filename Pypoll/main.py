# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:16:57 2018
This script is made to run each data set individually
This assumes that election data is for a different election

@author: gizmo
"""
import os
import csv

##Change the following to election_data_2 for those results
csvpath1 = os.path.join('election_data_1.csv')


with open(csvpath1,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) #this skips the header first row
    candidates1 = []
    votes = 0
    for row in csvreader:
        candidates1.append(row[2]) #append all candidattes to a list
        votes+=1 #number of votes
    
    ##what if there are more than 4 candidates in next election?
    
    candidates = list(set(candidates1))
    dictcan = {}
    keys = candidates
    ##create a dictionary, define candidate as keys
    ##set number of votes for each candidate to 0
    for j in keys:
        dictcan[j] = 0
        
    ##check matching between the file and the set    
    for i in range(len(candidates)):
        for each in candidates1:
            if each == candidates[i]:
                dictcan[candidates[i]]+=1
                
output_path = os.path.join('Results','output2.txt')

with open(output_path,'w') as txtfile:
    print("Election Results: ")
    txtfile.write("Election Results: \n")
    print("-------------------")
    txtfile.write("------------------\n")   
    print("Total Votes: "+str(votes))
    txtfile.write("Total Votes: "+str(votes)+"\n")
    print("-------------------")     
    txtfile.write("------------------\n")           
    for i in range(len(dictcan)):
        totvote = dictcan[candidates[i]]
        percvote = round((dictcan[candidates[i]]/votes)*100,0)
        print(candidates[i]+": " +str(percvote) +"% " + "total: "+str(totvote))
        txtfile.write(candidates[i]+": " +str(percvote) +"% " + "total: "+str(totvote)+"\n")
    print("-------------------") 
    txtfile.write("------------------\n")
    print("The Winner is: " +max(dictcan,key=dictcan.get))    
    txtfile.write("The Winner is: " +max(dictcan,key=dictcan.get))  
    
                
            
                
        

    
    
        
