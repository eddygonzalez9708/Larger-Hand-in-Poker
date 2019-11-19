def largerHand(h1, h2):
  ptr = 0

  high = 0
  cache_h1 = {}
  cache_h2 = {}

  duplicate = False
  larger_hand = None

  while ptr < 5:
    h1_num = h1[ptr]
    h2_num = h2[ptr]

    if duplicate:
      if h1_num in cache_h1:
        if h1_num > high:
          high = h1_num
          larger_hand = h1

      if h2_num in cache_h2:
        if h2_num > high:
          high = h2_num
          larger_hand = h2
    else:
      if h1_num in cache_h1 and h2_num not in cache_h2:
        high = h1_num
        larger_hand = h1
        duplicate = True
      elif h2_num in cache_h2 and h1_num not in cache_h1:
        high = h2_num
        larger_hand = h2
        duplicate = True
      elif h1_num in cache_h1 and h2_num in cache_h2:
        if h1_num > h2_num:
          high = h1_num
          larger_hand = h1
        elif h2_num < h1_num:
          high = h2_num
          larger_hand = h2
        duplicate = True
      elif h1_num > h2_num and h1_num > high:
        high = h1_num
        larger_hand = h1
      elif h2_num > h1_num and h2_num > high:
        high = h2_num
        larger_hand = h2
      
    cache_h1[h1_num] = True
    cache_h2[h2_num] = True
    
    ptr += 1
  
  return larger_hand if high else [h1, h1]

h1 = [2, 14, 7, 10, 11]
h2 = [3, 11, 11, 10, 9]
print(largerHand(h1, h2))

h1 = [14, 3, 5, 7, 10]
h2 = [14, 13, 3, 2, 9]
print(largerHand(h1, h2))

h2 = [2, 2, 3, 4, 10]
h1 = [1, 1, 1, 5, 14]
print(largerHand(h1, h2))