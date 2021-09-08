import math
a = [2,2,3,3]
b = [0,0,5,5]

def variance(data):
      xminus_mean = 0
      mean = sum(data)/len(data)
      for i in data:
            xminus_mean += math.pow((i - mean), 2)
      print(f'The Variance is : {xminus_mean/(len(data)-1)}')

variance(a)
variance(b)