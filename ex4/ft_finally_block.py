class PlantError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")
if __name__ == "__main__":
    print('=== Garden Watering System ===\n')
    print('Testing valid plants...')
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrot")
        print('Closing watering system')
        print('\nTesting invalid plants...')
        print('Opening watering system')
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print('.. ending tests and returning to main')
        print('Closing watering system\n')
    print('Cleanup always happens, even with errors!')