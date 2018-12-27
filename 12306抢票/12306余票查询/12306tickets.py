# -*- coding:UTF-8 -*-
import requests
import json
import re

class queryTickets():

    def __init__(self,train_date = '2019-01-25',from_station='金华',to_station ='重庆',purpose_codes = 'ADULT'):
        self.station_name_to_codes = self.get_station_codes()
        self.station_codes_to_name = { k:v for v,k in self.station_name_to_codes.items() }
        self.train_date = train_date
        self.from_station = self.station_name_to_codes[from_station]
        self.to_station =self.station_name_to_codes[to_station]
        self.purpose_codes = purpose_codes
    def query_url(self):
        url_head = 'https://kyfw.12306.cn/otn/leftTicket/queryA?'
        url_train_date = 'leftTicketDTO.train_date={}'.format(self.train_date)
        url_from_station = 'leftTicketDTO.from_station={}'.format(self.from_station)
        url_to_station = 'leftTicketDTO.to_station={}'.format(self.to_station)
        url_purpose_codes = 'purpose_codes={}'.format(self.purpose_codes)
        return url_head+url_train_date+'&'+url_from_station+'&'+url_to_station+'&'+url_purpose_codes
    def get_station_codes(self):
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9085'
        response = requests.get(url)
        station_codes = {}
        stations = re.findall(r'[\u4e00-\u9fa5]+\|[A-Z]+',response.text)
        for station in stations:
            station = station.split('|')
            station_codes[station[0]] = station[1]
        return station_codes

    def query_tickets(self):
        url = self.query_url()
        response = requests.get(url)
        res =  json.loads(response.text)
        if res['status'] == True:
            tickets_infos = []
            for info in res['data']['result']:
                ticket= {}
                info = info.split('|')
                ticket['车次'] = info[3]
                ticket['出发站'] = self.station_codes_to_name[info[6]]
                ticket['到达站'] = self.station_codes_to_name[info[7]]
                ticket['出发时间'] = info[8]
                ticket['到达时间'] = info[9]
                ticket['乘坐用时'] = info[10]
                ticket['可预订'] = info[11]
                #ticket['商务座'] = info[-13]
                ticket['一等座'] = info[-7]
                ticket['二等座'] = info[-8]
                ticket['高级软卧'] = info[21]
                ticket['软卧'] = info[23]
                ticket['动卧'] = info[33]
                ticket['硬卧'] = info[28]
                ticket['软座'] = info[24]
                ticket['硬座'] = info[29]
                ticket['无座'] = info[26]
                ticket['其他'] = info[1]
                tickets_infos.append(ticket)
            return tickets_infos
        else:
            print("！！！无余票信息！！！")
    def query_bookable_tickets(self):
        all_trains = self.query_tickets()
        for train in all_trains[:]:
            if train['可预订'] == 'N':
                all_trains.remove(train)
        return all_trains
    def show_tickets_infos(self,train_type='a',only_bookable=False):
        if only_bookable:
            tickets_infos = self.query_bookable_tickets()
            from termcolor import colored
            print(colored('%s-->%s     %s     有票车次信息：'%
                    (
                        self.station_codes_to_name[self.from_station],
                        self.station_codes_to_name[self.to_station],
                        self.train_date
                    )
                )   
                )
        else: 
            tickets_infos = self.query_tickets()
        import prettytable as pt
        tb = pt.PrettyTable()
        tb.field_names = tickets_infos[0].keys()
        for info in tickets_infos:
            if info['车次'][0] in train_type or train_type == 'a':
                tb.add_row(info.values())
        print(tb)
if __name__ == '__main__':
    query1 = queryTickets(train_date='2019-01-22',from_station='杭州')
    query1.show_tickets_infos(only_bookable=True)
    query2 = queryTickets(train_date='2019-01-22',from_station='福州')
    query2.show_tickets_infos(only_bookable=True)