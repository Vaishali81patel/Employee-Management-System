import unittest
from file_handler import FileHandler


class FileHandlerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test 7
    def test_list(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue(type(csv._fieldnames) == list)

    # Test 8
    def test_field(self):
        csv = FileHandler("employeeinfo.csv")
        data = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        self.assertListEqual(csv._fieldnames, data)

    # Test 9
    def test_file_exist(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue (csv.file_exist ())

    # Test 10
    def test_read(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertTrue (csv.read())

    # Test 11
    def test_save(self):
        csv = FileHandler("employeeinfo.csv")
        data = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        self.assertListEqual (csv._fieldnames, data)

    # Test 12
    def test_datalist(self):
        csv = FileHandler ("employeeinfo.csv")
        self.assertTrue (type (csv.read ()) == list)

    # Test 13
    def test_csv(self):
        csv = FileHandler("employeeinfo.csv")
        self.assertRaises(AttributeError, csv.save, "This is a data list")

    # Test 14
    def file_read(self):
        self.assertTrue (hasattr (FileHandler, "read"))

    # Test 15
    def file_save(self):
        self.assertTrue (hasattr (FileHandler, "save"))

    # Test 16
    def get_data(self):
        self.assertTrue (callable (getattr (FileHandler, "read")))

    # Test 17
    def save_data(self):
        self.assertTrue (callable (getattr (FileHandler, "save")))

suite = unittest.TestLoader().loadTestsFromTestCase(FileHandlerTests)
unittest.TextTestRunner(verbosity=1).run(suite)
