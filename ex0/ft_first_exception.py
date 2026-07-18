def ft_first_exception(a):
    print(f"Input data is '{a}'")
    
    try:
        int(a)
        print(f"Temperature is now {a}°C\n")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{a}'\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    ft_first_exception(25)
    ft_first_exception('abc')
    print("All tests completed - program didn't crash!")
