from .. models import Company
import pytest


# @pytest.mark.usefixtures("session")
class TestModels:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_company_exists(self):
        assert Company

    def test_query_all(self):
        assert Company.query.all() == []

    def test_add_then_query_all(self, session):
        company = Company(symbol = 'goog')
        session.add(company)
        session.commit()
        assert len(Company.query.all()) == 1

    def test_add_then_query_all_again(self, session):
        company = Company(symbol = 'amzn')
        session.add(company)
        session.commit()
        assert len(Company.query.all()) == 1
