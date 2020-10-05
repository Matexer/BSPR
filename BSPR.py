TEST = True

if not TEST:
    from app import Application
    app = Application()

else:
    from tests.impulse import ImpulseTest
    ImpulseTest()