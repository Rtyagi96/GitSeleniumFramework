import unittest
import pytest
from Test.test_Login import TestLoginUser
from Test.test_Register import TestNewTour
from Test.test_FlightBooking import TestFlight

TC1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginUser)
TC2 = unittest.TestLoader().loadTestsFromTestCase(TestNewTour)
TC3 = unittest.TestLoader().loadTestsFromTestCase(TestFlight)


# creating test suite
def test_smoke_suite():
    smoke = unittest.TestSuite([TC1, TC2])
    # unittest.TextTestRunner().run(smoke)

    functional = unittest.TestSuite([TC2, TC3])
    unittest.TextTestRunner(verbosity=2).run(functional)
