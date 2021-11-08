from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Flatten, Conv2D, Dense, concatenate, Activation # Импортируем стандартные слои keras
from tensorflow.keras.callbacks import ModelCheckpoint, LambdaCallback, ReduceLROnPlateau
from tensorflow.keras.optimizers import Nadam
import time, random, gc, pickle
import numpy as np
import pandas as pd
from IPython import display
from termcolor import colored
import matplotlib.pyplot as plt
from . import utils

class TerraModel():    
    def __init__(self, layers, param):
        self.model = None
        self.input_size = param['sampling_size']
        self.layers = layers
        if isinstance(layers, tuple):            
            self.create_fmodel(param['task'])
        else:            
            self.create_model(param['task'])
        
    def create_model(self, task, rep = False):
        task = task.lower()
        self.task = task
        if task == 'классификация изображений':
            params = {'loss':'sparse_categorical_crossentropy',
                      'opt':'adam',
                       'metrics':['accuracy']}
        self.create_image_classification_model(
            self.layers + '-softmax',
            params,
            rep
        )
        
    def create_fmodel(self, task, rep = False):
        task = task.lower()
        self.task = task
        input1 = Input(self.input_size[0],)
        input2 = Input(self.input_size[1],)
                  
        layers = self.layers[0].split()
        x1 = self.create_layer(layers[0]) (input1)
        layers[-1]+='-linear'
        for i in range(1, len(layers)):
            layer = self.create_layer(layers[i])
            assert layer!=0, 'Невозможно добавить указанный слой: '+layer
            x1 = self.create_layer(layers[i]) (x1)

        layers = self.layers[1].split()
        x2 = self.create_layer(layers[0]) (input2)
        layers[-1]+='-linear'
        for i in range(1, len(layers)):
            layer = self.create_layer(layers[i])
            assert layer!=0, 'Невозможно добавить указанный слой: '+layer
            x2 = self.create_layer(layers[i]) (x2)
           
        x = concatenate([x1, x2])        
        layers = self.layers[2].split()        
        layers[-1]+='-linear'
        x3 = self.create_layer(layers[0]) (x)
        for i in range(1, len(layers)):
            layer = self.create_layer(layers[i])
            assert layer!='0', 'Невозможно добавить указанный слой: '+layer
            x3 = self.create_layer(layers[i]) (x3)        
        self.model = Model([input1, input2], x3)
        self.model.compile(loss="mae", optimizer=Nadam(learning_rate=1e-3), metrics=["mae"])        
        print('Создана модель нейронной сети!')
        
    def create_image_classification_model(self, layers, params, rep):
        self.model = Sequential()        
        layers = layers.split()
        layer = self.create_layer(layers[0], входной_размер=self.input_size)
        self.model.add(layer)   
        for i in range(1, len(layers)):
            layer = self.create_layer(layers[i])
            self.model.add(layer)
        if not rep:
            print('Создана модель нейронной сети!')
        if 'metrics' in params:
            self.model.compile(loss=params['loss'], optimizer = params['opt'], metrics=params['metrics'])
        else:
            self.model.compile(loss=params['loss'], optimizer = params['opt'])
    
    def create_layer(self, layer, **kwargs):
        args={}
        if 'входной_размер' in kwargs:
            args['input_shape'] = kwargs['входной_размер']  
        параметры = [layer]
        act = 'relu'
        if '-' in layer:
            параметры = layer.split('-')
        if параметры[0].upper() == 'ПОЛНОСВЯЗНЫЙ':    
            if len(параметры)>2:
                act = параметры[2]
            return Dense(int(параметры[1]), activation=act, **args)
        elif параметры[0].upper() == 'СВЕРТОЧНЫЙ2D':
            if len(параметры)<5:
                act = 'relu'
                pad='same'
            else:
                act = параметры[4]
                pad = параметры[3]
            if any(i in '()' for i in параметры[2]):
                return Conv2D(int(параметры[1]), (int(параметры[2][1]),int(параметры[2][3])), padding=pad,activation=act, **args)
            else:
                return Conv2D(int(параметры[1]), int(параметры[2]), padding=pad,activation=act, **args)
        elif параметры[0].upper() == 'ВЫРАВНИВАЮЩИЙ':
            if 'input_shape' in args:
                return Flatten(input_shape=args['input_shape'])
            else:
                return Flatten()   
        else:
            assert False, f'Невозможно добавить указанный слой: \'{параметры[0]}\'.\
                Возможно вы имели ввиду \'{check_for_errors.check_word(параметры[0], "layer")}\'.'
                
    def train_model(self, epochs, repeats, sampling=[]):
        x_train = sampling[0]
        x_test = sampling[2]
        y_train = sampling[1]
        y_test = sampling[3]
        batch_size = 64
        global result, best_result, idx_best, best_result_on_train_arr
        cur_time = time.time()
        
        if repeats > 0:
            cur_time = time.time()
            global stage_result, stage_best_result
            stage_result = ''
            stage_best_result = []
            best_result_on_train_arr = []
            stage_history = []
            for start in range(repeats):
                del(self.model)
                gc.collect()
                self.create_model(self.task, rep = True)
                result = ''
                idx_best = 0
                best_result = 0
                best_result_on_train = 0
                filepath="model.h5"

                model_checkpoint_callback = ModelCheckpoint(
                    filepath=filepath,
                    save_weights_only=True,
                    monitor='val_loss',
                    mode='min',
                    save_best_only=True)
                cur_time = time.time()
                
                def on_epoch_end(epoch, log):
                    global cur_time, result, best_result, idx_best, stage_result, текущая_эпоха, stage_best_result, best_result_on_train, best_result_on_train_arr
                    текущая_эпоха = epoch
                    k = list(log.keys()) 
                    p1 = 'Запуск №' + str(start+1)
                    p2 = p1 + ' '* (12 - len(p1)) + 'Время обучения: ' + str(round((time.time()-cur_time) * epochs,1)) +'c'
                    p3 = p2 + ' '* (34 - len(p2)) + 'Точность на обучающей выборке: ' + str(round(log[k[1]]*100,1))+'%'
                    if len(k)>2:
                        p4 = p3 + ' '* (77 - len(p3)) + 'Точность на проверочной выборке: ' + str(round(log[k[3]]*100,1))+'%'
                        result += p4 + '\n'
                        if log[k[3]]*100 >= best_result:
                            best_result = log[k[3]]*100
                            best_result_on_train = log[k[1]]*100
                            idx_best = epoch
                    else:
                        result += p3 + '\n'
                        if log[k[1]]*100 >= best_result:
                            best_result = log[k[1]]*100
                            best_result_on_train = log[k[1]]*100
                            idx_best = epoch 
                    if (текущая_эпоха+1) == epochs:
                        result = result.split('\n')
                        stage_best_result.append(best_result)
                        best_result_on_train_arr.append(best_result_on_train)
                        for i in range(len(result)):
                            if i == idx_best:
                                best_in_epoc = result[i]
                                stage_result += best_in_epoc + '\n'
                        print(best_in_epoc)
                    cur_time = time.time()

                def on_epoch_begin(epoch, log):
                    global cur_time
                    cur_time = time.time()
                    
                myCB = LambdaCallback(on_epoch_end = on_epoch_end, on_epoch_begin=on_epoch_begin)              
                history = self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data = (x_test, y_test), callbacks=[model_checkpoint_callback, myCB], verbose = 0)
                stage_history.append(history)
                self.model.load_weights('model.h5')
                self.model.save('model_s.h5')

            display.clear_output(wait=True)
            stage_result = stage_result.split('\n')
            stage_best_result = np.asarray(stage_best_result)
            best_result_on_train_arr = np.asarray(best_result_on_train_arr)
            idx_best_stage = np.argmax(stage_best_result)

            for i in range(len(stage_result)):
                s = stage_result[i]
                if i == idx_best_stage:
                    s = colored(stage_result[i], color='white', on_color='on_green')
                print(s)
            print('Средняя точность на обучающей выборке:   ' , str(round(np.mean(best_result_on_train_arr), 1)) +  '%', '\n' 
                  'Средняя точность на проверочной выборке: ' , str(round(np.mean(stage_best_result), 1)) + '%')

            keys = list(stage_history[idx_best_stage].history.keys())
            data={
                "Обучающая выборка": best_result_on_train_arr,
                "Проверочная выборка": stage_best_result
                }
            df=pd.DataFrame(data)
            df.plot(kind="bar",stacked=False,figsize=(10,8))
            plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
            plt.hlines(round(np.mean(stage_best_result)), -1, len(stage_history), color='green')
            plt.title('График точности обучения, на лучшем запуске') # Выводим название графика         
            plt.show()


        else:
            result = ''
            idx_best = 0
            best_result = 0            
            model_checkpoint_callback = ModelCheckpoint(
                filepath="model.h5",
                save_weights_only=True,
                monitor='val_loss',
                mode='min',
                save_best_only=True)              
            cur_time = time.time()
            def on_epoch_end(epoch, log):
                k = list(log.keys())
                global cur_time, result, idx_best, best_result
                p = f'Эпоха №{epoch+1}'.ljust(12) \
                    + f'Время обучения: {round(time.time()-cur_time,1)}c'.ljust(24) \
                    + f'Точность на обучающей выборке: {round(log[k[1]]*100,1)}%'.ljust(44) \
                    + f'Точность на проверочной выборке: {round(log[k[3]]*100,1)}%'
                result += p + '\n'
                if log[k[3]]*100 >= best_result:
                    best_result = log[k[3]]*100
                    idx_best = epoch
                print(p)
                cur_time = time.time()

            def on_epoch_begin(epoch, log):
                global cur_time
                cur_time = time.time()

            myCB = LambdaCallback(on_epoch_end = on_epoch_end, on_epoch_begin=on_epoch_begin)            
            history = self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data = (x_test, y_test), callbacks=[model_checkpoint_callback, myCB], verbose = 0)
            
            self.model.load_weights('model.h5')
            self.model.save('model_s.h5')
            display.clear_output(wait=True)
            result = result.split('\n')
            for i in range(len(result)):
                s = result[i]
                if i == idx_best:
                    s = colored(result[i], color='white', on_color='on_green')
                print(s)
            keys = list(history.history.keys())
            plt.plot(history.history[keys[1]], label ='Обучающая выборка') # Визуализируем график точности на обучающей выборке
            if len(keys)>2:
                plt.plot(history.history['val_'+keys[1]], label ='Проверочная выборка') # Визуализируем график точности на проверочной выборке
            plt.legend() # Выводим подписи на графике
            plt.title('График точности обучения') # Выводим название графика
            plt.show()
            return history
    
    def train_fmodel(self, epochs, sampling=[]):
        cur_time = time.time()
        global loss, val_loss, history, result, best_result, idx_best
        result = ''
        idx_best = 0
        best_result = 50000000
        filepath="model.h5"
        batch_size = 256
        model_checkpoint_callback = ModelCheckpoint(
            filepath=filepath,
            save_weights_only=True,
            monitor='val_loss',
            mode='min',
            save_best_only=True)

        def on_epoch_end(epoch, log):
            global cur_time, loss, val_loss, result, best_result, idx_best, count_len
            yScaler = pickle.load(open('yscaler.pkl','rb'))
            pred = self.model.predict(sampling[2]) #Полуаем выход сети на проверочно выборке
            predUnscaled = yScaler.inverse_transform(pred).flatten() #Делаем обратное нормирование выхода к изначальным величинам цен квартир
            yTrainUnscaled = yScaler.inverse_transform(sampling[3]).flatten() #Делаем такое же обратное нормирование yTrain к базовым ценам
            delta = predUnscaled - yTrainUnscaled #Считаем разность предсказания и правильных цен
            absDelta = abs(delta) #Берём модуль отклонения

            pred2 = self.model.predict(sampling[0]) #Полуаем выход сети на проверочно выборке
            predUnscaled2 = yScaler.inverse_transform(pred2).flatten() #Делаем обратное нормирование выхода к изначальным величинам цен квартир
            yTrainUnscaled2 = yScaler.inverse_transform(sampling[1]).flatten() #Делаем такое же обратное нормирование yTrain к базовым ценам
            delta2 = predUnscaled2 - yTrainUnscaled2 #Считаем разность предсказания и правильных цен
            absDelta2 = abs(delta2) #Берём модуль отклонения
            loss.append(sum(absDelta2) / (1e+6 * len(absDelta2)))
            val_loss.append(sum(absDelta) / (1e+6 * len(absDelta)))
            
            p1 = 'Эпоха №' + str(epoch+1)
            p2 = p1 + ' '* (10 - len(p1)) + 'Время обучения: ' + str(round(time.time()-cur_time,2)) +'c'
            p3 = p2 + ' '* (33 - len(p2)) + 'Ошибка на обучающей выборке: ' + str(round(sum(absDelta2) / (1e+6 * len(absDelta2)), 3))+'млн'
            p4 = p3 + ' '* (77 - len(p3)) + 'Ошибка на проверочной выборке: ' + str(round(sum(absDelta) / (1e+6 * len(absDelta)), 3))+'млн'
            result += p4 + '\n' 
            
            a = round(sum(absDelta) / (1e+6 * len(absDelta)), 3)
            if a < best_result:
                best_result = a
                idx_best = epoch
            print(p4)           

        def on_train_begin(log):
            global cur_time, loss, val_loss
            loss=[]
            val_loss = []

        def on_epoch_begin(epoch, log):
            global cur_time
            cur_time = time.time()

        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                                      patience=5, min_lr=1e-6)

        myCB = LambdaCallback(on_train_begin=on_train_begin, on_epoch_end = on_epoch_end, on_epoch_begin=on_epoch_begin)
        myCB23 = LambdaCallback(on_epoch_end = on_epoch_end, on_epoch_begin=on_epoch_begin)
        self.model.fit(sampling[0], sampling[1], batch_size=batch_size, epochs=epochs, validation_data = (sampling[2], sampling[3]), callbacks=[model_checkpoint_callback, myCB, reduce_lr], verbose = 0)
        self.model.load_weights('model.h5')
        self.model.save('model_s.h5')

        display.clear_output(wait=True)
        result = result.split('\n')
        self.res = result
        self.l= loss
        self.vl = val_loss
        idx = 0
        for i in range(len(result)):
            s = result[i]
            if i == idx_best:
                s = colored(result[i], color='white', on_color='on_green')
            print(s)
        plt.figure(figsize=(12, 6)) # Создаем полотно для визуализации  
        plt.plot(loss, label ='Обучающая выборка') # Визуализируем график ошибки на обучающей выборке
        plt.plot(val_loss, label ='Проверочная выборка') # Визуализируем график ошибки на проверочной выборке
        plt.legend() # Выводим подписи на графике
        plt.title('График ошибки обучения') # Выводим название графика
        plt.show()
  
    def test_model(self, data, param, test_sampling):
        if param['task']=='классификация изображений':
            self.test_model_image_classification(param, test_sampling)
        if param['task']=='регрессия квартир':
            self.test_model_regression(data)
        
    def test_model_image_classification(self, param, test_sampling):        
        for i in range(5):
            number = np.random.randint(test_sampling[0].shape[0]) # Задаем индекс изображения в тестовом наборе
            sample = test_sampling[0][number]            
            print('Тестовое изображение:')
            plt.imshow(sample, cmap='gray') # Выводим изображение из тестового набора с заданным индексом
            plt.axis('off') # Отключаем оси
            plt.show()
            sample = sample.reshape((1 + self.model.input.shape[1:]))
            pred = self.model.predict(sample)[0] # Распознаем изображение с помощью обученной модели
            print()
            print('Результат предсказания модели:')
            dicts = {}
            classes = param['classes']
            for i in range(len(classes)):
                dicts[classes[i]] = round(100*pred[i],2)
                print(f'   класс {classes[i]}:'.ljust(40), round(100*pred[i],1),'%',sep='')
            print('---------------------------')
            answer = str(classes[test_sampling[1][number]])
            if len(test_sampling[1])>0:
                if utils.keywithmaxval(dicts) == answer:
                    print('Правильный ответ: ', utils.out_green(answer))
                    print('---------------------------')
                    print()
                    print()
                elif utils.keywithmaxval(dicts) != classes[test_sampling[1][number]]:
                    print('Правильный ответ: ', utils.out_red(answer))
                    print('---------------------------')
                    print()
                    print()  
        
    def test_model_regression(self, данные):
        df = pd.DataFrame(
            np.array([[1, данные[0], str(данные[1])+данные[2][0], str(данные[3])+'/'+str(данные[4])+' П', данные[5],  данные[6], str(данные[7])+'/12/12', 0, 0,0,0,0,0,данные[8] ]]),
            columns=['Комнат', 'Метро / ЖД станции', 'От станции', 'Дом', 'Балкон', 'Санузел', 'Площадь', 'Цена, руб.', 'ГРМ', 'Бонус агенту', 'Дата', 'Кол-во дней в экспозиции', 'Источник', 'Примечание'],
        )
        data = df.values #Вытаскиваем данные в numpy array
        oneRoomMask = [utils.getRoomsCount(d, 30) == 1 for d in data] #Делаем маску однокомнатных квартир, принцип (getRoomsCount(d, 30) == 1)
        data1 = data[oneRoomMask] #В data1 оставляем только однокомнатные квартиры
        xTrain = utils.getXTrain(data1, df)
        yTrain = utils.getYTrain(data1)
        xTrainC, allTextComments = utils.getXTrainComments(data1) #Создаём обучающую выборку по текстам и большо текст для словаря
        allWords = utils.text2Words(allTextComments) #Собираем полный текст в слова
        allWords = allWords[::10] #Берём 10% слов (иначе словарь слишком долго формируется)
        vocabulary = utils.createVocabulary(allWords) #Создаём словарь
        xTrainC01 = utils.changeSetToIndexes(xTrainC, vocabulary, 2000) #Преобразеум xTrain в bag of words
        #Нормируем размер квартиры в xTrain  
        xTrainScaled = xTrain.copy()
        xScaler = pickle.load(open('xscaler.pkl','rb'))
        yScaler = pickle.load(open('yscaler.pkl','rb'))
        xTrainScaled[:,-1] = xScaler.transform(xTrain[:,-1].reshape(-1, 1)).flatten() #Нормируем данные нормировщиком
        
        pred = self.model.predict([xTrainScaled, xTrainC01]) #Полуаем выход сети на проверочно выборке
        predUnscaled = yScaler.inverse_transform(pred).flatten() #Делаем обратное нормирование выхода к изначальным величинам цен квартир
        print('Цена квартиры: ' + str(int(predUnscaled[0]//1000000))+'млн  '+str(int(predUnscaled[0]%1000000//1000))+'тыс рублей')


                