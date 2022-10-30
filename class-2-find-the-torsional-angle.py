class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        d1 = self.x-no.x
        d2 = self.y-no.y
        d3 = self.z-no.z
        return Points(d1,d2,d3)

    def dot(self, no):
        d1 = self.x*no.x
        d2 = self.y*no.y
        d3 = self.z*no.z
        res = d1+d2+d3
        return res
        

    def cross(self, no):
        d1 = (self.y*no.z)-(self.z*no.y)
        d2 = (self.x*no.z)-(self.z*no.x)
        d3 = (self.x*no.y)-(self.y*no.x)
        return Points(d1,d2,d3)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
