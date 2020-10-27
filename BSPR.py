TEST = 0

if TEST:
    from tests.core import ImpulseTest
    from tests.core import AnTest
    from tests.core import EngineParaTest

    #ImpulseTest()
    #AnTest()
    EngineParaTest()

else:
    from app import Application
    Application()
