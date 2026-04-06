class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius ** 2

    def perimeter(self):
        return 2 * 22/7 * self.radius

r = float(input("Enter radius: "))

c = circle(r)

print("Area:", c.area())
print("Perimeter:", c.perimeter())