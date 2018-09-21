#Mock Trial Van Organizer/Sorter
import random
from datetime import datetime
import xlsxwriter
#import xlsxwriter
def MTVanOrganizer(numofPeople, numofPeoplePerVan, numofVans, minNumofDriversPerVan, mockers): 
    #drivers - dictionary with everyone's naames and their values being whether they are drivers or non drivers. 
    keepGoing=True
    while(keepGoing): 
        #program keeps running until something runs off. 
        vans={} #dictionary that will be returned and later formatted. 
        #going to create a list of names; only names.
        randomizedNames=[] 
        x=[randomizedNames.append(keys) for keys in mockers]
        #print(randomizedNames)
        for n in range(1,numofVans+1): 
            vans[n]={}
            a=0
            while(a<numofPeoplePerVan): 
                name=random.choice(randomizedNames)
                vans[n][name]=mockers[name]
                randomizedNames.remove(name) #taking care of any duplicates. 
                a+=1
        #print(vans)
        #keepGoing=False
        count=0
        #print("minNumofDriversPerVan: " + str(minNumofDriversPerVan))
        for n in vans: 
            count=0
            for m in vans[n]: 
                if(vans[n][m]=="Driver"): 
                    count+=1
                if(count==minNumofDriversPerVan): 
                    keepGoing=False
    print(vans)
    #Now going to write the data into an .xlsx file (excel file)
    
    #Create a workbook and add a workm,m,sheet 
    workbook=xlsxwriter.Workboook() #input filename in paranthesis 
    worksheet=workbook.add_worksheet()
    #add a bold format to use to highlight cells 
    bold=workbook.add_format({'bold':True})
    #writing data headers - van1, van2, van3, van4, etc. 
    for n in vans: 
        a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        worksheet.write(a[n].upper()+n,"Van "+n, bold)
def MTOrganizerTester(): 
    mockers={"Isabelle":"Driver","Abby":"Driver","Adam":"Driver","Albert":"Non-Driver","Audrey":"Driver","Chase":"Driver","Christian":"Non-Driver","Delaney":"Driver","Elanna":"Non-Driver","Elizabeth":"Non-Driver","Ellen":"Non-Driver", "Ellie":"Driver", "Erica":"Non-Driver", "Faith":"Driver", "John":"Non-Driver", "Keilye":"Driver","Kimberley":"Non-Driver","Kristen":"Non-Driver","Maggie":"Driver","Mason":"Driver","Megan":"Driver","Michelle":"Driver","Mikayla":"Driver","Omar":"Non-Driver","Rohan":"Driver","Sarah":"Driver","Serena":"Driver","Sophie":"Non-Driver","Taren":"Driver","Tian":"Non-Driver","Travis":"Non-Driver"}
    MTVanOrganizer(33,5,6,2,mockers)
    