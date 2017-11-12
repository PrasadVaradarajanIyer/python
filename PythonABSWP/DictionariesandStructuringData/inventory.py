#Program to find out all the items in the inventory and their number

import pprint
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def totalInventory(inventoryList):
	totalNumberofItems = 0
	for k, v in inventoryList.items():
		totalNumberofItems = totalNumberofItems + v
		pprint.pprint(str(v) + ' ' +  k)
	return totalNumberofItems

print('Inventory: ')
print('Total Number of items: ' + str(totalInventory(inventory)))
