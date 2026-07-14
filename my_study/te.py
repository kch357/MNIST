class Man:
    count = 0

    def __init__(self, name):
        self.name = name
        Man.count += 1
        print("Initialized!")
        print(f"Person count: {Man.count}")

    def hello(self):
        print("Hello " + self.name + "!")
        print(f"Person count: {Man.count}")

    def goodbye(self):
        print("Good-bye " + self.name + "!")
        Man.count -= 1
        print(f"Person count: {Man.count}")


m = Man("David")
m = Man("Alice")
Man.hello(m)  # m.hello() syntactic sugar
Man.goodbye(m)

# a[3]
# 3[a]
# Obfuscation 난독화



# *(a + 3)
# 3[a]
# *(3 + a)