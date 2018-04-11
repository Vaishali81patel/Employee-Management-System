import unittest
from data_validator import DataValidator


class ValidatorTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # Test 1
    def test_id(self):
        v = DataValidator()
        self.assertFalse(v.check_empid('AZ0'))
        self.assertFalse(v.check_empid('000'))
        self.assertFalse(v.check_empid('AAA'))
        self.assertFalse(v.check_empid('999'))
        self.assertTrue (v.check_empid ('E111'))
        self.assertTrue (v.check_empid ('e111'))
        self.assertFalse (v.check_empid ('EE11'))

    # Test 2
    def test_gender(self):
        v = DataValidator()
        self.assertTrue (v.check_gender ('M'))
        self.assertTrue (v.check_gender ('F'))
        self.assertTrue (v.check_gender ('GIRL'))
        self.assertTrue (v.check_gender ('BOY'))
        self.assertTrue (v.check_gender ('girl'))
        self.assertTrue (v.check_gender ('boy'))
   #     self.assertFalse (v.check_gender (None))
   #     self.assertFalse (v.check_gender ({}))
   #     self.assertFalse (v.check_gender ('MF'))

   # Test 3
    def test_age(self):
        v = DataValidator ()
        self.assertTrue (v.check_age ('01'))
        self.assertFalse (v.check_age ('00'))
        self.assertFalse (v.check_age (''))
        self.assertFalse (v.check_age (' '))
        self.assertFalse (v.check_age ('0.0'))
        self.assertFalse (v.check_age ('0,0'))
        self.assertFalse (v.check_age ('0:0'))
        self.assertFalse (v.check_age ('01-01-0000'))

    # Test 4
    def test_sales(self):
        v = DataValidator ()
        self.assertTrue (v.check_sales ('999'))
        self.assertTrue (v.check_sales ('111'))
        self.assertTrue (v.check_sales ('99'))
    #    self.assertTrue (v.check_sales ('99.99'))


    # Test 5
    def test_bmi(self):
        v = DataValidator ()
        self.assertTrue (v.check_bmi ('Normal'))
        self.assertTrue (v.check_bmi ('Overweight'))
        self.assertTrue (v.check_bmi ('Obesity'))
        self.assertTrue (v.check_bmi ('Underweight'))
    #    self.assertFalse (v.check_bmi ('rUnderweight'))
    #    self.assertFalse (v.check_bmi ('Underweight2'))
    #    self.assertFalse (v.check_bmi ('UNDERWEIGHT'))
        self.assertFalse (v.check_bmi (""))
        self.assertFalse (v.check_bmi (1))
        self.assertFalse (v.check_bmi (True))

    # Test 7
    def test_birthday(self):
        v = DataValidator ()
        self.assertTrue (v.check_birthday ('1-1-1996'))
        self.assertTrue (v.check_birthday ('31-12-1961'))
        self.assertTrue (v.check_birthday ('31-12-1161'))
        self.assertTrue (v.check_birthday ('31-12-3161'))
    #        self.assertFalse (v.check_birthday (56186729))
          
        self.assertFalse (v.check_birthday ('1/1/1996'))
        """
        self.assertFalse (v.check_birthday ("Jan-31-1971"))
        self.assertFalse (v.check_birthday (True))
        self.assertFalse (v.check_birthday (""))
        self.assertFalse (v.check_birthday ("--"))

    # Test 6
    def test_salary(self):
        v = DataValidator ()
        self.assertTrue (v.check_salary ('111'))
        self.assertTrue (v.check_salary ('001'))
        self.assertTrue (v.check_salary ('999'))
        self.assertFalse (v.check_salary (1))
        self.assertFalse (v.check_salary (999))
        self.assertFalse (v.check_salary ('1'))
        self.assertFalse (v.check_salary ("1000"))
        self.assertFalse (v.check_salary ("one"))
        self.assertFalse (v.check_salary (True))


"""

suite = unittest.TestLoader().loadTestsFromTestCase(ValidatorTests)
unittest.TextTestRunner(verbosity=1).run(suite)
