# -*- coding: utf-8 -*-
import serialize


class MainClass(serialize.JsonSerializer):
    def __init__(self):
        self.string = ''
        self.integer = 0
        self.float = 0.0
        self.subclass = SubClass()
        self.array = []
        self.dictionary = {}


class SubClass(serialize.JsonSerializer):
    def __init__(self):
        self.string = ''
        self.integer = 0
        self.float = 0.0


if __name__ == '__main__':
    json_str = """
    {
        "string":"string",
        "integer":10,
        "float":1.1,
        "subclass":{
            "string":"string",
            "integer":10,
            "float":1.1
        },
        "array":[1,2,3,"a","b","c"
        ],
        "dictionary":{
            "a":"a",
            "b":"b",
            "c":"c"
        }
    } """

    main = MainClass()
    main.serialize(json_str)
