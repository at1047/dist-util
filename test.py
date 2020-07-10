from list_dict_util import DistUtil
import json

def main():

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

                
