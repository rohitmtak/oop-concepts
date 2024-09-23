class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
        
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
        
    def __sub__(self, other):
        temp_num = self.num * other.num - other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
        
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = other.num * self.den
        return "{}/{}".format(temp_num, temp_den)
        

f1 = Fraction(4, 2)
f2 = Fraction(2, 3)
        
print("Fraction 1:", f1)
print("Fraction 2:", f2)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
