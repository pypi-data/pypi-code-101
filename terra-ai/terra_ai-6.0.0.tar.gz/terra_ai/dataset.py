import gdown, os, random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from . import settings, utils, models
from IPython import display
from PIL import Image 

class Dataset():
    def __init__(self, ds_name):
        self.dataset_name = ds_name.lower() # название датасета
        self.sampling = [[],[],[],[]] # выборки
        
    def load_dataset(self):
        print('Загрузка данных')
        print('Это может занять несколько минут...')
        archive_name = settings.param_datasets[self.dataset_name]['archive']
        url = settings.SERVER + '/' +archive_name
        gdown.download(url+'.zip', archive_name, quiet=True) # Скачиваем файл по указанному URL
        gdown.download(url+'_sampling.zip', archive_name+'_sampling', quiet=True) # Скачиваем файл по указанному URL
        utils.unzip_archive(
            from_ = archive_name,
            to_ = os.path.join(self.dataset_name)
            )
        utils.unzip_archive(
            from_ = archive_name+'_sampling',
            to_ = ''
            )
        display.clear_output(wait=True)
        print('Загрузка данных завершена \n')
        print('url:', url)
        print(settings.param_datasets[self.dataset_name]['info'])
    
    def show_samples(self):
        # молочная продукция
        if self.dataset_name == settings.DATASET_NAMES[0]:
            if not os.path.exists(self.dataset_name):
                print(f'Загрузите базу для \'{self.dataset_name}\' для корректной работы.')
                return
            size=(256, 512)
            fig = plt.figure(figsize=(10,10))
            classes = sorted(os.listdir(self.dataset_name))
            for i in range(len(classes)):
                images = sorted(os.listdir(os.path.join(self.dataset_name, classes[i])))
                img_path = os.path.join(self.dataset_name, classes[i], random.choice(images))
                img = Image.open(img_path)  # Открытие обрабатываемого файла
                img = img.resize(size)                
                img = np.array(img)       
                ax = fig.add_subplot(1, 3, i+1, xticks=[], yticks=[])
                plt.imshow(img)
        # автобусы
        elif self.dataset_name == settings.DATASET_NAMES[1]:
            if not os.path.exists(self.dataset_name):
                print(f'Загрузите базу для \'{self.dataset_name}\' для корректной работы.')
                return        
            size=(150, 256)
            entering_idx = [1,170,338,1200,1536,
                      1762,1830,1942,2312,2414,
                      2455,2712,3513,3657,3744,
                      3761,3792,3797,3826,3877,
                      3904,3945,3972,3993,4140]
            getting_off_idx = [184,445,653,1220,1241,
                        1283,1367,1388,1409,1453,
                        1487,1648,1906,2505,2412,
                        2292,1865]
            fig = plt.figure(figsize=(16,10))
            entering_img = sorted(os.listdir(os.path.join(self.dataset_name, 'entering')))
            for i, idx in enumerate(np.random.choice(entering_idx, 5, replace=False)):
                img_path = os.path.join(self.dataset_name, 'entering', entering_img[idx])
                img = Image.open(img_path)  # Открытие обрабатываемого файла
                img = img.resize(size)     
                img = np.array(img)          
                ax = fig.add_subplot(2, 5, i+1, xticks=[], yticks=[])
                ax.set_title('Входящий')
                plt.imshow(img)
            getting_off_img = sorted(os.listdir(os.path.join(self.dataset_name, 'getting_off')))
            for i, idx in enumerate(np.random.choice(getting_off_idx, 5, replace=False)):
                img_path = os.path.join(self.dataset_name, 'getting_off', getting_off_img[idx])
                img = Image.open(img_path)  # Открытие обрабатываемого файла
                img = img.resize(size)
                img = np.array(img)          
                ax = fig.add_subplot(2, 5, i+6, xticks=[], yticks=[])
                ax.set_title('Выходящий')
                plt.imshow(img)
         # квартиры
        elif self.dataset_name == settings.DATASET_NAMES[2]:
            def getRoomsCount(d, maxRoomCount):
                roomsCountStr = d[0] #Получаем строку с числом комнат
                roomsCount = 0
                try:
                    roomsCount = int(roomsCountStr) #Пробуем превратить строку в число
                    if (roomsCount > maxRoomCount): 
                        roomsCount = maxRoomCount #Если число комнат больше максимального, то присваиваем максимальное
                except: #Если не получается превратить строку в число
                    if (roomsCountStr == roomsCountStr): #Проверяем строку на nan (сравнение с самим собой)
                        if ("Ст" in roomsCountStr): #Еcть строка = "Ст", значит это Студия
                            roomsCount = maxRoomCount + 1
                return roomsCount
            df = pd.read_csv('квартиры/moscow.csv', sep=";") #Загружаем данные в data frame
            df = df.iloc[::2,:] #Выбираем нечётные строки, в чётных строках в исходном фрейме пустые строки для комментариев
            data = df.values #Вытаскиваем данные в numpy array
            oneRoomMask = [getRoomsCount(d, 30) == 1 for d in data] #Делаем маску однокомнатных квартир, принцип (getRoomsCount(d, 30) == 1)
            data1 = data[oneRoomMask] #В data1 оставляем только однокомнатные квартиры
            idx = 0
            while idx<5:
                try:
                    i = np.random.randint(0, data1.shape[0])
                    print('* Пример объявления: ')
                    print()
                    print('Количество комнат: ', data1[i][0])
                    print('Площадь квартиры:  ', data1[i][6])
                    print('Метро/ЖД станция:  ', data1[i][1])
                    print('От станции:        ', data1[i][2])
                    print('Дом:               ', data1[i][3])
                    print('Балкон:            ', str(data1[i][4]).replace('nan',''))
                    print('Санузел:           ', str(data1[i][5]).replace('nan',''))
                    s = data1[i][13].replace('/n',' ')
                    s = s.replace('/r',' ')
                    print('Примечание:        ', s)
                    print('-----------')
                    c1 = int(int(data1[i][7])/1e+6)      
                    c2 = int(((int(data1[i][7])/1e+6) - c1) * 1e+3)
                    print('Цена квартиры:     ',  c1, ' млн  ', c2,' тыс рублей', sep='')
                    print('---------------------------------------------------------------------------------------------------------------')
                    print()
                    idx += 1
                except:
                    continue
                
    def create_sampling(self):
        # молочная продукция
        if self.dataset_name == settings.DATASET_NAMES[0] or self.dataset_name == settings.DATASET_NAMES[1]:
            print('Создание наборов данных для обучения модели...')            
            self.sampling[0] = np.load('x_train.npy') # Добавляем в список x_train сформированные данные
            self.sampling[1] = np.load('y_train.npy') # Добавлеям в список y_train значение 0-го класса
            self.sampling[2] = np.load('x_test.npy') # Добавляем в список x_test сформированные данные
            self.sampling[3] = np.load('y_test.npy')# Добавлеям в список y_test значение 0-го класса
            display.clear_output(wait=True)
            print('Размер сформированного массива обучающая_выборка:'.ljust(57), self.sampling[0].shape)
            print('Размер сформированного массива метки_обучающей_выборки:'.ljust(57), self.sampling[1].shape)
            print('Размер сформированного массива тестовая_выборка:'.ljust(57), self.sampling[2].shape)
            print('Размер сформированного массива метки_тестовой_выборки:'.ljust(57), self.sampling[3].shape)
        # квартиры
        if self.dataset_name == settings.DATASET_NAMES[2]:
            print('Создание наборов данных для обучения модели...')            
            self.sampling[0] = (np.load('flats_x_train_1.npy'), np.load('flats_x_train_2.npy')) # Добавляем в список x_train сформированные данные
            self.sampling[1] = np.load('flats_y_train.npy') # Добавлеям в список y_train значение 0-го класса
            self.sampling[2] = (np.load('flats_x_test_1.npy'), np.load('flats_x_test_2.npy')) # Добавляем в список x_test сформированные данные
            self.sampling[3] = np.load('flats_y_test.npy')# Добавлеям в список y_test значение 0-го класса
            display.clear_output(wait=True)
            print('Размер сформированного массива обучающая_выборка (числовые данные):'.ljust(77), self.sampling[0][0].shape)
            print('Размер сформированного массива обучающая_выборка (текстовые данные):'.ljust(77), self.sampling[0][1].shape)
            print('Размер сформированного массива метки_обучающей_выборки:'.ljust(77), self.sampling[1].shape)
            print('Размер сформированного массива тестовая_выборка(числовые данные):'.ljust(77), self.sampling[2][0].shape)
            print('Размер сформированного массива тестовая_выборка(текстовые данные):'.ljust(77), self.sampling[2][1].shape)
            print('Размер сформированного массива метки_тестовой_выборки:'.ljust(77), self.sampling[3].shape)

    def create_model(self, layers):
        self.terraModel = models.TerraModel(layers, settings.param_datasets[self.dataset_name])

    def train_model(self, epochs, repeats):
        if settings.param_datasets[self.dataset_name]['task'] == 'классификация изображений':
            self.terraModel.train_model(epochs, repeats, self.sampling)
        elif settings.param_datasets[self.dataset_name]['task'] == 'регрессия квартир':
            self.terraModel.train_fmodel(epochs, self.sampling)
        
    def test_model(self, data):
        self.terraModel.test_model(data, settings.param_datasets[self.dataset_name], self.sampling[2:])