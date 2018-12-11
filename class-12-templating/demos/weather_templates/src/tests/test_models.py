from src.models import City
import pytest


# @pytest.mark.usefixtures("session")
class TestClass:
    @classmethod
    def setup_class(cls):
        city = City(name='Bellevue', zipcode='98038')

        # import pdb; pdb.set_trace()
        #
        # session.add(city)
        # session.commit()

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_create_city(self):
        assert self.city.id > 0

    def test_city_name(self):
        assert self.city.name == 'Bellevue'

    def test_city_zip(self):
        assert self.city.zipcode == '98038'
