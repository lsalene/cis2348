# Leira Salene 1785752

import csv
from operator import itemgetter

manl = []
pricel = []
sdl = []

with open("ManufacturerList.csv", "r") as manlist:
    man = csv.reader(manlist)
    for line in man:
        manl.append(line)

with open("PriceList.csv", "r") as pricelist:
    price = csv.reader(pricelist)
    for line in price:
        pricel.append(line)

with open("ServiceDatesList.csv", "r") as sdlist:
    sd = csv.reader(sdlist)
    for line in sd:
        sdl.append(line)

new_manl = (sorted(manl, key = itemgetter(0)))
new_pricel = (sorted(pricel, key = itemgetter(0)))
new_sdl = (sorted(sdl, key = itemgetter(0)))

for x in range (0, len(new_manl)):
    new_manl[x].append(pricel[x][1])

for x in range (0, len(new_manl)):
    new_manl[x].append(sdl[x][1])

final_list = new_manl

full_inv = (sorted(final_list, key = itemgetter(1)))

with open("FullInventory.csv", "w") as newfile:
    fw = csv.writer(newfile)

    for x in range (0, len(full_inv)):
        fw.writerow(full_inv[x])

type = final_list
tower = []
laptop = []
phone = []

for x in range (0, len(type)):
    if type[x][2] == "tower":
        tower.append(type[x])
    elif type[x][2] == "phone":
        phone.append(type[x])
    elif type[x][2] == "laptop":
        laptop.append(type[x])

with open("LaptopInventory.csv", "w") as newfile:
    lw = csv.writer(newfile)

    for x in range  (0, len(laptop)):
        lw.writerow(laptop[x])

with open("PhoneInventory.csv", "w") as newfile:
    pw = csv.writer(newfile)

    for x in range(0, len(phone)):
        pw.writerow(phone[x])

with open("TowerInventory.csv", "w") as newfile:
    tw = csv.writer(newfile)

    for x in range(0, len(tower)):
        tw.writerow(tower[x])

damaged = []

for x in range (0, len(type)):
    if type[x][3] == "damaged":
        damaged.append(type[x])

damaged = (sorted(damaged, key = itemgetter(4), reverse = True))

with open("DamagedInventory.csv", "w") as newfile:
    dw = csv.writer(newfile)

    for x in range (0, len(damaged)):
        dw.writerow(damaged[x])

user_man = str(input("Enter manufacturer: "))
user_type = str(input("Enter item type: "))
item = []

while (user_man != "q"):
    for x in range (0, len(final_list)):
        if user_man in final_list[x] and user_type in final_list[x]:
            item.append(final_list[x])

    if len(item) != 0:
        item = sorted(item, key = itemgetter(4), reverse = True)
        print("Your item is: ", item[0])
    else:
        print("No such item in inventory")

user_man = str(input("Enter manufacturer or q to exit: "))
user_type = str(input("Enter item type: "))