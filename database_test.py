import unittest
from database import Database


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.database_handler = Database()
        self.data = [['E111', 'F', '36', '550', 'Normal', '99', '30-5-1975'],
                     ['B234', 'M', '7', '777', 'Overweight', '250', '27-12-1978'],
                     ['C4', 'Male', 'nine', '99,9', 'heavy', '3,00', '1-12-19']]

    # Test 18
    def test_temp_db(self):
        # opens a new database then returns contents
        # returns a blank list
        self.assertFalse(self.database_handler.insert_employee_data("test_db"))

    # Test 19
    def test_db_mydb(self):
        # Try save data to a database that has the name mydb
        # Should pass
        self.assertTrue(self.database_handler.save_data(self.data, 'mydb'))

    # Test 20
    def test_temp_db(self):
        # Try save data to a database that has the name mydb
        # but no data is passed in Should fail
        self.assertFalse(self.database_handler.save_data('mydb'))

    # Test 21
    def test_save_temp_db(self):
        # Try save data to a database but no data
        # is passed in to the method. Should fail
        self.assertFalse(self.database_handler.save())


suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseTests)
unittest.TextTestRunner(verbosity=1).run(suite)
