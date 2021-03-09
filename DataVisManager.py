import DataVisualisation as dv

data = dv.readData()
dv.barPriceVsTown(data)
choice = 1

while (1 <= choice <= 3):
    while type(choice) is not int:
        try:
            choice = int(input("Select 1 for barPriceVsTown, 2 for barPriceVsFlatType, 3 for pointPriceVsYear, 4 to exit: "))
        except ValueError:
            choice = int(input("This was not a valid input please try again: "))
    if choice == 1:
        dv.barPriceVsTown(data)
    elif choice == 2:
        dv.barPriceVsFlatType(data)
    elif choice == 3:
        dv.pointPriceVsYear(data)
    else:
        break