# UIMT-VAN-SORTER
Orders and sorts people into x different vans. More info available on README. 

Given a dictionary with people's names as keys, and their designation as 'driver' or 'non-Driver' as their values. 
Program should iterate through and return the number of vans (which should be an input), taking into account the number of drivers that are needed. This should reutrn a dictionary stating {1: d1, d2, p1, p2, p3} where d=driver, and p=passenger. 

Then the program should write this returned dictionary in a excel spreadsheet, where the first row should just state Van 1, Van 2, all the way to the number of vans needed. 
Then vertically from each van number, should be the list of names, the driver names should come first and be bolded and the passengers (ie people who can't drive). Then close the file. 

If there is any errors such as not enough drivers for every van, or not enough vans for everyone, then the program should print out appropriate messages. 
