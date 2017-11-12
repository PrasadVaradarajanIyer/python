#This program adds up all the items in the list and displays the total items using dictionary and lisst in the same program

def addToInventory(inventory, addedItem):
	for i in range(len(addedItem)):
		inventory.setdefault(addedItem[i], 0)
		inventory[addedItem[i]]+=1
	return inventory
			


def displayInventory(inventoryList):
        totalNumberofItems = 0
	print('Inventory: ')
        for k, v in inventoryList.items():
                totalNumberofItems = totalNumberofItems + v
                print(str(v) + ' ' +  k)
	print('Total number of items in the inventory are: ' + str(totalNumberofItems))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
