import base64

import boto3


class LambdaClient:
    def __init__(self):
        self.client = boto3.client("lambda")

    def invoke(self, function_name: str, print_logs=True):
        response = self.client.invoke(FunctionName=function_name, LogType="Tail" if print_logs else "None")
        if print_logs:
            print(f"Invoked {function_name}. \n"
                  f"Status code: {response['StatusCode']}. \n"
                  f"Logs: {base64.b64decode(response['LogResult']).decode('utf-8')}\n")
