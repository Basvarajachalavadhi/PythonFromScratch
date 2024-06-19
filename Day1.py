# First program as per tradition is
print("Hello World of Python and Git")
# Problem Statement objective is to solve real life physics problems using Python

# Problem 1 : Write a program to solve the force problem i.e we have to calculate the force when mass and acceleration is given .

# Tools required
class Force:
    def __init__(self, mass, acceleration):
        self.mass = mass
        self.acceleration = acceleration

    def GenForce(self):
        return self.mass * self.acceleration

    def MomForce(m,iv,vv,t):
        return m*(vv-iv) // t

# Testing and running the code
m = 12
a = 1
force_instance = Force(m, a)
res = force_instance.GenForce()
res = Force.MomForce(m,1,4,2)
print(res)
