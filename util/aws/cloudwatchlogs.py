# coding: utf-8
import datetime
import boto3
from botocore.config import Config


def export_logs(loggroup_name, logstream_name, log):
    """
    CloudWatch Logs出力関数

    Parameters
    -------
    loggroup_name : str
        ロググループ名
    logstream_name : str
        ログストリーム名
    log : str
        出力ログ
    """
    # クライアント作成
    client = create_client()
    # ログストリーム取得
    logstream = get_logstream(client, loggroup_name, logstream_name)
    # 出力ログイベント作成
    logevents = create_logevents(log)
    # ログ出力
    export_logstream(client, loggroup_name,
                     logstream_name, logstream, logevents)


def create_client():
    """
    CloudWatch Logsクライアント作成

    Returns
    -------
    client : boto3.client
        CloudWatch Logsクライアント
    """
    client = boto3.client('logs', config=Config(
        proxies={'http': '10.101.0.1:8080'}))
    return client


def get_logstream(client, loggroup_name, logstream_name):
    """
    ログストリームを取得する。
    ログストリームがない場合は作成する。

    Parameters
    -------
    client : boto3.client
        CloudWatch Logs クライアント
    loggroup_name : str
        ロググループ名
    logstream_name : str
        ログストリーム名
    """
    # ログストリームを検索
    logstream = client.describe_log_streams(
        logGroupName=loggroup_name,
        logStreamNamePrefix=logstream_name)
    # ログストリームが存在しない場合、ログストリームを作成する
    if len(stream['logStreams']) == 0:
        client.create_log_stream(
            logGroupName=loggroup_name,
            logStreamName=logstream_name)
        logstream = client.describe_log_streams(
            logGroupName=loggroup_name,
            logStreamNamePrefix=logstream_name)
    return logstream


def create_logevents(log):
    """
    出力ログイベントを作成する

    Parameters
    ----------
    log : str
        出力ログ

    Returns
    -------
    logevents : dict
        ログイベント
    """
    logevents = [{
        'timestamp': int(datetime.datetime.now().strftime('%s')) * 1000,
        'message': log
    }]
    return logevents


def export_logstream(client, loggroup_name, logstream_name, logstream,
                     logevents):
    """
    CloudWatch Logsに通信履歴を出力する

    Parameters
    ----------
    client : boto3.client
        CloudWatch Logs クライアント
    loggroup_name : str
        ロググループ名
    logstream_name : str
        ログストリーム名
    logstream : dict
        ログストリーム
    logevents : dict
        出力ログイベント

    Returns
    -------
    response : dict
        ログ出力結果
    """
    # ログ出力
    if 'uploadSequenceToken' in logstream['logStreams'][0]:
        response = client.put_log_events(
            logGroupName=loggroup_name,
            logStreamName=logstream_name,
            logEvents=logEvents,
            sequenceToken=logstream['logStreams'][0]['uploadSequenceToken'])
    else:
        response = client.put_log_events(
            logGroupName=loggroup_name,
            logStreamName=logstream_name,
            logEvents=logEvents)
    return response


def search_log_groups(name, token=None, limit=50):
    clinet = create_client()
    if token is None:
        response = clinet.describe_log_groups(logGroupNamePrefix=name,
                                              limit=limit)
    else:
        response = clinet.describe_log_groups(logGroupNamePrefix=name,
                                              nextToken=token, limit=limit)
    return response


def search_log_stream(group_name, stream_name_prefix=None):
    client = create_client()
    if stream_name_prefix is None:
        response = client.describe_log_streams(
            logGroupName=group_name)
    else:
        response = client.describe_log_streams(
            logGroupName=group_name, logStreamNamePrefix=stream_name_prefix)
    return response


def filter_log_group(group_name, stream_prefix=None, start=None,
                     end=None):
    client = create_client()
    if stream_prefix is None:
        response = client.filter_log_events(
            logGroupName=group_name, startTime=start,
            endTime=end, interleaved=True)
    else:
        response = client.filter_log_events(
            logGroupName=group_name,
            logStreamNamePrefix=stream_prefix, startTime=start,
            endTime=end, interleaved=True)


def log_backup(group_name, fromTime, to, destination, stream_prefix=None,
               destinationPrefix=None):
    client = create_client()
    if stream_prefix is None:
        response = client.create_export_task(
            taskName='export logs task',
            logGroupName=group_name,
            fromTime=fromTime,
            to=to,
            destination=destination,
            destinationPrefix=destinationPrefix)
    else:
        response = client.create_export_task(
            taskName='export logs task',
            logGroupName=group_name,
            logStreamNamePrefix=stream_prefix,
            fromTime=fromTime,
            to=to,
            destination=destination,
            destinationPrefix=destinationPrefix)
