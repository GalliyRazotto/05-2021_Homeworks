class Base:
    def __init__(self, x=0):
        self.x = x


class Slave(Base):
    def __init__(self, x):
        super(Slave, self).__init__()
        self.x = x


s1 = Slave(x=2)
print(s1.x)