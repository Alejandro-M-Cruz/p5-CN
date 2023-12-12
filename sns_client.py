import boto3


class SnsClient:
    def __init__(self):
        self.client = boto3.client("sns")

    def publish(self, topic_arn: str, message: str):
        self.client.publish(TopicArn=topic_arn, Message=message)
