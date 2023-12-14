def intdiv(a, b):
    try:
        result = a // b
        return result
    except TypeError:
        print("Check operands. Some of them seems strange ...")
    except ZeroDivisionError:
        print("Please don't divide by zero ...")
    except Exception:
        print("Somthing went wrong ...")

result = intdiv(3, "2")
print(result)
result = intdiv(10, 0)
print(result)
result = intdiv(6, 2)
print(result)