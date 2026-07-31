def input_temperature(a: str) -> int:
    print(f"Input data is '{a}'")
    temp = int(a)
    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature is now {temp}°C\n")
        return temp


def test_temperature() -> None:
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
