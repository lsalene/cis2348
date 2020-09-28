##Leira Salene 1785752

lemon_juice = float (input('Enter amount of lemon juice (in cups):'))
water = float (input('\nEnter amount of water (in cups):'))
agave_nectar = float (input('\nEnter amount of agave nectar (in cups):'))
serving = float (input('\nHow many servings does this make?'))
print()

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(serving))+' servings')
print(str('{:.2f}'.format(lemon_juice)) + ' cup(s) lemon juice')
print(str('{:.2f}'.format(water)) + ' cup(s) water')
print(str('{:.2f}'.format(agave_nectar)) + ' cup(s) agave nectar')
print()

new_serving = float (input('How many servings would you like to make?'))
print()
x = new_serving/serving
new_lemon_juice = lemon_juice * x
new_water = water * x
new_agave_nectar = agave_nectar * x

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice)) + ' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water)) + ' cup(s) water')
print(str('{:.2f}'.format(new_agave_nectar)) + ' cup(s) agave nectar')
print()

print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice/16)) + ' gallon(s) lemon juice')
print(str('{:.2f}'.format(new_water/16)) + ' gallon(s) water')
print(str('{:.2f}'.format(new_agave_nectar/16)) + ' gallon(s) agave nectar')
