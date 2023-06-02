
"""
python = json
dict = object
list, tuple = array
str = string
int, float = number
True = true
False = false
None = null
"""



string_jason = '''{

    "voce" : "pode largar o texto json aqui dentro",
    }

'''


import json
from pprint import pprint
from typing import TypedDict

filme = json.loads(string_jason) # de json para python e dumps , coverte para json
print(filme)


