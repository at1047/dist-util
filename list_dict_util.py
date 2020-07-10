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

    def key_change(self, obj, keysToChange):
        jsoned = json.dumps(obj)
        for keyPair in keysToChange.items():
            jsoned = jsoned.replace(keyPair[0], keyPair[1])
        return json.loads(jsoned)

        #TODO: Stop errors when a value is equal to an old key


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
            return self.find_value_diffkey_inner(obj, oldKey, oldValue, newKey, final)
