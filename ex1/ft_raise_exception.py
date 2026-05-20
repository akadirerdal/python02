def ft_raise_exception(a):
    print(f"input data is '{a}'")
    try:
        number = int(a)
    except ValueError:
        print (f"Caught input_temperature error: invalid literal for int() with base 10: '{a}'")
        return
    if number < 0:
        print(f"Caught input_temperature error: {number}°C is too cold for plants (min 0°C)")
    elif number > 40:
        print (f"Caught input_temperature error: {number}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature is now {number}°C")
if __name__ == "__main__":
    print('=== Garden Temperature Checker ===\n')
    number = ft_raise_exception("25")
    print('\n')
    ft_raise_exception('abc')
    print('\n')
    ft_raise_exception('100')
    print('\n')
    ft_raise_exception('-50')
    print('\n')
    print('All tests completed - program didn\'t crash!')
