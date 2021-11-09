import json
from collections import abc

class TickData:
    def __init__(self, market, type, raw):
        if(market == "TWS"):
            columns = raw.split("|")
            if(type == "TX"):
                self.code = columns[0]
                self.trail_flag = columns[4]
                self.q5_flag = columns[5]
                self.total_volume = columns[9]
                self.price = columns[9]
                self.buy_price[0] = columns[13]
                self.buy_volume[0] = columns[14]
        elif(market == "TWF"):
            columns = raw.split("|")
            if(type == "TX"):
                self.code = columns[0]
                self.trail_flag = columns[4]
                self.mathing_time = columns[5]
                self.total_volume = columns[7]
                self.match_buy_cnt = columns[8]
                self.match_sell_cnt = columns[9]
                txn_cnt = columns[11]
                self.match_data = list
                for i in range(txn_cnt):
                    self.match_data.append((columns[12+i],columns[13+i]))
            elif(type == "5Q"):
                self.code = columns[0]
                self.seq = columns[3]
                self.trail_flag = columns[4]
                self.buy = list()
                self.sell = list()
                for i in range(5):
                    self.buy.append((columns[5+i], columns[6+i]))
                for j in range(5):
                    self.sell.append((columns[15+i], columns[16+i]))
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)


class ProductData:
    def __init__(self, market, raw):
        if(market == "TWS"):
            columns = raw.split("|")
            self.code = columns[0]
            self.name_ch = columns[1]
            # self.timestamp = columns[2]
            # self.serial_no = columns[3]
            self.ref_price = columns[4]
            self.rise_stop_price = columns[5]
            self.fall_stop_price = columns[6]
            self.industry_category = columns[7]
            self.stock_category = columns[8]
            self.stock_entries = columns[9]
            self.stock_anomaly_code = columns[10]
            self.board_code = columns[11]
            self.class_code = columns[12]
            self.non_10_face_value_indicator = columns[13]
            self.abnormal_recommendation_indicator = columns[14]
            self.abnormal_securities_indicator = columns[15]
            self.day_trading_indicator = columns[16]
            self.examp_unchg_market_margin_sale_indicator = columns[17]
            self.examp_unchg_market_securities_lending_sale_indicator = columns[18]
            self.matching_cycle_seconds = columns[19]
            self.warrant_id = columns[20]
            self.warrant_strike_price = columns[21]
            self.warrant_strike_volume_before = columns[22] 
            self.warrant_cancel_volume_before = columns[23]
            self.warrant_issuing_balance = columns[24]
            self.warrant_strike_ratio = columns[25]
            self.warrant_upper_limit_price = columns[26]
            self.warrant_lower_limit_price = columns[27]
            self.warrant_maturity_date = columns[28]
            self.foreign_stock_indicator = columns[29]
            self.trading_unit = columns[30]
            self.trading_currency_code = columns[31]
            self.market_information_line = columns[32]
            self.tick_size = columns[33]
        elif(market == "TWF"):
            columns = raw.split("|")
            self.code = columns[0]
            self.name_ch = columns[1]
            self.ref_price = columns[4]
            self.rise_stop_price = columns[5]
            self.fall_stop_price = columns[6]
            self.product_kind = columns[7]
            self.decimal_locator = columns[8]
            self.strike_price_decimal_locator = columns[9]
            self.begin_date = columns[10]
            self.end_date = columns[11]
            self.flow_group = columns[12]
            self.delivery_date = columns[13]
            self.dynamic_banding = columns[14]
            self.contract_kind_code = columns[15]
            self.contract_name_ch = columns[16]
            self.stock_code = columns[17]
            self.contract_size = columns[18]
            self.status_code = columns[19]
            self.currency_type = columns[20]
            self.accept_quote_flag = columns[21]
            self.block_trade_flag = columns[22]
            self.expiry_type = columns[23]
            self.underlying_type = columns[24]
            self.market_close_group = columns[25]
            self.end_session = columns[26]
            self.after_hour = columns[27]
            
    @staticmethod
    def appendHL(data, market, raw):
        if market == "TWS":
            columns = raw.split("|")
            data.market = columns[0]
            data.matching_time = columns[3]
            data.price = columns[6]
            data.volume = columns[7]
            data.high = columns[8]
            data.low = columns[9]
            data.total_amount = columns[10]
            data.total_volume = columns[11]
        elif(market == "TWF"):
            columns = raw.split("|")
            data.market = columns[0]
            data.matching_time = columns[6]
            data.price = columns[9]
            data.volume = columns[10]
            data.high = columns[11]
            data.low = columns[12]
            data.total_volume = columns[14]

def decode_snapshot(data_map, market, json_data):
    json_obj = json.loads(json_data)
    base_list = json_obj["BAS"]
    for basic_raw in base_list:
        product = ProductData(market, basic_raw)
        data_map[product.code] = product
    for hl_raw in json_obj["HL"]:
        if market == "TWS":
            product = hl_raw.split("|")[2]
        if market == "TWF":
            product = hl_raw.split("|")[3]
        ProductData.appendHL(data_map[product], market, hl_raw)


if __name__ == "__main__":
    json_file = \
        '''{"BAS":["23383|光罩三|1635900600695629|180|111.5000|122.6500|100.3500|00|  |  |0|0|0| | | | | | |0| |0.0000|0|0|0|0.00|0.0000|0.0000|0||1000|   |1|0.01:0.05;150.00:1.00;1000.00:5.00","2337|旺宏|1635900557544674|22838|39.4500|43.3500|35.5500|24|  |  |0|0|| | | |A|Y|Y|0| |0.0000|0|0|0|0.00|0.0000|0.0000|0| |1000|   |1|0.01:0.01;10.00:0.05;50.00:0.10;100.00:0.50;500.00:1.00;1000.00:5.00","2331|精英|1635900557540609|22836|22.8500|25.1000|20.6000|25|  |  |0|0|| | | |A|Y|Y|0| |0.0000|0|0|0|0.00|0.0000|0.0000|0| |1000|   |1|0.01:0.01;10.00:0.05;50.00:0.10;100.00:0.50;500.00:1.00;1000.00:5.00","2332|友訊|1635900557542626|22837|20.8000|22.8500|18.7500|27|  |  |0|0|| | | |A|Y|Y|0| |0.0000|0|0|0|0.00|0.0000|0.0000|0| |1000|   |1|0.01:0.01;10.00:0.05;50.00:0.10;100.00:0.50;500.00:1.00;1000.00:5.00","2330|台積電|1635900557538590|22835|592.0000|651.0000|533.0000|24|  |  |0|0|| | | |A|Y|Y|0| |0.0000|0|0|0|0.00|0.0000|0.0000|0| |1000|   |1|0.01:0.01;10.00:0.05;50.00:0.10;100.00:0.50;500.00:1.00;1000.00:5.00","2338|光罩|1635900557546731|22839|87.6000|96.3000|78.9000|24|  |  |0|0|| | | |A|Y|Y|0| |0.0000|0|0|0|0.00|0.0000|0.0000|0| |1000|   |1|0.01:0.01;10.00:0.05;50.00:0.10;100.00:0.50;500.00:1.00;1000.00:5.00"],"HL":["OTC|S|23383|143000.000000|154|2201286|112.1500|0|112.3000|111.0000|15645500.0000|0|5|111.5500|1|111.5000|12|111.4000|3|111.3000|1|111.1500|1|5|112.1500|4|112.3000|11|112.5000|10|112.9000|15|113.0000|21||||||||1","TSE|S|2337|143000.000000|11027|6280824|39.8500|56|40.3000|39.1500|867766200.0000|0|5|39.8500|67|39.8000|136|39.7500|47|39.7000|277|39.6500|153|5|39.9000|25|39.9500|21|40.0000|493|40.0500|81|40.1000|180||||||||1","TSE|S|2331|143000.000000|11025|6281186|23.0000|13|23.3000|22.5000|155985750.0000|0|5|23.0000|101|22.9500|36|22.9000|68|22.8500|78|22.8000|54|5|23.0500|2|23.1000|127|23.1500|39|23.2000|297|23.2500|48||||||||1","TSE|S|2332|143000.000000|11026|6281333|20.8000|7|21.3000|20.7000|93001500.0000|0|5|20.8000|57|20.7500|109|20.7000|275|20.6500|80|20.6000|138|5|20.8500|1|20.9000|18|20.9500|30|21.0000|80|21.0500|15||||||||1","TSE|S|2330|143000.000000|11024|6280977|592.0000|35|597.0000|592.0000|6084130000.0000|0|5|591.0000|346|590.0000|859|589.0000|1017|588.0000|385|587.0000|337|5|592.0000|6|593.0000|91|594.0000|178|595.0000|1093|596.0000|518||||||||1","TSE|S|2338|143000.000000|11028|6280770|90.0000|84|90.4000|86.8000|2320085000.0000|0|5|89.9000|23|89.8000|4|89.7000|8|89.6000|14|89.5000|251|5|90.0000|128|90.1000|34|90.2000|132|90.3000|88|90.4000|79||||||||1"],"message":[""],"status":["success"]}'''
    quote_data = dict()
    decode_snapshot(quote_data, "TWS", json_file)
    print(quote_data)
