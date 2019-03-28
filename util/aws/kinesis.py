# -*- coding:utf-8 -*-
import boto3


def create_client():
    client = boto3.client('kinesis')


def describe_stream(client, stream_name, limit=100, shard_id=None):
    response = client.describe_stream(
        StreamName=stream_name, Limit=limit, ExclusiveStartShardId=shard_id)
    return response
