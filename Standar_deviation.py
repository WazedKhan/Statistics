import math

def variance(data):
      xminus_mean = 0
      mean = sum(data)/len(data)
      for i in data:
            xminus_mean += math.pow((i - mean), 2)
      return xminus_mean/len(data)

pop = [1,2,3,8,7]
value = variance(pop)

std = math.sqrt(value)
print(std)