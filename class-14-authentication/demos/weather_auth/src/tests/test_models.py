class TestCityModel:
    """
    """
    def test_create_city(self, city):
        """
        """
        assert city.id > 0

    def test_city_name(self, city):
        """
        """
        assert city.name == 'Bellevue'

    def test_city_zip(self, city):
        """
        """
        assert city.zipcode == '98038'


class TestCategoryModel:
    """
    """
    def test_create_category(self, category):
        """
        """
        assert category.id > 0

    def test_category_name(self, category):
        """
        """
        assert category.name is not None
