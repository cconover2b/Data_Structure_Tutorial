'''
Remove the items from the bag and then sort the fruits into the fruits_bag and the veggies into the veggies_bag.
'''

def sorter(list):
  bag = list
  fruit_bag = []
  veggies_bag = []
  
  fruit_bag.append(bag.pop())
  # print(fruit_bag)
  veggies_bag.append(bag.pop())
  # print(veggies_bag)
  veggies_bag.append(bag.pop())
  # print(veggies_bag)
  fruit_bag.append(bag.pop())
  # print(fruit_bag)
  fruit_bag.append(bag.pop())
  # print(fruit_bag)
  veggies_bag.append(bag.pop())
  # print(veggies_bag)
  fruit_bag.append(bag.pop())
  # print(fruit_bag)
    
  print(f'Bag: {bag}')
  print(f'Fruit Bag: {fruit_bag}')
  print(f'Veggies Bag: {veggies_bag}')

sorter(['bananas', 'cucumbers', 'grapes', 'apples', 'carrots', 'celery', 'strawberies'])

'''
Expected results:
Bag: []
Fruit Bag: ['strawberies', 'apples', 'grapes', 'bananas']
Veggies Bag: ['celery', 'carrots', 'cucumbers']
'''