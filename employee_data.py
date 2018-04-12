from data import Data
from file_handler import FileHandler
from database import Database


class EmployeeData:
    """
    For data related operations
    """
    def __init__(self):
        self.data = []
        self.new_data = []
        self._source = None

    def select_source(self, source, file_path=None, create=False):
        """
        Initialise the data source
        :param source: <String>
        :param file_path: <Sting>
        :param create: <Boolean>
        :return: None
        :Author: Vaishali Patel
        """
        # Set _self as an object of data operation when it hasn't been set
        if source == "csv":
            self._source = FileHandler(file_path, create)
            self.load_data()
        if source == "db":
            self._source = Database()
            self.load_data()

    def load_data(self):
        """
        Fetch all data from the specified data source
        :return: None
        :Author: Vaishali Patel
        """
        # When fetch data from the data source
        # Move existed data in self.data to the end of the list
        self.data = self._source.read()
        # else:
        #     old_data = self.data
        #     self.data = self._source.read()
        #     self.data += old_data

    def add_data(self, data):
        """
        Add data to self.data
        :param data: <List> data
        :return: None
        :Author: Vaishali Patel
        """
        if not self.data_exist(data):
            # Append to the temporary data
            # self.data.append({d.name:data[d.value] for d in Data})
            self.new_data.append({d.name: data[d.value] for d in Data})
        else:
            # If the EMPID is exists, raise an exception
            raise AttributeError("The EMPID already existed.")

    def data_exist(self, data):
        """
        Check if the data with same empid exists.
        :param data: <List> data
        :return: Boolean
        :Author: Vaishali Patel
        """
        for employee in self.data:
            if data[int(Data.EMPID.value)] == employee[Data.EMPID.name]:
                return True

        for employee in self.new_data:
            if data[int(Data.EMPID.value)] == employee[Data.EMPID.name]:
                return True
        return

    def save_data(self):
        """
        Save data
        :return: None
        :Author: Vaishali Patel
        """
        if self._source is None:
            raise OSError("No data source specified.")

        if len(self.new_data) == 0:
            raise ValueError("Nothing to save.")

        try:
            self._source.save(self.new_data)
        except Exception as e:
            raise IOError(e)
        else:
            # Reset temp data and reload data from the data source
            self.new_data = []
            self.load_data()

    def get_all_data(self):
        return self.data + self.new_data

    def get_gender(self):
        gendeer = {}
        """
        Get gender statistics
        :return: <Dictionary> gender
        :Author: Vaishali Patel
        """
        all_data = self.get_all_data()
        if len(all_data) == 0:
            return {}

        male = 0
        female = 0
        for row in all_data:
            # Calculate sum of male
            if row[Data.GENDER.name] == "M":
                male += 1
            # Calculate sum of female
            else:
                female += 1

        return {"Male": male, "Female": female}

    def get_bmi(self):
        bmi = {}

        all_data = self.get_all_data()
        if len(all_data) == 0:
            return bmi

        for row in all_data:
            if row[Data.BMI.name] not in bmi.keys():
                bmi[row[Data.BMI.name]] = 1
            else:
                bmi[row[Data.BMI.name]] += 1
        return bmi

    def get_salary(self):
        salary = {}

        all_data = self.get_all_data()
        if len(all_data) == 0:
            return salary

        for row in all_data:
            if row[Data.SALARY.name] not in salary.keys():
                salary[row[Data.SALARY.name]] = 1
            else:
                salary[row[Data.SALARY.name]] += 1
        return salary


    def __del__(self):
        self.data = []
        self._source = None


