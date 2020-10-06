TEST = 0

if not TEST:
    from app import Application
    app = Application()

else:
    from tests.core import ImpulseTest
    from tests.core import AnTest

    ImpulseTest()
    AnTest()
