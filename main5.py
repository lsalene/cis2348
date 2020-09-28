## Leira Salene 1785752
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

def getCost(s):
    if s == 'Oil change':
        return 35
    if s == 'Tire rotation':
        return 19
    if s == 'Car wash':
        return 7
    if s == 'Car wax':
        return 12

    print ("Davy's auto shop services")
    print ("\nOil change--$35")
    print ("\nTire rotation--$19")
    print ("\nCar wash--$7")
    print ("\nCar wax--$12\n")

first = input ('Select first service:\n')
second = input ('Select second service:\n')
print ("\nDavy's auto shop invoice\n")
one = getCost(first)
two = 0
print ('Service 1: %s, $%d' %(first, one))
if second == '-':
    print ("Service 2: No service")
else:
    two = getCost(second)
    print ("Service 2: %s, $%d" %(second, two))

print("\nTotal: $%d" %(one+two))