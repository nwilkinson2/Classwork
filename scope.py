b = "Hello"


def variable_definition():
    global a, b
    a = 5
    b = "Hello"
    print("a defined as {} in variable_definition".format(a))
    print("b defined as {} in variable_definition".format(b))
    return a, b


def variable_output():
    print("a is {} in variable output".format(a))
    print("b is {} in variable output".format(b))


if __name__ == "__main__":
    a=10
    variable_definition()
    variable_output()