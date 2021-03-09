import DataVisualisation as dv

data = dv.readData()
dv.barPriceVsTown(data)

while (True):
    try:
        choice = int(input("Select 1 for barPriceVsTown, 2 for barPriceVsFlatType, 3 for pointPriceVsYear, 4 to exit: "))
    except ValueError:
        print ("That was not a valid input, please try again.")
        continue
    if choice == 1:
        dv.barPriceVsTown(data)
    elif choice == 2:
        dv.barPriceVsFlatType(data)
    elif choice == 3:
        dv.pointPriceVsYear(data)
    elif choice == 4:
        break
