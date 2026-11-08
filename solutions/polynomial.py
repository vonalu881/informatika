class Polynomial:
    def __init__(self, coeffs):
        c = list(coeffs)
        
        while len(c) > 1 and c[-1] == 0:
            c.pop()
            
        if not c:
            c = [0]
            
        self.coeffs = c

    def degree(self):
        return len(self.coeffs) - 1

    def __call__(self, x):
        result = 0
        for i in range(len(self.coeffs) - 1, -1, -1):
            result = result * x + self.coeffs[i]
        return result

    def __add__(self, other):
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len1 else 0
            c2 = other.coeffs[i] if i < len2 else 0
            new_coeffs.append(c1 + c2)
            
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        
        new_coeffs = [0] * (len1 + len2 - 1)
        
        for i in range(len1):
            for j in range(len2):
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(new_coeffs)

    def derivative(self):
        if self.degree() == 0:
            return Polynomial([0])
            
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(self.coeffs[i] * i)
            
        return Polynomial(new_coeffs)

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return False
        return self.coeffs == other.coeffs

    def __repr__(self):
        return f"Polynomial({self.coeffs})"
