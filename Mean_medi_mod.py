#All the theoritical explaination 
#https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php#:~:text=Add%20up%20all%20of%20the,This%20is%20the%20median.

n = [181, 187, 196, 198, 203, 207, 211, 215] 
points_per_game = [3, 15, 23, 42, 30, 10, 10, 12]
sponsorship = ['nike', 'adidas', 'nike', 'jordan',
               'jordan', 'rebook', 'under-armour', 'adidas']
#n = [1, 1, 2, 6, 6, 9]
# mean is the avarage

n = sorted(n)

mean = sum([1,2,3,4])/len([1,2,3,4])
print(f'Mean: {mean}')

# mediun 
med = len(n)/2
if med %2 != 0:
      print(f'Medium: {n[int(med)]}')
else:
      med = int(len(n)/2)
      med = (n[med-1] + n[med])/2
      print(f'Medium: {med}')

#Mode

freq = {}
for i in points_per_game:
      freq[i] = freq.get(i, 0) + 1
      most_freq = max(freq.values())
      mode = [key for key, value in freq.items() if value == most_freq]

print(max(mode))