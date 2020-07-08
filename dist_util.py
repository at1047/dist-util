import json

class DistUtil():
	def __init__(self):
		pass

	def key_change(self, obj, keysToChange):
		jsoned = json.dumps(obj)
		for keyPair in keysToChange.items():
			jsoned = jsoned.replace(keyPair[0], keyPair[1])
		return json.loads(jsoned)

	def filter_name_inner(self, obj, whiteList):
		if isinstance(obj, list): # obj must be list
			for listEntry in obj:
				self.filter_name_inner(listEntry, whiteList)

		elif isinstance(obj, dict): # obj must be dict
			for key in [key for key in list(obj.keys()) if key not in whiteList]:
				del obj[key]
			for key in list(obj.keys()):
				if whiteList[key] == 0:
					self.filter_name_inner(obj.get(key), whiteList)
		return obj

	def filter_name(self, obj, whiteList):
		return self.filter_name_inner(obj, whiteList)

	def find_value_diffkey_inner(self, obj, oldKey, value, newKey, final):
		if isinstance(obj, list): # obj must be list
			for listEntry in obj:
				final = self.find_value_diffkey_inner(listEntry, oldKey, value, newKey, final)
		elif isinstance(obj, dict):
			if oldKey in obj and value == obj.get(oldKey):
				final = obj.get(newKey)
			else:
				for key in list(obj.keys()):
					final = self.find_value_diffkey_inner(obj.get(key), oldKey, value, newKey, final)
		return final

	def find_value_samekey_inner(self, obj, oldKey, final):
		if isinstance(obj, list): # obj must be list
			for listEntry in obj:
				final.append(self.find_value_samekey_inner(listEntry, oldKey, final))
		elif isinstance(obj, dict):
			if oldKey in obj:
				final.append(obj.get(oldKey))
			else:
				for key in list(obj.keys()):
					if isinstance(obj.get(key), (dict, list)):
						final.append(self.find_value_samekey_inner(obj.get(key), oldKey, final))
		return final

	def find_value(self, obj, oldKey, value=None, newKey=None):
		final = None
		if value == None and newKey == None:
			final = []
			return self.find_value_samekey_inner(obj, oldKey, final)
		else:
			return self.find_value_diffkey_inner(obj, oldKey, value, newKey, final)

# Use main() for testing cases

def main():

	# whiteList = ["id", "otherField", "newName", "otherName"]

	toChange = {
	'name': 'Name',
	'otherName': 'OTHERNAME'
	}

	listA = [{
	            "id": 1,
	            "name": "name1",
	            "otherField": [{
	            	"newName": "name3",
	            	"name": "first"
	            },
	            {
	            	"otherName": "otherName1"
	            }]
	            
	        },
	        {
	            "id": 2,
	            "name": "name2",
	            "otherField": [{
	            	"newName": "name4",
	            	"name": "second"
	            }]
	        },
	        {
	            "id": 3,
	            "name": "name3",
	            "otherField": [{
	            	"newName": "name4",
	            	"name": "third"
	            }]
	        }
	    ]

	# listA = {
	#             "id": 1,
	#             "name": "first",
	#             "otherField": [{
	#             	"newName": "name3",
	#             	"temp": 1
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
	
	du = DistUtil()
	print(du.key_change(listA, toChange))

if __name__ == "__main__":
    main()

				