import re

r = re.findall("\\$\\$\\{.+?\\}",open("../case/test_001.json",'r').read())
print(r)

# import requests
# re1 = getattr(requests,'get')
# rp = re1(url = "http://www.baidu.com")
# print(rp.text)

class Test():
    a = 1
    b = 2
    @classmethod
    def test1(cls):
        c = 1
        cls.test2()
        print(cls.a)
    @staticmethod
    def test2():
        print(2)

    @property
    def test3(self):
        return 4

    def test4():
        return 4
Test.test4()
Test.test1()
#Test.test2()
d = Test().test3
print(d)