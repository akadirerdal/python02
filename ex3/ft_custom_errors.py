class GardenerError(Exception):
    def __init__(self, mesage):
        self.mesage = mesage
        super().__init__(self.mesage)
class watererror(GardenerError):
    def __init__(self, mesage):
        self.mesage = mesage
        super().__init__(self.mesage)
class planteror(GardenerError):
    def __init__(self, mesage):
        self.mesage = mesage
        super().__init__(self.mesage)
def check_plant():
    raise planteror("The tomato plant is wilting!")
def check_water():
    raise watererror("Not enough water in the tank!")
if __name__ == "__main__":
    print('=== Custom Gardener Errors Demo ===\n')
    print('Testing PlantError...')
    try:
        check_plant()
    except planteror as e:
        print(f"Caught PlantError: {e}\n")
    print('Testing WaterError...')
    try:
        check_water()
    except watererror as e:
        print(f"Caught WaterError: {e}\n")
    print('Testing catching all garden errors...')
    try:
        check_plant()
    except GardenerError as e:
        print(f"Caught GardenerError: {e}")
    try:
        check_water()
    except GardenerError as e:
        print(f"Caught GardenerError: {e}\n")
    print('All custom error types tested successfully!')
