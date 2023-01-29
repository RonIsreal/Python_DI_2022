'''Exercise 1 : Temperature
Instructions
Write a base class called Temperature.
Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
Each of the subclasses should have a method which can convert the temperture to another type.
You must consider different designs and pick the best one according to the SOLID Principle.'''
import random


class Temperature(object):

    def __init__(self, temperature, temptype):
        self.temperature = temperature
        self.temptype = temptype

    def convert_to_celsius(self, temptype):
        if temptype == 'fahrenheit':
            return f" The temperature is {(self.temperature - 32)/1.8} degrees Celsius."
        elif temptype == 'kelvin':
            return f" The temperature is {self.temperature - 273.15} degrees Kelvin."
        else:
            pass

    def convert_to_fahrenheit(self, temptype):
        if temptype == 'celsius':
            return f" The temperature is {(self.temperature * 1.8) + 32} degrees Fahrenheit."
        elif temptype == 'kelvin':
            return f" The temperature is {1.8 * (self.temperature - 273.15) + 32} degrees Kelvin."
        else:
            pass

    def convert_to_kelvin(self, temptype):
        if temptype == 'celsius':
            return f" The temperature is {self.temperature + 273.15} degrees Celsius."
        elif temptype == 'fahrenheit':
            return f" The temperature is {(self.temperature - 32) * 5/9 + 273.15} degrees Fahrenheit."
        else:
            pass

    def __repr__(self):
        return f"It is {self.temperature} degrees {self.temptype}."

class Celsius(Temperature):

    def __init__(self, temperature, temptype):
        super().__init__(temperature, temptype)
        super(Celsius, self).convert_to_celsius(temptype)

class Fahrenheit(Temperature):

    def __init__(self, temperature, temptype):
        super().__init__(temperature, temptype)
        super(Celsius, self).convert_to_fahrenheit(temptype)

class Kelvin(Temperature):

    def __init__(self, temperature, temptype):
        super().__init__(temperature, temptype)
        super(Celsius, self).convert_to_kelvin(temptype)

f_to_c = Celsius(90,'fahrenheit')
print(f_to_c.convert_to_celsius('fahrenheit'))
k_to_c = Celsius(300, 'kelvin')
print(k_to_c.convert_to_celsius('kelvin'))


'''Exercise 2: In The Quantum Realm
Instructions
Write a class called QuantumParticle and implement the following:
The attributes - The particle has an initial position (x), momentum (y) and spin (p)

The method position() - Position measurement: generate a random position (integer between 1 and 10,000)

The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0 and 1)

The method spin() - Spin measurement: can randomly be 1/2 or -1/2

Create a method that implements a disturbance. A disturbance occurs each time a measurement is made (e.g. one of the measurements method is called). Disturbance changes the position and the momentum of the particle (randomly generated) and then prints ‘Quantum Interferences!!’

Implement a meaningful representation of the particle (repr)'''

class QuantumParticle:

    def __init__(self):
        self.position = self.position()
        self.momentum = self.momentum()
        self.spin = self.spin()
        # self. disturbance = self.disturbance()

    def position(self):
        return random.randint(1,10001)

    def momentum(self):
        self.disturbance()
        return "%.2f" % random.uniform(0.00, 1.00)

    def spin(self):
        return random.choice((-0.5, 0.5))

    def disturbance(self):

        new_position = random.randint(1,10001)
        new_momentum = "%.2f" % random.uniform(0.00, 1.00)
        if self.position:
            self.position = new_position
        elif self.momentum:
            self.momentum = new_momentum
        print(f"Quantum interferences!")

    def entangle(self, other):

        if self.spin == -0.5 and other.spin == 0.5 or self.spin == 0.5 and other.spin == -0.5:
            print("Spooky Action at a Distance!")
        else:
            print("Nothing happened.")


    def __repr__(self):
        return f"Particle's Info: POSITION: {self.position}, MOMENTUM: {self.momentum}, SPIN: {self.spin}. "

test = QuantumParticle()
test2 = QuantumParticle()
print(test.position)
print(test.momentum)
print(test.spin)
print(test.__repr__())
test.entangle(test2)