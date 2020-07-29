from head.app import Application

app = Application()


val = [0, 1, 0]
egg = set(val)

if egg != {0}:
    print(egg)
