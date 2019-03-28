# -*- coding:utf-8 -*-
import boto3
from boto3.dynamodb.conditions import Key, Attr


def get_all_items(table):
    """
    指定したテーブルのすべてのデータを取得する

    Parameters
    -------
    table : str
        テーブル名

    Returns
    -------
    result : list
        検索結果
    """
    table = create_obj(table)
    result = table.scan()
    if 'Items' in result:
        return result['Items']
    else:
        return None


def put_item(table, p_key, p_value, s_key=None, s_value=None, others=dict()):
    """
    指定したテーブルにデータを格納する

    Parameters
    -------
    table : str
        テーブル名
    p_key : str
        プライマリーキー
    p_value : str
        プライマリーキーの値
    s_key : str
        ソートキー
    s_key : str
        ソートキーの値
    others : dict
        キー以外の値
    """
    table = create_obj(table)
    item = create_item(p_key, p_value, s_key, s_value)
    for k, v in others.items():
        item[k] = v
    table.put_item(Item=item)


def delete_item(table, p_key, p_value, s_key=None, s_value=None):
    """
    指定したテーブルの、指定したキーのデータを削除する

    Parameters
    -------
     table : str
        テーブル名
    p_key : str
        プライマリーキー
    p_value : str
        プライマリーキーの値
    s_key : str
        ソートキー
    s_key : str
        ソートキーの値
    """
    table = create_obj(table)
    item = create_item(p_key, p_value, s_key, s_value)
    table.delete_item(Key=item)


def get_item(table, p_key, p_value, s_key, s_value):
    """
    指定したテーブルからデータを取得する

    Parameters
    -------
     table : str
        テーブル名
    p_key : str
        プライマリーキー
    p_value : str
        プライマリーキーの値
    s_key : str
        ソートキー
    s_key : str
        ソートキーの値

    Returns
    -------
    result : list
        検索結果
    """
    table = create_obj(table)
    item = create_item(p_key, p_value, s_key, s_value)
    result = table.get_item(Key=item)
    if 'Item' in result:
        return result['Item']
    else:
        return None


def create_obj(table_name):
    """
    テーブルオブジェクトを作成する

    Parameters
    -------
    table_name : str
        テーブル名

    Returns
    -------
    table : 
        テーブルオブジェクト
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(str(table_name))
    return table


def create_item(p_key, p_value, s_key, s_value):
    """
    プライマリとソートのItemを作成する

    Parameters
    -------
    p_key : str
        プライマリーキー
    p_value : str
        プライマリーキーの値
    s_key : str
        ソートキー
    s_key : str
        ソートキーの値

    Returns
    -------
    item : dict
        辞書型
    """
    item = {str(p_key): p_value}
    if s_key is not None:
        item[str(s_key)] = s_value
    return item
