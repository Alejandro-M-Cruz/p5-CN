import os

import boto3


def lambda_handler(event, context):
    sqs = boto3.client("sqs")
    topic_message = event["Records"][0]["Sns"]["Message"]
    message = topic_message + " Hello from function A."
    print(message)
    sqs.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody=message)
    return {
        "message": message
    }
