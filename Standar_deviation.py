import math

# variance for population
def varianceP(data):
      xminus_mean = 0
      mean = sum(data)/len(data)
      for i in data:
            xminus_mean += math.pow((i - mean), 2)
      return xminus_mean/len(data)

#variance for sample
def varianceS(data):
      xminus_mean = 0
      mean = sum(data)/len(data)
      for i in data:
            xminus_mean += math.pow((i - mean), 2)
      return xminus_mean/(len(data)-1)

pop = [1,2,3,8,7]
value_of_pop_var = varianceP(pop)

std_p = math.sqrt(value_of_pop_var)
print(std_p)

value_of_sam_var = varianceS(pop)

std_s = math.sqrt(value_of_sam_var)
print(std_s)