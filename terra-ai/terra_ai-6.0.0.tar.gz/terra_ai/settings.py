SERVER = 'https://storage.googleapis.com/terra_ai/DataSets'

DATASET_NAMES = ('молочная_продукция', 'автобусы', 'квартиры')
param_datasets = {    
    DATASET_NAMES[0] : 
        {'archive' : 'milk',
        'info' : 'Вы скачали базу с изображениями бутылок молока',
        'task' : 'классификация изображений',
        'sampling_size' : (96, 53, 3),
        'classes' : ['Parmalat', 'Кубанский_молочник', 'Кубанская_буренка']
        },
    DATASET_NAMES[1] : 
        {'archive' : 'bus',
        'info' : 'Вы скачали базу с изображениями входящих и выходящих пассажиров в автобус',
        'task' : 'классификация изображений',
        'sampling_size' : (128, 64, 3),
        'classes' : ['Входящий', 'Выходящий']
        },
    DATASET_NAMES[2] : 
        {'archive' : 'flats',
        'info' : 'Загружена база квартир',
        'task' : 'регрессия квартир',
        'sampling_size' : (109, 2000),
        },
    }