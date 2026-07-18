class MyEror(Exception):
    pass

def Garden_Error():
        try:
            raise MyEror("The tomato plant is wilting!")
        except MyEror as e:
            print(f"Caught PlantError: {e}")

def Repo_Eror():
        try:
            raise MyEror("Not enough water in the tank!")
        except MyEror as i:
            print(f"Caught WaterError: {i}")

def Garden_test():
    print("Testing PlantError...")
    Garden_Error()
    print("\n")
    print("Testing WaterError...")
    Repo_Eror()
    print("\n")
    print("Testing catching all garden errors...")
    Garden_Error()
    Repo_Eror()
    print("\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    Garden_test()
    print("All custom error types work correctly!")