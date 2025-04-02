#Script 1: unit_1_units_converter
print("******UNITS CONVERTER******")
print("1 - Lenght\n2 - Area\n3 - Volume\n4 - Mass")
option = int(input("Select an option"))
result = 0 
units = ""

if option == 1:
    print("Meters to centimetres")
    datum = float(input("Enter the number of meters: "))
    result = datum * 1E2
    units = "cm"

elif option == 2:
    print("Square Meters to square kilometres")
    datum = float(input("Enter the number of square meters "))
    result = datum * 1E-6
    units = "kmE2"

elif option == 3:
    print("Cubic Meters to cubic milimeters")
    datum = float(input("Enter the number of cubic meters: "))
    result = datum * 1E9
    units = "mmE3"

elif option == 4:
    print("Decigrams to kilograms")
    datum = float(input("Enter the nmber of decigrams: "))
    result = datum * 1E-4
    units = "dg"
else:
    print("Choose a valid option")

print(f"The result of the conversion is: {result:.3E} {units}")


    


