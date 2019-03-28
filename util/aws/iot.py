# coding: utf-8
import boto3


def matt_publish(topic, qos, payload):
    # MQTTクライアントの作成
    iot = boto3.client('iot-data')
    # メッセージをPublish
    iot.publish(topic=topic, qos=qos, payload=payload)
