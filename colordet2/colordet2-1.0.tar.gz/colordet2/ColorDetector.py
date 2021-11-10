from typing import List, Tuple
import numpy as np
import cv2
import imghdr

class ColorDetector:
     def __init__(self, imgpath: str):
          try: 
               if imghdr.what(imgpath):
                    self.img = cv2.imread(imgpath)
                    self.imgArray = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
                    self.size = int( self.imgArray.size / 3 )
               else:
                    print('Image file is not supported or the file is broken, try another image')
          except FileNotFoundError:
               print('Image not found, try another path')
               
          self.colorList = []
          self.colorDicts = [
               {'color' : 'black' , 'tb': np.array([180, 255, 35]) , 'bb': np.array([0, 0, 0])    },
               {'color' : 'white' , 'tb': np.array([180, 40, 255]) , 'bb': np.array([0, 0, 231])  },
               {'color' : 'gray'  , 'tb': np.array([180, 40, 230]) , 'bb': np.array([0, 0, 36])   },
               {'color' : 'red1'  , 'tb': np.array([180, 255, 255]), 'bb': np.array([169, 41, 36])},
               {'color' : 'red2'  , 'tb': np.array([8, 255, 255])  , 'bb': np.array([0, 41, 36])  },
               {'color' : 'green' , 'tb': np.array([80, 255, 255]) , 'bb': np.array([35, 41, 36]) },
               {'color' : 'blue'  , 'tb': np.array([128, 255, 255]), 'bb': np.array([81, 41, 36]) },
               {'color' : 'yellow', 'tb': np.array([34, 255, 255]) , 'bb': np.array([21, 41, 36]) },
               {'color' : 'purple', 'tb': np.array([143, 255, 255]), 'bb': np.array([129, 41, 36])},
               {'color' : 'pink'  , 'tb': np.array([168, 255, 255]), 'bb': np.array([144, 41, 36])},
               {'color' : 'orange', 'tb': np.array([20, 255, 255]) , 'bb': np.array([9, 41, 36])  }]

     def __search_colors(self, arr: np.array, bb: List, tb: List, i: int, key: str):
          index = ( (arr[:,:,0] >= bb[0]) & (arr[:,:,0] <= tb[0]) & 
                    (arr[:,:,1] >= bb[1]) & (arr[:,:,1] <= tb[1]) & 
                    (arr[:,:,2] >= bb[2]) & (arr[:,:,2] <= tb[2]) ) 
          self.colorDicts[i][key] = arr[index]

     def __most_common_in_color(self, index: int, key: str, nColors: int) -> Tuple[np.array, int]:
          unique, counts = np.unique(self.colorDicts[index][key], axis=0, return_counts=True)
          zipVariable = zip(unique, counts)

          return sorted(zipVariable, key=lambda x: x[1], reverse=True)[:nColors]

     def __merge_list(self, large: List, small: List) -> List:
          megrgeList = []
          for i in range(len(large)):    
               try:
                    if (str(small[i]) not in str(megrgeList)):       
                         megrgeList.append(small[i])    
               except IndexError:
                    pass
               if (str(large[i]) not in str(megrgeList)):
                    megrgeList.append(large[i]) 

          return megrgeList

     def __merge_dict(self):
          self.colorDicts.append(
               { 'color': 'red',
               'ar': np.concatenate( (self.colorDicts[3]['ar'], self.colorDicts[4]['ar']) ),
               'arlight': np.concatenate( (self.colorDicts[3]['arlight'], self.colorDicts[4]['arlight']) ),
               'px': self.colorDicts[3]['px'] + self.colorDicts[4]['px']
               }
          )
          
          del self.colorDicts[4]
          del self.colorDicts[3]

     def __sort_dict(self):
          return sorted(self.colorDicts, key=lambda x: x['px'], reverse=True)

     def __get_n_pixels(self) -> int:
          nPixels = 0
          pxrange = self.nOfColors
          if self.nOfColors > len(self.colorDicts):
               pxrange = len(self.colorDicts)
          for i in range(pxrange):
               nPixels += self.colorDicts[i]['px']

          return nPixels

     def __how_much_color(self, index: int) -> int:
          if int( self.nOfColors * self.colorDicts[index]['px/pxn'] ) == 0:
               return 1
          else:
               return int( self.nOfColors * self.colorDicts[index]['px/pxn'] )

     def __algorithm(self, colorN: int, pixelN: int) -> List:
          outList = []  
          for i in range(colorN):
               if len(outList) == colorN:
                    break
               try: # in case of too little pixels
                    self.colorDicts[i]['px/pxn'] = self.colorDicts[i]['px'] / pixelN
               except IndexError:
                    break
               colorList = self.__most_common_in_color(i, 'ar', colorN)
               if self.colorDicts[i]['color'] == ('black' or 'white' or 'gray'):
                    mergeList = colorList
               else:
                    lColorList = self.__most_common_in_color(i, 'arlight', colorN)
                    mergeList = self.__merge_list(colorList, lColorList)
               n = self.__how_much_color(i)
               for j in range(n):
                    if j < len(mergeList):
                         hsv2rgb =  cv2.cvtColor( np.array([[mergeList[j][0]]]), cv2.COLOR_HSV2RGB) 
                         if tuple(hsv2rgb[0][0]) in [value for elem in outList for value in elem.values()]:
                              pass
                         else:
                              outList.append({'rgb': tuple(hsv2rgb[0][0]), 'hex': '#%02x%02x%02x' % tuple(hsv2rgb[0][0])})
                    else:
                         break
                    if len(outList) == colorN:
                         break
 
          if len(outList) < colorN: # in cale of too little pixels in colors
               generateN = int( (colorN - len(outList)) / len(outList) ) + 1
               outListCopy = outList[:]
               index = 0
               for i in range(len(outList)):
                    for j in range(generateN):
                         rgb = list(outList[i]['rgb'])
                         index += 1
                         if rgb[0] + ( 3 * (j+1) ) <= 255:
                              rgb[0] += (3 * (j+1))
                         else:
                              rgb[0] -= 3 * (j+1)
                         outListCopy.insert( i + index, {'rgb': tuple(rgb), 'hex': '#%02x%02x%02x' % tuple(rgb)} )
                         if len(outListCopy) >= colorN:
                              break   
                    if len(outListCopy) >= colorN:
                         break
               return outListCopy
          else:
               return outList

     def palete(self, n=5) -> List:
          try:
               if n < 3 or n > 25 :
                    print('Number of colors must be in range <3:25>')
               else:
                    self.nOfColors = n
               
               for i in range(len(self.colorDicts)):
                    
                    bb = self.colorDicts[i]['bb']
                    tb = self.colorDicts[i]['tb']
                    self.__search_colors(self.imgArray, bb, tb, i, 'ar')
                    
                    if self.colorDicts[i]['color'] != ('black' or 'white' or 'gray'):
                         bb = [self.colorDicts[i]['bb'][0], 125, 125]
                         tb = [self.colorDicts[i]['tb'][0], 255, 255]
                         self.__search_colors(np.array([self.colorDicts[i]['ar']]), bb, tb, i, 'arlight')                         
                    
                    self.colorDicts[i]['px'] = int(len(self.colorDicts[i]['ar']) )
               self.__merge_dict()
               self.colorDicts = self.__sort_dict()
               
               self.colorList = self.__algorithm(self.nOfColors, self.__get_n_pixels())
               for color in self.colorList:
                    print(color)
               return self.colorList
          except AttributeError:
               pass


