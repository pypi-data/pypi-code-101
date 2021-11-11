from vosk import Model, KaldiRecognizer, SetLogLevel
import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import pyaudio
import wave
import json
import  keyboard

import cn2an

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))





class voiceIO(object):
    def __init__(self):
        #语音输入的路径
        self.wavSavePath=''
        self.hanzi=''
        self.finalResult=''
    #这个函数不需要修改
    def voiceInit(self):
        q = queue.Queue()
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        args, remaining = parser.parse_known_args()
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            '-f', '--filename', type=str, metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-m', '--model', type=str, metavar='MODEL_PATH',
            help='Path to the model')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        args = parser.parse_args(remaining)
        return args,remaining,parser,q
    def voiceOut1(self,args,remaining,parser,q):
        try:
            if args.model is None:
                args.model = "model"
            if not os.path.exists(args.model):
                print("Please download a model for your language from https://alphacephei.com/vosk/models")
                print("and unpack as 'model' in the current folder.")
                parser.exit(0)
            if args.samplerate is None:
                device_info = sd.query_devices(args.device, 'input')
                # soundfile expects an int, sounddevice provides a float:
                args.samplerate = int(device_info['default_samplerate'])

            model = vosk.Model(args.model)
            if args.filename:
                dump_fn = open(args.filename, "wb")
            else:
                dump_fn = None
            print(1)
            with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device, dtype='int16',
                                   channels=1, callback=callback):
                print('#' * 80)
                print('Press Ctrl+C to stop the recording')
                print('#' * 80)

                rec = vosk.KaldiRecognizer(model, args.samplerate)
                printindex=0
                while True:
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        # print(rec.Result())
                        b=1
                    else:
                        # print(rec.PartialResult())
                        hz = json.loads(rec.PartialResult())
                        hanzi1 = hz["partial"]
                        hanzi1 = hanzi1.replace(' ', '')  # [5:]
                        self.hanzi = hanzi1.replace('[FIL]', '')
                    if dump_fn is not None:
                        dump_fn.write(data)
                    print(self.hanzi)
                    if keyboard.is_pressed('w'):
                        break
        except KeyboardInterrupt:
            print('\nDone')
            parser.exit(0)
        except Exception as e:
            parser.exit(type(e).__name__ + ': ' + str(e))
    #录音
    #参数介绍
    # wavSavePath   录音保存的路径
    #RECORD_SECONDS   这个是录音长度
    #wav的数据可以直接被DAC（声卡）读取并使用
    def get_audio(self,wavSavePath,RECORD_SECONDS):
        # input_filename = "input.wav"  # 麦克风采集的语音输入
        # input_filepath = "model/audioInput"  # 输入文件的path
        # in_path = input_filepath + '/' + input_filename
        self.wavSavePath=wavSavePath
        aa = str(input("是否开始录音？   （y/n）"))
        if aa == str("y"):
            CHUNK = 256                     #分块
            FORMAT = pyaudio.paInt16        #采样深度
            CHANNELS = 1                        # 声道数
            RATE = 8000                         # 采样率HZ
            RECORD_SECONDS = RECORD_SECONDS      #记录多长时间
            WAVE_OUTPUT_FILENAME = self.wavSavePath
            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            print("*" * 10, "开始录音：请在"+str(RECORD_SECONDS)+"秒内输入语音")
            #每一帧放过在一个
            frames = []
            #开始录制
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            print("*" * 10, "录音结束\n")
            # 录制完毕
            stream.stop_stream()
            stream.close()
            p.terminate()
            #写到文件里
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
        elif aa == str("n"):
            exit()
        else:
            print("无效输入，请重新选择")
    #这个是对录音之后的语音进行解码
    def hanZiFormat(self):
        hz=json.loads(self.finalResult)
        hanzi1=hz['text']
        self.hanzi=hanzi1.replace(' ','')     #[5:]
        self.hanzi=self.hanzi.replace('[FIL]','')
        self.hanzi=cn2an.transform(self.hanzi)
#,Model="C:\\Users\\86158\\Desktop\\vosk-api-master\\python\\example\\model"
    def voiceOut2(self,args,remaining,parser,q,wavFilePath,ModelPath):
        ModelPath1= ModelPath
        SetLogLevel(0)
        if not os.path.exists(ModelPath1):
            print(
                "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
            exit(1)
        # wf = wave.open('test.wav', "rb")
        #打开语音文件
        wf = wave.open(wavFilePath, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            exit(1)
            ModelPath1
           # "C:\\Users\\86158\Desktop\\vosk-api-master\\python\\model"
        model = Model(ModelPath1)
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        while True:
            #里面的参数表示采样频率
            #也可以用wf.getnframes()获得
            #print(wf.getframerate())
            #文件长度计算
            data = wf.readframes(8000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                pass
                # print(rec.Result())
            else:
                pass
            # hanzi1=
        #这一部分是汉子格式处理，输出为字符串
        self.finalResult=rec.FinalResult()
        self.hanZiFormat()
        print('语音解码结果')
if (__name__ == '__main__'):
#录音存放-汉字显示
    ##生成的语音文件在model\\audioInput\\input.wav
    ##这个不需要修改
    p2=voiceIO()
    #第一个参数是语音保存路径
    #第二个参数是录音时间需要修改
    p2.get_audio("C:\\Users\\86158\\Desktop\\vosk-api-master\\python\model\\audioInput\\input.wav",20)
    #不需要修改
    args, remaining, parser, q = p2.voiceInit()
    #最后一个参数可以修改，是语音保存的路径，转汉语
    p2.voiceOut2(args, remaining, parser, q ,p2.wavSavePath,"C:\\Users\\86158\Desktop\\vosk-api-master\\python\\model")
    # p2.voiceOut2(args, remaining, parser, q, "model\\audioInput\\input.wav")
    print(p2.hanzi)
#实时录音实时显示
    # p=voiceIO()
    # args,remaining,parser,q=p.voiceInit()
    # p.voiceOut1(args,remaining,parser,q)
    # print(123)
    # print(p.hanzi)
    # output = cn2an.transform(p.hanzi)
    # print(output)
