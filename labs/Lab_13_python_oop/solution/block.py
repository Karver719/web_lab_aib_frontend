import xlsxwriter
from datetime import datetime
from base import BaseXlsBlock
from collections import Counter


class HeaderBlock(BaseXlsBlock):
    NAME = "Параметры запроса"
    colNames = ['Дата выгрузки', 'Период, за который сделана выгрузка']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        maxDate, minDate = datetime(1, 1, 1), datetime(3000, 12, 31)
        self.worksheet.write(self.row, 0, datetime.now().strftime('%Y-%m-%d'), subheader_format)
        for payData in self.data['payments']:
            maxDate = max(datetime(*list(map(int, payData["created_at"][:10].split('-')))), maxDate)
            minDate = min(datetime(*list(map(int, payData["created_at"][:10].split('-')))), minDate)

        self.worksheet.write(self.row, 1, f'{minDate.strftime("%Y-%m-%d")} - {maxDate.strftime("%Y-%m-%d")}',
                             subheader_format)


class QuartetPaymentBlock(BaseXlsBlock):
    NAME = "Отчёт по активным клиентам"
    colNames = ['Топ клиентов по количеству платежей', 'Q4 2023', 'Q3 2023', 'Q2 2023', 'Q1 2023', 'Q4 2022']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        quarters = {
            'Q4 2023': [],
            'Q3 2023': [],
            'Q2 2023': [],
            'Q1 2023': [],
            'Q4 2022': [],
        }
        for payment in self.data['payments']:
            client_id = payment['client_id']
            created_at = datetime.strptime(payment['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            quarter = f'Q{(created_at.month - 1) // 3 + 1} {created_at.year}'
            quarters[quarter].append(client_id)

        for quarter in quarters.values():
            self.col += 1
            most_common = Counter(quarter).most_common()[:10]
            for idx, most in enumerate(most_common):
                self.worksheet.write(self.row + idx, self.col, f'{idx + 1}. {self.data["clients"][most[0] - 1]["fio"]}',
                                     cell_format)


class CustomerGeographyBlock(BaseXlsBlock):
    NAME = "География клиентов"
    colNames = ['Статистика распределения клиентов', 'Города', 'Количество клиентов']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        city_counts = {}
        for client in self.data['clients']:
            city = client['city']
            city_counts[city] = city_counts.get(city, 0) + 1

        popular_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        idx = 0
        for city, count in popular_cities:
            self.worksheet.write(self.row + idx, 1, f'{idx + 1}. {city}', cell_format)
            self.worksheet.write(self.row + idx, 2, count, cell_format)
            idx += 1


class BankAccountBlock(BaseXlsBlock):
    NAME = "Анализ состояния счёта"
    colNames = ['Статистика состояния счёта клиента', 'Клиент', 'Состояние счёта', 'Клиент', 'Состояние счёта']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        account_balances = {}
        for payment in self.data['payments']:
            client_id = payment['client_id']
            amount = payment['amount']
            account_balances[client_id] = account_balances.get(client_id, 0) + amount

        debtors = sorted(account_balances.items(), key=lambda x: x[1])[:10]
        rich = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]

        for idx, debtor in enumerate(debtors):
            self.worksheet.write(self.row + idx, 1, f'{idx + 1}. {self.data["clients"][debtor[0] - 1]["fio"]}',
                                 cell_format)
            self.worksheet.write(self.row + idx, 2, debtor[1], cell_format)
            self.worksheet.write(self.row + idx, 3, f'{idx + 1}. {self.data["clients"][rich[idx][0] - 1]["fio"]}',
                                 cell_format)
            self.worksheet.write(self.row + idx, 4, rich[idx][1], cell_format)
