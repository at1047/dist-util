import json


class DistUtil():
	def __init__(self):
		pass

	def key_change_helper(self, obj, keysToChange):
		if isinstance(obj, list):
			for dictEntry in obj:
				self.key_change_helper(dictEntry, keysToChange)

		elif isinstance(obj, dict):
			for key in list(obj.keys()):
				for keyPair in keysToChange.items():
					if key == keyPair[0]:
						obj[keyPair[1]] = obj.pop(key)
					else:
						if isinstance(obj.get(key), (dict, list)):
							self.key_change_helper(obj[key], keysToChange)
		return obj

	def key_change(self, obj, keysToChange):
		"""Changes specified key
		
		Args:
		    obj ([list, dict]): List or dict to be edited
		    keysToChange (dict): key name pair to be changed
		
		Returns:
		    TYPE: [list, dict]
		"""
		return self.key_change_helper(obj, keysToChange)

	def filter_name_helper(self, obj, whiteList):
		if isinstance(obj, list): # obj must be list
			for listEntry in obj:
				self.filter_name_helper(listEntry, whiteList)

		elif isinstance(obj, dict): # obj must be dict
			for key in [key for key in list(obj.keys()) if key not in whiteList]:
				del obj[key]
			for key in list(obj.keys()):
				self.filter_name_helper(obj.get(key), whiteList)
				
		return obj

	def filter_name(self, obj, whiteList):
		"""Filters based on white list
		
		Args:
		    obj ([list, dict]): List or dict to be edited
		    whiteList (list): List of keys to be white listed
		
		Returns:
		    TYPE: [list, dict]
		"""
		return self.filter_name_helper(obj, whiteList)

# class ListMerger():
# 	def __init__(self, listA, listB, fieldA="id", fieldB=None):
# 		self.listA = listA
# 		self.listB = listB
# 		self.fieldA = fieldA
# 		if fieldB == None:
# 			self.fieldB = fieldA
# 		else:
# 			self.fieldB = fieldB

# 	def mergeId(self):
# 		newList = []
# 		for a in self.listA:

# 			b = next((item for item in self.listB if item[self.fieldB] == a[self.fieldA]), None)

# 			newData = {self.fieldA: a.pop(self.fieldA)}
# 			for key in a:
# 				newData[key] = a[key]

# 			for key in b:
# 				if key != self.fieldB:
# 					newData[key] = b[key]
# 			newList.append(newData)
# 		return newList



# Use main() for testing cases

def main():

	# whiteList = ["id", "otherField", "newName", "otherName"]

	# listA = [{
	#             "id": 1,
	#             "name": "first",
	#             "otherField": [{
	#             	"newName": "name3",
	#             	"name": "second"
	#             },
	#             {
	#             	"otherName": "otherName1"
	#             }]
	            
	#         },
	#         {
	#             "id": 2,
	#             "name": "second",
	#             "otherField": [{
	#             	"newName": "name4",
	#             	"name": "second"
	#             }]
	#         },
	#         {
	#             "id": 3,
	#             "name": "second",
	#             "otherField": [{
	#             	"newName": "name4",
	#             	"name": "second"
	#             }]
	#         }
	#     ]

	# listA = {
	#             "id": 1,
	#             "name": "first",
	#             "otherField": [{
	#             	"newName": "name3"
	#             }]
	            
	#         }


	# listB = [
	#         {
	#             "id": 2,
	#             "somefield": "random2"
	#         },
	#         {
	#             "id": 1,
	#             "somefield": "random1"
	#         }
	# ]
	
	distUtil = DistUtil()
	print(json.dumps(distUtil.filter_name(listA, whiteList)))

if __name__ == "__main__":
    main()

				