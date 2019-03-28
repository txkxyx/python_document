# coding: utf-8
import boto3


def send_mail(source, to, subject, body):
    """
    AWS SESを用いたメール送信

    Parameters
    ----------
    source : str
        送信元メールアドレス
    to : str
        送信先メールアドレス
    subject : str
        件名
    body : str
        メール本文

    Returns
    -------
    response : dict
        メール送信レスポンス
    """
    client = boto3.client('ses', region_name='us-east-1')
    response = client.send_email(
        Source=source,
        Destination={
            'ToAddresses': [
                to
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )

    return response
