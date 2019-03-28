import cloudwatchlogs as cl
from datetime import datetime

response = cl.log_backup(
    '/aws/lambda/ut-class',
    int(datetime(2019, 3, 1).timestamp()*1000),
    int(datetime.now().timestamp()*1000),
    's3-gwcloud-file',
    destinationPrefix='com'
)

print(response)
