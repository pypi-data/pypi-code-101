from hyload.util import getCurTime
import time,sys,json,socket,os,gevent
import http.client
from urllib.parse import quote_plus




def getCommandArg(argName):
    # 检查参数
    for arg in sys.argv[1:]:
        if f'{argName}=' in arg:
            value = arg.replace(f'{argName}=','')
            return value
    
    return None

# 控制台程序地址
ConsoleAddr = getCommandArg('console')

# 统计数据文件
StatsFile = getCommandArg('statsfile')

if ConsoleAddr:
    print (f'Console addr:{ConsoleAddr}')
    # consoleConnection = http.client.HTTPConnection(
    #                             ConsoleAddr,  #ConsoleAddr 'httpbin.org'
    #                             timeout=0.3)

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    parts = ConsoleAddr.split(':')
    UDPServerAddr = parts[0],int(parts[1])
    print(UDPServerAddr)

if StatsFile:
    os.makedirs(os.path.dirname(StatsFile),exist_ok=True)
    foStats = open(StatsFile,'wb')

class Stats:

    @classmethod
    def clear(cls):
        cls.startTime = getCurTime()

        cls.connectionNumber = 0 # 连接数量统计

        cls.totalSend = 0
        cls.totalRecv = 0
        cls.totalTimeout = 0
        cls.totalError = 0

        # 响应时长区段统计
        cls.resptimerange ={
            '<100ms':      0,
            '100-500ms':   0,
            '500-1000ms':  0,
            '1000-3000ms': 0,
            '>=3000ms':    0,
        } 
        
        cls.rpsTable = {}
        cls.tpsTable = {}
        cls.responseTimeTable = {}
        cls.timeoutTable = {}
        cls.errorTable = {}

        cls.runFlag = False

        cls.logFh = None


    @classmethod
    def start(cls):
        cls.clear()
        cls.runFlag = True  # 启动标识

        gevent.spawn(cls.runStats)


    
                

    @classmethod
    def runStats(cls):

        def sendStatsToConsoleTcp(stats):
            if not ConsoleAddr:
                return
                
            consoleConnection = http.client.HTTPConnection(
                                ConsoleAddr,  #ConsoleAddr 'httpbin.org'
                                timeout=5)

            # print('send request to console----------')
            try:
                consoleConnection.request('GET', 
                         '/stats?value=' + quote_plus(json.dumps(stats)), 
                         
                        #  '/get?'+ quote_plus(json.dumps(stats).encode()), 
                         body=None,
                         headers={
                                'User-Agent' : "BYLOAD TESTER"
                            })                
                
                httpResponse = consoleConnection.getresponse()
                
                httpResponse.close()

            except Exception as e:
                print(f'send stats to console failed! {e}')


        def sendStatsToConsoleUdp(statsBytes):
            if not ConsoleAddr:
                return
                           
            
            # print('send request to console----------')
            try:
                UDPClientSocket.sendto(
                    statsBytes,
                    UDPServerAddr)                
                                

            except Exception as e:
                print(f'send stats to console failed! {e}')
                
                

        def statsOneTable(lastSecond,
                          curTable,
                          tableName,
                          action,
                          statsOneSecond):

            # 如果前1秒 有记录， 打印出记录，并且加入发送给console的信息里
            if lastSecond in curTable:
                print(f'{lastSecond} s: {action} {curTable[lastSecond]:6}')
                statsOneSecond[tableName] = curTable[lastSecond]
                curTable.pop(lastSecond)
            # else:
            #     statsOneSecond[tableName] = 0

        # 总是发送上一秒的统计，因为当前秒还没有结束，总计发送接收消息数量统计没有结束
        while True:

            if not cls.runFlag:
                break

            # check every 0.8 seconds
            time.sleep(0.4)

            curTime = getCurTime()

            # get last second to measure
            lastSecond = int(curTime) - 1

            #  请求个数 数据
            statsOneSecond = {'t':lastSecond}

            statsOneTable(lastSecond,cls.rpsTable,'rps','send',statsOneSecond)

            statsOneTable(lastSecond,cls.timeoutTable,'tops','timeout',statsOneSecond)

            statsOneTable(lastSecond,cls.errorTable, 'eps','error',statsOneSecond)

            # 每次发送接收消息，都会调用 oneSent/oneRecv 更新 cls.tpsTable
            # 如果上一秒对应 key 不在 tpsTable 中 
            # 表示 要么时上1秒没有收发数据，要么是 上1秒的统计已经发送出去 
            # 这次都不需要发送统计
            if lastSecond not in cls.tpsTable:       
                continue   

                
            # 如果上1秒统计数据存在，表示上1秒的数据还没有发送出去   
            count = cls.tpsTable[lastSecond]
            avgRespTime = cls.responseTimeTable[lastSecond]/count  
            print(f'{lastSecond} s: recv {count:6} | avg lantency {avgRespTime:.4f}')

            statsOneSecond['tps'] = count
            statsOneSecond['respTimeSum'] = round(cls.responseTimeTable[lastSecond],4)
            statsOneSecond['avgRespTime'] = round(avgRespTime,4)

            cls.tpsTable.pop(lastSecond)
            cls.responseTimeTable.pop(lastSecond)
 
            # 如果上一秒没有发送/接收消息，这次不需要发送统计
            if len(statsOneSecond) == 1:
                continue

            # 否则加上 累计汇总 统计信息，一起发出去
            total = {}
            total['send'] = cls.totalSend
            total['recv'] = cls.totalRecv

            if  cls.totalTimeout > 0 :
                total['timeout'] = cls.totalTimeout
            if  cls.totalError > 0 :
                total['error'] = cls.totalError

            # 响应时长区段统计，去掉为0的            
            total.update({ tr:count  for tr,count in  cls.resptimerange.items() if count>0})

            statsOneSecond['total'] = total
            
            
            # 统计对象数据序列化为字节
            statsBytes = json.dumps(statsOneSecond).encode()

            # 发给console集中显示
            if ConsoleAddr:
                sendStatsToConsoleUdp(statsBytes)

            
            if StatsFile:
                foStats.write(statsBytes+b'\n')
                foStats.flush()

            # 发送到 console的 并发连接数量 数据
            # 目前侦测到连接断开比较麻烦，暂时先不做并发连接的统计
            # sendStatsToConsoleUdp({'connNum':cls.connectionNumber})

    @classmethod
    def stop(cls):
        # wait for more than 1 second, so stats greenlet could count last second
        time.sleep(1.2)
        cls.runFlag = False

    @staticmethod
    def measurePerSecond(recTable,addAmount,curTime=None):
        
        if curTime is None:
            curTime = getCurTime()

        # get cur second to measure
        curSecond = int(curTime)
        # new second to stats
        if curSecond not in recTable:          
            recTable[curSecond] = addAmount
        # add one to  stats
        else:
            recTable[curSecond] += addAmount
        
        return curTime

    @classmethod
    def oneSent(cls):

        cls.totalSend +=1

        sentTime = cls.measurePerSecond(cls.rpsTable,1)


        return sentTime


    @classmethod
    def connectionNumIncreace(cls):
        cls.connectionNumber +=1

    @classmethod
    def connectionNumDecreace(cls):
        cls.connectionNumber -=1


        
    @classmethod
    def oneRecv(cls,sentTime):
        
        cls.totalRecv +=1
                
        recvTime = cls.measurePerSecond(cls.tpsTable,1)
        duration = recvTime - sentTime
        cls.measurePerSecond(cls.responseTimeTable,duration,recvTime)

        
        if duration < 0.1 :
            cls.resptimerange['<100ms'] += 1
        elif 0.1<= duration < 0.5 :
            cls.resptimerange['100-500ms'] += 1
        elif 0.5<= duration < 1 :
            cls.resptimerange['500-1000ms'] += 1
        elif 1<= duration < 3 :
            cls.resptimerange['1000-3000ms'] += 1
        else :
            cls.resptimerange['>=3000ms'] += 1

        return recvTime

    @classmethod
    def oneTimeout(cls):

        cls.totalTimeout += 1

        cls.measurePerSecond(cls.timeoutTable, 1)

        return


    @classmethod
    def oneError(cls):

        cls.totalError += 1

        cls.measurePerSecond(cls.errorTable, 1)

        return

Stats.clear()