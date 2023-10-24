

#numbers = ['1','2','3','4','5','6','7','8','9']
#letters = ['K','J','Q']

#hand_1 = ['J', 'A', 'A', '2']
#hand_2 = ['9', '6', 'K', 'A', '5', 'J']

hand_1 = ['6', '2', '8']
hand_2 = ['3', '4', 'Q', 'K', '6', '3']

def blackjack_hand_greater_than(hand_1, hand_2):
  import random
  
  numbers = ['1','2','3','4','5','6','7','8','9','10']
  letters = ['K','J','Q']
  aux = [1,11]
  sum1 = 0
  sum2 = 0
    
  print('\nhand_1 =',hand_1)
  print('hand_2 =',hand_2)
    
  count1 = 0
  for elem1 in hand_1:
    count1 += 1
    for el1 in elem1:
      if el1 in numbers:
        sum1 += int(el1)
      if el1 == 'A':
        k1 = random.choice(aux)
        sum1 += k1
      if el1 in letters:
        sum1 += 10

  count2 = 0
  for elem2 in hand_2:
    count2 += 1
    for el2 in elem2:
      if el2 in numbers:
        sum2 += int(el2)
      if el2 == 'A':
        k2 = random.choice(aux)
        sum2 += k2
      if el2 in letters:
        sum2 += 10
            
            
  print('\nsum1 =', sum1)
  print('sum2 =', sum2)
    
  if sum1 > 21: 
    return print('\nFalse')
  else:
    if sum1 < sum2 or sum2 > 21:
      return print('\nFalse')
    else:
      return print('\nTrue')
            
blackjack_hand_greater_than(hand_1,hand_2)

# Para que a mão_1 vença a mão_2, o seguinte deve ser verdadeiro:
#O total de hand_1 não deve exceder 21
#O total de hand_1 deve exceder o total de hand_2 OU o total de hand_2 deve exceder 21