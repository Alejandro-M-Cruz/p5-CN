import boto3


class SqsClient:
    def __init__(self, queue_url: str):
        self.client = boto3.client("sqs")
        self.queue_url = queue_url

    def send_message(self, message: str):
        self.client.send_message(QueueUrl=self.queue_url, MessageBody=message)

    def receive_message(self):
        self.client.receive_message(QueueUrl=self.queue_url)
