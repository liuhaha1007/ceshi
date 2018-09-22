import pytest

class TestLogin(object):

    # def setup(self):
    #     print("setup")
    #
    # def setup_class(self):
    #     print("setup_class")
    #
    # def teardown(self):
    #     print("teardown")
    #
    # def teardown_class(self):
    #     print("teardown_class")
    @pytest.mark.run(order=-1)
    def test_login1(self):
        print("0")
        assert True

    @pytest.mark.run(order=-2)
    def test_login2(self):
        print("1")
        assert True
    #
    # @pytest.mark.run(order=5)
    # def test_login3(self):
    #     print("1.5")
    #     assert True
    #
    # @pytest.mark.run(order=2)
    # def test_login4(self):
    #     print("2")
    #     assert True
    #
    # @pytest.mark.run(order=-1)
    # def test_login5(self):
    #     print("-1")
    #     assert True
    #
    # @pytest.mark.run2
    # def test_login6(self):
    #     print("-1.5")
    #     assert True
    #
    # @pytest.mark.run1
    # def test_login4(self):
    #     print("-2")
    #     assert True
    #
    # def test_login8(self):
    #     print("没有")
    #     assert True
    #
    #
    #
    #
