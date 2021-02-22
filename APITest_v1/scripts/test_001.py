import unittest
from public.httpjsonrequest import HttpJsonRequest


class ApiTest(unittest.TestCase):
    # def __init__(self,var='../config/var.ini',case=__name__):
    #     super(unittest.TestCase,self).__init__(var,case)
    #     self.var = var
    #     self.case = '../case/' + case + '.json'
    @classmethod
    def setUpClass(cls,var='../config/var.ini',case=__name__) -> None:
        cls.var = var
        cls.case = '../case/' + case + '.json'


    def setUp(self) -> None:
        pass

    def test_step01(self):
       return HttpJsonRequest(self.var,self.case).send_requet()
    def test_step02(self):
       return HttpJsonRequest(self.var,self.case).send_requet()

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()