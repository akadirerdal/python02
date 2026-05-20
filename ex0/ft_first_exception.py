def ft_first_exception(a):
    print(f"input data is '{a}'")
    try:
        number = int(a)
        return number
    except ValueError:
        print (f"Caught input_temperature error: invalid literal for int() with base 10: '{a}'")

if __name__ == "__main__":
    print('=== Garden Temperature ===\n')
    number = first_exception("25")
    print(f"Temperature is now {number}°C")
    print('\n')
    first_exception('abc')
    print('\n')
    print('All tests completed - program didn\'t crash!')
          