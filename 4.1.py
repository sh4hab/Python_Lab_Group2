# levenshtein Algorithm
import numpy as np



def levenshtein_distance(s, t, row , col , distance):
      if s[row-1] == t[col-1]:
        cost = 0
      else:
        cost = 1
      if(row == 0 or col == 0 ):
        return distance[row][col]
      else :
        distance[row][col] = min(levenshtein_distance(s , t , row - 1 , col , distance) + 1,      # Cost of deletions
                                 levenshtein_distance(s , t , row , col - 1 , distance )+ 1,          # Cost of insertions
                                 levenshtein_distance(s , t , row - 1 , col - 1 , distance) + cost)     # Cost of substitutions
        return distance[row][col]


s = input()
t = input()

rows = len(s)+1
cols = len(t)+1


distance = np.zeros((rows,cols),dtype = int)
for i in range(1, rows):
  for k in range(1,cols):
    distance[i][0] = i
    distance[0][k] = k
print(levenshtein_distance(s , t , len(s) , len(t) , distance) ,"\n" , distance)