import configparser


class ReadIni:

    def __init__(self,file_name=None):
        if file_name is None:
            self.cp = self.load_ini(r'../config/var.ini')
        else:
            self.cp = self.load_ini(file_name)

    def load_ini(self,file_name):
        cp = configparser.ConfigParser()
        cp.read(file_name)
        return cp

    def get_value(self,section,option):
        return  self.cp.get(section,option)