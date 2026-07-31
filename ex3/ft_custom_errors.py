class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def Garden_Error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def Water_Eror() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as i:
        print(f"Caught WaterError: {i}")


def Garden_test() -> None:
    print("Testing PlantError...")
    Garden_Error()
    print("\n")
    print("Testing WaterError...")
    Water_Eror()
    print("\n")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as i:
        print(f"Caught GardenError: {i}")
    print("\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    Garden_test()
    print("All custom error types work correctly!")
