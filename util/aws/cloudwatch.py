# coding: utf-8
import boto3
import datetime


def create_client():
    """
    CloudWatch クライアント作成

    Returns
    -------
    client : boto3.client
        CloudWatch クライアント
    """
    client = boto3.client('cloudwatch')
    return client


def create_metric(metricname, dimensions, value):
    """
    メトリクスデータの作成

    Parameters
    -------
    metricname : str
        メトリクス名
    dimensions : list
        メトリクス属性
    value : number
        メトリクス値
    """
    metric_data = {
        'MetricName': metricname,
        'Dimensions': dimensions,
        'Timestamp': datetime.datetime.now(),
        'Value': value
    }
    return metric_data


def put_metrics(client, namespace, metricsdata):
    """
    CloudWatchにメトリクスを出力する

    Parameters
    -------
    client : boto3.client
        CloudWatchクライアント
    namespace : str
        名前空間
    metricsdata : list
        出力メトリクス
    """
    response = client.put_metric_data(
        Namespace=namespace, MetricData=metricsdata)
    return response
