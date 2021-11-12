from ejtraderIQ import IQOption


api = IQOption('tribolinux@gmail.com','tribopass@123','DEMO')


for _ in range(5):
   id = api.buy(1,'EURUSD','M1')
   win = api.checkwin(id)
   print(win)
