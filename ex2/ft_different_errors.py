def  input_temperature(operation_number, a):
    try:
        if operation_number == 0:
            int(a)
        elif operation_number == 1:    
            number = 10 / a
        elif operation_number == 2:
            with open(a, "r") as f:
                print(f.read())
        elif operation_number == 3:
            str = "loloko" + a
        else:
            print("Operation completed successfully\n")
    except ValueError:
        print(f"Caught ValueError: invalid literal for int() with base 10: '{a}'")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError:
        print("Caught TypeError: can only concatenate str (not \"int\") to str")
        
def garden_operations(operation_number):
    print (f"Testing operation {operation_number}..")
    if operation_number == 0:
        input_temperature(operation_number, 'abc')
    elif operation_number == 1:
        input_temperature(operation_number, 0)
    elif operation_number == 2:
        input_temperature(operation_number ,"non/existent/file")
    elif operation_number == 3:
        input_temperature(operation_number, 15)
    else:
        input_temperature(operation_number ,25)

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("All error types tested successfully!")