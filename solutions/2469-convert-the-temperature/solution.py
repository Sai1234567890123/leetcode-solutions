class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        # Calculate Kelvin using the provided formula: Kelvin = Celsius + 273.15
        kelvin = celsius + 273.15
        
        # Calculate Fahrenheit using the provided formula: Fahrenheit = Celsius * 1.80 + 32.00
        fahrenheit = celsius * 1.80 + 32.00
        
        # Return the results as a list [kelvin, fahrenheit]
        return [kelvin, fahrenheit]
