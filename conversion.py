
def convert(celsius_data):
    return [celsiusToFarenheit(t) for t in celsius_data]

def celsiusToFarenheit(temperature):
    return (temperature*9/5) + 32
