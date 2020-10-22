TEST = 0

if TEST:
    from tests.core import ImpulseTest
    from tests.core import AnTest

    # ImpulseTest()
    AnTest()

else:
    from app import Application
    Application()
