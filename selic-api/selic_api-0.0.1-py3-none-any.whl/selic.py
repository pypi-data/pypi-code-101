'''
Módulo de obtenção dos dados da SELIC por meio da API do BACEN.

Site com a explicação da API da SELIC:
https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic/resource/b73edc07-bbac-430c-a2cb-b1639e605fa8

Neste site:
https://www.bcb.gov.br/htms/selic/selicacumul.asp?frame=1
Há os valores acumulados mensalmente para fins de conferência. Os dados mensais da SELIC constantes no arquivo "dados_selic_mensal.csv" foram obtidos neste site.

Legislação SELIC:
RESOLUÇÃO BCB Nº 46, DE 24 DE NOVEMBRO DE 2020
Dispõe sobre a metodologia de cálculo e a divulgação da Taxa Selic.
https://www.in.gov.br/en/web/dou/-/resolucao-bcb-n-46-de-24-de-novembro-de-2020-290037317

'''
import requests
import json

from datetime import datetime
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_DOWN

import csv



def get_daily_selic_data(init_date: datetime=datetime(year=1986, month=6, day=4), final_date: datetime=None):
    '''
    Get SELIC data from the BACEN API.
    '''
    URL = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json'
    INIT_DATE_PARAMETER = '&dataInicial={init_date}'
    FINAL_DATE_PARAMETER = '&dataFinal={final_date}' # data_inicial e data_final são Strings no formato dd/mm/aaaa.

    final_date = datetime.today() if not final_date else final_date
        
    response = requests.get(URL + INIT_DATE_PARAMETER.format(init_date=init_date.strftime('%d/%m/%Y')) + FINAL_DATE_PARAMETER.format(final_date=final_date.strftime('%d/%m/%Y')))
    if response.ok:
        return list(map(lambda selic_data: {**selic_data, 'data_datetime': datetime.strptime(selic_data['data'], '%d/%m/%Y')}, json.loads(response.text)))
    elif response.status_code == '404':
        # TODO: Verificar a melhor forma de retornar erro que possa ser facilmente verificado.
        return 'Não foi possível obter os dados da SELIC.'


def calc_selic_month(selic_data, month: datetime) -> Decimal:
    '''
    Calculates the accumulated SELIC index on a given month.
    '''
    selic_month_data = list(filter(lambda d: d['data_datetime'] >= month.replace(day=1) and d['data_datetime'] < (month + relativedelta(months=+1)).replace(day=1), selic_data))

    if not selic_month_data:
        raise Exception(f'Não existe dados da SELIC para o mês {month.strftime("%m/%Y")}')

    selic_index = Decimal(1.0)
    for selic in selic_month_data:
        selic_index = selic_index * (1 + Decimal(selic['valor']) / Decimal(100))
    
    return selic_index.quantize(Decimal('.00000001'), rounding=ROUND_HALF_DOWN)


def get_monthly_selic_hard_data():
    selic_monthly_data = []
    with open('dados_selic_mensal.csv') as file:
        reader = csv.reader(file, delimiter=';')
        
        for line in reader:
            selic_monthly_data.append({'month': datetime.strptime(line[0], '%b/%Y') , 'value': Decimal(line[1].replace(',', '.'))})
            
    return selic_monthly_data

def get_monthly_acc_selic_in_period(init_date: datetime, final_date: datetime):
    '''
    Get the monthly accumulated SELIC rate for a given period.
    '''

    if final_date < init_date:
        raise Exception('A data final deve ser igual ou posterior à data inicial!')
    
    curr_date = init_date.replace(day=1)
    months = [curr_date]
    
    while curr_date < final_date.replace(day=1):
        curr_date = curr_date + relativedelta(months=+1)
        months.append(curr_date)
    
    selic_data = get_daily_selic_data(init_date.replace(day=1), final_date.replace(day=1) + relativedelta(months=+1) + relativedelta(days=-1)) # Como a taxa é acumulada mensalmente, o dia da data final tem que ser o último dia do mês e o primeiro da data inicial.
    return [{'month': month, 'selic_acc_rate': calc_selic_month(selic_data, month) - Decimal('1')} for month in months]



