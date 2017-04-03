from cmath import sqrt


class Program:
    fi = (sqrt(5) + 1) / 2
    e = 0.00001

    def f(self, x):
        return x * x + 2

    def ObshiiPoisk(self, a, b, e):
        h = self.e / 2
        min = self.f(a)
        xk = 0
        for x in range(int(b + h / 2)):
            x = a

            if self.f(x) < min:
                min = self.f(x)
                xk = x
            a += h
        return xk


if __name__ == "__main__":
    cl = Program()
    cl.ObshiiPoisk(10000, 1000, 0.00001)
