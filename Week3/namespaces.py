# def my_function():
#    msg = "Hello"
#    print(msg)
#    return None

# my_function()
# print(msg)
# print(my_function())
# print(msg)


def my_function():
    def my_second_function():
        global msg
        msg = "Hello"
        return None

    my_second_function()
    msg = "Hello1"
    print(f"Functia Principala {msg}")
    return None


my_function()
print(msg)
