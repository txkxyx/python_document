
# -*- coding:utf-8 -*-


def json_csv_body(dict_obj):
    text = ''
    for v in dict_obj.values():
        text = text + str(v) + ','
    return text + '\n'


def json_csv_header(dict_obj):
    text = ''
    for k in dict_obj.keys():
        text = text + str(k) + ','
    return text + '\n'


def jsonlist_csv(json_list):
    text = ''
    for i, v in enumerate(json_list):
        if i == 0:
            text = text + json_csv_header(v)
        text = text + json_csv_body(v)
    return text + '\n'


def jsonlist_csvfile(file_name, json_list):
    with open(file_name, 'w') as f:
        text = jsonlist_csv(json_list)
        f.write(text)
