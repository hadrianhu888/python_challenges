SalesDictionary = {"John" : {"N": 3056, "S":8463, "E": 8441, "W": 2694}, "Tom":{"N": 4832, "S":6786, "E": 4737, "W": 3612},"Anne":{"N": 5239, "S":4802, "E": 5820, "W": 1859},"Fiona":{"N": 3904, "S":3645, "E": 8821, "W": 2451}}
print(SalesDictionary)
name = input("Enter a name: ")
region = input("Enter a region: ")
print("\n\nThe data for the person " + name + " in region " + region + " is: \n\n")
if ((name in SalesDictionary) and (region in SalesDictionary[name])):
    print(SalesDictionary[name][region])
changeSalesOption = input("Would you like to change the sales figure? [y/n]")
if (changeSalesOption.lower() =='y'): 
    changeSalesFigure = int(input("Please change the Sales figure for this region: "))
    SalesDictionary[name][region] = changeSalesFigure
    #print out the name and region information:
    print("\n\nThe newly updated sales figures are: \n\n")
    print(SalesDictionary[name])
elif (changeSalesOption.lower() == 'n'):
    print("\n\nThe newly updated sales figures are: \n\n")
    print(SalesDictionary[name])
else:
    print(SalesDictionary[name])