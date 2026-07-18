def  input_temperature(a):
    print(f"Input data is '{a}'")
    
    try:
        int(a)
        if a >= 40:
            print(f"Caught input_temperature error: {a}°C is too hot for plants (max 40°C)\n")
        elif a <= 0:
            print(f"Caught input_temperature error: {a}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature is now {a}°C\n")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{a}'\n")

def test_temperature():
    input_temperature(25)
    input_temperature('abc')
    input_temperature(100)
    input_temperature(-50)

if  __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")