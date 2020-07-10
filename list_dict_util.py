import json

class DistUtil:
    def __init__(self):
        pass

    def parse_white_list(self, whiteList):
        procWhiteList = []
        for string in whiteList:
            # Declaring base case
            parentDict = None
            unwrap = True
            nameToWL = None

            stringArr = string.split('#')
            typeOfWhiteList = len(stringArr)

            if typeOfWhiteList == 1:
                nameToWL = stringArr[0]
            elif typeOfWhiteList == 2:
                if stringArr[1] == "":
                    unwrap = False
                    nameToWL = stringArr[0]
                else:
                    parentDict = stringArr[0]
                    nameToWL = stringArr[1]
            else:
                unwrap = False
                parentDict = stringArr[0]
                nameToWL = stringArr[1]

            procWhiteList.append({"nameToWL": nameToWL, "parentDict": parentDict, "unwrap": unwrap})
        return procWhiteList

    def filter_name_inner(self, obj, whiteList, parentDict):
        if isinstance(obj, list):  # obj must be list
            for listEntry in obj:
                self.filter_name_inner(listEntry, whiteList, parentDict)

        elif isinstance(obj, dict):  # obj must be dict
            toDelete = []
            for dictKey in obj.keys():
                keep = False
                unwrap = True
                for WLEntry in whiteList:
                    if dictKey == WLEntry["nameToWL"] and parentDict == str(WLEntry["parentDict"]):
                        keep = True
                        unwrap = WLEntry["unwrap"]
                if keep is False:
                    toDelete.append(dictKey)
                elif unwrap:
                    self.filter_name_inner(obj[dictKey], whiteList, dictKey)
            for keyToDelete in toDelete:
                del obj[keyToDelete]

        return obj

    def filter_name(self, obj, whiteList):
        parentDict = "None"
        parsedWhiteList = self.parse_white_list(whiteList)
        # print(json.dumps(obj, indent=4))
        print(json.dumps(parsedWhiteList, indent=4))
        return self.filter_name_inner(obj, parsedWhiteList, parentDict)



    # def filter_name_inner(self, obj, whiteList):
    #     if isinstance(obj, list):  # obj must be list
    #         for listEntry in obj:
    #             self.filter_name_inner(listEntry, whiteList)

    #     elif isinstance(obj, dict):  # obj must be dict
    #         for key in [key for key in list(obj.keys()) if key not in whiteList]:
    #             del obj[key]
    #         for key in list(obj.keys()):
    #             if whiteList[key] == 0:
    #                 del whitelist[key]
    #                 self.filter_name_inner(obj.get(key), whiteList)
    #     return obj

    # def filter_name(self, obj, whiteList):
    #     return self.filter_name_inner(obj, whiteList)




    def key_change(self, obj, keysToChange):
        jsoned = json.dumps(obj)
        for keyPair in keysToChange.items():
            jsoned = jsoned.replace(keyPair[0], keyPair[1])
        return json.loads(jsoned)

    # def filter_name_inner(self, obj, whiteList):
    #     if isinstance(obj, list):  # obj must be list
    #         for listEntry in obj:
    #             self.filter_name_inner(listEntry, whiteList)

    #     elif isinstance(obj, dict):  # obj must be dict
    #         for key in [key for key in list(obj.keys()) if key not in whiteList]:
    #             del obj[key]
    #         for key in list(obj.keys()):
    #             if whiteList[key] == 0:
    #               del whitelist[key]
    #                 self.filter_name_inner(obj.get(key), whiteList)
    #     return obj

    # def filter_name(self, obj, whiteList):
    #     return self.filter_name_inner(obj, whiteList)

    def find_value_diffkey_inner(self, obj, oldKey, oldValue, newKey, newValue):
        if isinstance(obj, list):  # obj must be list
            for listEntry in obj:
                newValue = self.find_value_diffkey_inner(
                    listEntry, oldKey, oldValue, newKey, newValue
                )
        elif isinstance(obj, dict):
            if oldKey in obj and oldValue == obj.get(oldKey):
                newValue = obj.get(newKey)
            else:
                for key in list(obj.keys()):
                    newValue = self.find_value_diffkey_inner(
                        obj.get(key), oldKey, oldValue, newKey, newValue
                    )
        return newValue

    def find_value_samekey_inner(self, obj, oldKey, final):
        if isinstance(obj, list):  # obj must be list
            lambda listEntry: self.find_value_samekey_inner(listEntry, oldKey, final), (listEntry for listEntry in obj)

        elif isinstance(obj, dict):
            if oldKey in obj:
                final.append(obj.get(oldKey))
            else:
                lambda key: self.find_value_samekey_inner(obj.get(key), oldKey, final), (key for key in obj)
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

    # schemaTest1 = {
    # 'id': 0,
    # 'name': 0,
    # 'otherField': 0
    # 'newName': 0
    # }

    # schemaTest2 = [
    # 'id',
    # 'otherField#',
    # 'name#innerName',
    # 'newName'
    # ]

    testObj = [
    {
        "name": "john",
        "class": {
            "name": "3A",
            "numberOfStudents": 10,
            "role": None
        },
        "friends": [
        {
            "name": "sam",
            "id": 10
        },
        {
            "name": "susan",
            "id": 20
        }],
        "location": {
            "name": "NP",
            "time": "morning",
            "id": 1
        }
    },
    {
        "name": "mary",
        "class": {
            "name": "4A",
            "numberOfStudents": 10,
            "role": ["prefect", "librarian"]
        },
        "friends": ["name4", "name5", "name6"],
        "location": {
            "name": "SSP",
            "time": "afternoon",
            "id": 2
        }

    },
    {
        "name": "jack",
        "class": {
            "name": "5",
            "numberOfStudents": 10,
            "role": "librarian"
        },
        "friends": "name7",
        "location": {
            "name": "MK",
            "time": "evening",
            "id": 3
        }
    }]

    schema = [
        "class#",
        "friends",
        "friends#name",
        "location",
        "location#name",
        "location#id"
    ]

    # ParentDirectory#Name#

    du = DistUtil()
    print(json.dumps(du.filter_name(testObj, schema), indent=4))
    # To get all values for key: [d["nameToWL"] for d in whiteList]



if __name__ == "__main__":
    main()

                
