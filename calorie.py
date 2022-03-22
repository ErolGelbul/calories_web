from temperature import Temperature


class Calorie:
    """ BMR Calculations
    BMR = 10 * weight + 6.25 * height - 5 * age + 5 - 10 * temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age


    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result
