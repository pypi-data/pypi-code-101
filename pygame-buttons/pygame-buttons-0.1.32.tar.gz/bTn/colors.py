MAX=255
MIN=0
BLACK=3*[MIN]
WHITE=3*[MAX]
GREEN=(MIN,MAX,MIN)
BLUE=(72,61,139)
GRAY=[96]*3
RED=(220,20,60)
YELLOW=[MAX for i in range(2)]+[MIN]
if __name__=="__main__":
  print ("colors:\n",globals())