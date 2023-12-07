from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from cloud_formation_client import CloudFormationClient
from lambda_client import LambdaClient


def main(delete=False, only_invoke=False):
    if not only_invoke:
        cloud_formation = CloudFormationClient()
        cloud_formation.delete_stack(name="p5-stack", wait=True)
        if delete:
            return
        code = {}
        for code_file in ["function_a.py", "function_b.py", "function_c.py"]:
            with open(code_file) as f:
                code[code_file] = f.read()
        cloud_formation.create_stack_from_template_file(
            template_path="p5_stack.yaml",
            name="p5-stack",
            template_params={
                "QueueName": "p5-queue",
                "FunctionAName": "p5-function-a",
                "FunctionACode": code["function_a.py"],
                "FunctionBName": "p5-function-b",
                "FunctionBCode": code["function_b.py"],
                "FunctionCName": "p5-function-c",
                "FunctionCCode": code["function_c.py"],
            },
            wait=True
        )
    lambda_client = LambdaClient()
    lambda_client.invoke(function_name="p5-function-a")
    lambda_client.invoke(function_name="p5-function-b")
    lambda_client.invoke(function_name="p5-function-c")


if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--delete", action="store_true", help="delete the stack", default=False)
    parser.add_argument("--only-invoke", action="store_true", help="invoke lambda functions and exit", default=False)
    args = vars(parser.parse_args())
    main(delete=args["delete"], only_invoke=args["only_invoke"])
