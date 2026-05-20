def operation_number(a):
    print(f"Testing operation {a}...")
    if a == 0:
        try:
            int("abc")
        except ValueError:
            a = str('abc')
            print (f"Caught input_temperature error: invalid literal for int() with base 10: '{a}'")
            return
    elif a == 1:
        try:
            5 / 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
            return
    elif a == 2:
        try:
            open("test.txt", 'r')
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
            return
    elif a == 3:
        try:
            "abc" + 5
        except TypeError:
            print("Caught TypeError: can only concatenate str (not \"int\") to str")
            return       
    else:
        print("Operation completed successfully") 
if __name__ == "__main__":
    print('=== Garden Error Types Demo ===')
    operation_number(0)
    operation_number(1)
    operation_number(2)
    operation_number(3)
    operation_number(4)
    print('\n')
    print('All error types tested successfully!')