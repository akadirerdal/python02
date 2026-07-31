def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            number = 10 / 0
            print(number)
        elif operation_number == 2:
            with open("/non/existent/file", "r") as f:
                print(f.read())
        elif operation_number == 3:
            text = "loloko" + 15
            print(text)
        else:
            print("Operation completed successfully\n")
    except ValueError:
        print("Caught ValueError: invalid literal for int() "
              "with base 10: 'abc'")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError:
        print("Caught TypeError: can only concatenate str "
              "(not \"int\") to str")


def test_error_types() -> None:
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
