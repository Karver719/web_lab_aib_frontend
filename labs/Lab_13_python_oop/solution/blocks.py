from base import BaseXlsBlock
import xlsxwriter
from datetime import datetime

class Parameters(BaseXlsBlock):
    TITLE = 'Параметры запроса'
    DATE = 'Дата выгрузки'
    SUBTITLE = 'Период, за который сделана выгрузка'
    def writer_some_data(self):
        self.row+=1
        self.worksheet.write(self.row, self.col, self.DATE)
        self.col+=1
        formatted_date = datetime.now().strftime("%Y-%m-%d")
        self.worksheet.write(self.row, self.col, formatted_date)
        self.col -=1
        self.row+=1
        self.worksheet.write(self.row, self.col, self.SUBTITLE)
        self.col +=1
        some_dates = []
        for pay in self.some_data['payments']:
            some_dates.append(pay['created_at'])
        some_dates = [datetime.fromisoformat(date[:-1]) for date in some_dates]
        some_dates.sort()
        data_min =some_dates[0].strftime("%Y-%m-%d")
        data_max =some_dates[-1].strftime("%Y-%m-%d")
        some_data = f'{data_min} - {data_max}'
        self.worksheet.write(self.row, self.col, some_data )

    def writer_header(self):
        self.worksheet.write(self.row, self.col, self.TITLE)
    
class Report(BaseXlsBlock):
    TITLE = 'Отчет по активным клиентам'
    SUBTITLE = 'Топ клиентов по количеству платежей'

    def writer_header(self):
        self.row =5
        self.worksheet.write(self.row, self.col, self.TITLE)
    def writer_some_data(self):
        self.row+=1
        self.worksheet.write(self.row, self.col, self.SUBTITLE)
        self.col+=1
        clients_and_payments = []
        for client in self.some_data['clients']:
            for payment in self.some_data['payments']:
                if client['id'] == payment['client_id']:
                    clients_and_payments.append({
                        'fio': client['fio'],
                        'amount': payment['amount'],
                        'created_at' : payment['created_at']
                    })
        clients_and_payments.sort(key=lambda amount:datetime.fromisoformat(amount['created_at']), reverse=True)

        quarters = {}
        for client_payment in clients_and_payments:
            payment_date = datetime.fromisoformat(client_payment['created_at'])
            q = f'Q{(payment_date.month%4 + 1)} {payment_date.year}' 
            quarters.setdefault(q,[]).append({
                'fio':client_payment['fio'],
                'amount':client_payment['amount']
                })
        
        for q in quarters:
            self.worksheet.write(self.row,self.col,q)
            srt = sorted(quarters[q], key=lambda amount:amount['amount'])[:10]
            count =0
            for s in srt:
                self.row+=1
                count+=1
                self.worksheet.write(self.row, self.col, f"{count}. { s['fio']}")
            self.row-=10
            self.col+=1

class Geography(BaseXlsBlock):
    TITLE = 'География клиентов'
    SUBTITLE = 'Статистика распределения клиентов'
    CITY = 'Города'
    KOL = 'Количество городов'
    def writer_header(self):
        print("Report")
        self.row =19
        self.worksheet.write(self.row, self.col, self.TITLE)
        self.row +=1
        self.worksheet.write(self.row, self.col, self.SUBTITLE)
        self.col+=1
        self.worksheet.write(self.row, self.col, self.CITY)  
        self.col+=1   
        self.worksheet.write(self.row, self.col, self.KOL)     
    def writer_some_data(self):
        self.col-=1  
        self.row +=1
        cities={}
        for client in self.some_data['clients']:
            city = client['city']
            if city in cities:
                cities[city]+=1
            else: 
                cities[city]=1
        sort_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
        for city, count in sort_cities[:10]:
            self.worksheet.write(self.row,self.col,city)
            self.col+=1
            self.worksheet.write(self.row,self.col,count)
            self.col-=1
            self.row+=1

class Status(BaseXlsBlock):
    TITLE = 'АНАЛИЗ СОСТОЯНИЯ СЧЕТА'
    SUBTITLE = 'Статистика состояния счета'
    CLIENT = 'Клиент'
    STATE = 'Состояние счета'
    DEBT = 'Задолженность'
    PROFIT = 'Прибыль'

    def writer_header(self):
        self.col=0
        self.row=33
        self.worksheet.write(self.row,self.col,self.TITLE)
        self.worksheet.merge_range('A35:A36',self.SUBTITLE)
        self.worksheet.merge_range('B35:C35',self.DEBT)
        self.worksheet.merge_range('E35:D35',self.PROFIT)
        self.col+=1
        self.row+=2
        self.worksheet.write(self.row,self.col,self.CLIENT)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.STATE)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.CLIENT)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.STATE)
    
    def writer_some_data(self):
        self.col=1
        self.row=36

        status = []
        for client in self.some_data['clients']:
            for payment in self.some_data['payments']:
                if client['id'] == payment['client_id']:
                    status.append({
                        'fio': client['fio'],
                        'payment_amount': payment['amount'],
                    })
        
        status.sort(key=lambda x:x['payment_amount'],reverse=True)

        for s in status[-10:]:
            self.worksheet.write(self.row,self.col,s['fio'])
            self.col+=1
            self.worksheet.write(self.row,self.col,s['payment_amount'])
            self.col-=1
            self.row+=1
        
        self.col=3
        self.row=36

        for s in status[:10]:
            self.worksheet.write(self.row,self.col,s['fio'])
            self.col+=1
            self.worksheet.write(self.row,self.col,s['payment_amount'])
            self.col-=1
            self.row+=1