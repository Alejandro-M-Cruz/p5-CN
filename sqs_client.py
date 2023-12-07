import boto3


class SqsClient:
    def __init__(self):
        self.client = boto3.client("sqs")

    def get_queue_url(self, queue_name: str):
        self.client.get_queue_url(QueueName=queue_name)

    def send_message(self, message: str, queue_url: str):
        self.client.send_message(QueueUrl=queue_url, MessageBody=message)

    def receive_message(self, queue_url: str):
        self.client.receive_message(QueueUrl=queue_url)

