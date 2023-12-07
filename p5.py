from time import sleep


def function_a(a: str):
    print("Executing function a...")
    sleep(3)
    return f"{a} was processed by function a"

def function_b(b: str):
    print("Executing function b...")
    sleep(4)
    return f"{b} and by function b"

def function_c(c: str):
    print("Executing function c...")
    sleep(5)
    return f"{c} and also by function c"


if __name__ == "__main__":
    x = function_a("something")
    y = function_b(x)
    z = function_c(y)
    print(z)
