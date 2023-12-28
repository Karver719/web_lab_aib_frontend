from abc import ABCMeta, abstractmethod


class BaseXlsBlock(metaclass=ABCMeta):
    NAME = "Block"
    colNames = []

    def __init__(self, worksheet, workbook, row, col, data={}):
        self.worksheet = worksheet
        self.workbook = workbook
        self.row = row
        self.col = col
        self.data = data

    @abstractmethod
    def writeHeaderCol(self):
        pass

    @abstractmethod
    def writeData(self):
        pass
