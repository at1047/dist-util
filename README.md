#list_dict_util
Utilities for manipulating lists and dictionaries in python, especially from json.loads()

- Initialising

from list_dict_util import DistUtil 
du = DistUtil()


##functions
- Filter by name (filter_name)

**du.filter_name(obj: [list, dict], schema: [String])**

schema items follow the format of "{parent_directory}#{name}, 
where parent_directory is the parent of the key you want to whitelist (None if top layer)
Add # to the end of string if you do not wish to recurse into the key's value (ex. "parent_directory#name#")

Sample schema:
[
    "class#",
    "friends",
    "friends#name",
    "location",
    "location#name",
    "location#id"
]

- Change keys (key_change)

**du.key_change(obj: [list, dict], keysToChange: list)**

keysToChange follows the format of:
[{"old_key1": "new_key1"}, {old_key2}: {new_key2}, ...]

TODO: Errors when value is equal to an old key

- Find the value of a specific key (find_value)

Has two functions depending on number of inputs

**u.find_value(obj: [list, dict], key: String):**

returns a list of values with the matching key from obj

**return du.find_value(obj: [list, dict], oldKey: String, oldValue=None: String, newKey=None: String):**

returns a value of the value from newKey inside the dictionary that contains the key value pair of oldKey: oldValue