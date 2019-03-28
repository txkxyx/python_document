# -*- coding: utf-8 -*-
import sys
import json


class JsonSerializer(object):

    # jsonからシリアライズ
    def serialize(self, str_json):
        # Dict型に変換
        try:
            if isinstance(str_json, str):
                json_obj = json.loads(str_json)
        except json.JSONDecodeError as e:
            print(e)
            return False
        except ValueError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

        for key, value in self.__dict__.items():
            if isinstance(getattr(self, key), JsonSerializer):
                obj = getattr(self, key)
                if json_obj[key] is None:
                    setattr(self, key, None)
                else:
                    obj.serialize(json_obj[key])
                    setattr(self, key, obj)
            elif isinstance(getattr(self, key), int):
                # INT型の場合
                if json_obj[key] is None:
                    setattr(self, key, None)
                else:
                    setattr(self, key, int(json_obj[key]))
            elif isinstance(getattr(self, key), float):
                # FLOAT型の場合
                if json_obj[key] is None:
                    setattr(self, key, None)
                else:
                    setattr(self, key, float(json_obj[key]))
            elif isinstance(getattr(self, key), str):
                # str型の場合
                if json_obj[key] is None:
                    setattr(self, key, None)
                else:
                    setattr(self, key, json_obj[key])
            elif isinstance(getattr(self, key), list):
                # LISTの場合
                jsonlist = []
                if json_obj[key] is None:
                    setattr(self, key, None)
                else:
                    for obj in json_obj[key]:
                        jsonlist.append(obj)
                    setattr(self, key, jsonlist)
            else:
                break
    # Jsonを出力

    def ToJson(self):
        jsonDict = self.__ToDictionary()
        if isinstance(jsonDict, type(list())):
            jsonstring = []
            for jd in jsonDict:
                jsonstring.append(json.dumps(jd, ensure_ascii=False))
        else:
            jsonstring = json.dumps(jsonDict, ensure_ascii=False)
        return jsonstring

    # Mapを作成
    def __ToDictionary(self):
        jsonDict = {}
        for key in self.__dict__.keys():
            if isinstance(getattr(self, key), type(list())):
                data_list = [data.__ToDictionary()
                             for data in getattr(self, key)]
                jsonDict.update({key: data_list})
            elif isinstance(getattr(self, key), JsonAdapter):
                jsonDict.update({key: getattr(self, key).__ToDictionary()})
            else:
                jsonDict.update({key: getattr(self, key)})
        return jsonDict
