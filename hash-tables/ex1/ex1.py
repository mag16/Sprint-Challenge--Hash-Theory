def get_indices_of_item_weights(weights, limit):
  #initialize dictionary (hash table) to store values
  dict = {}
  #setting hash table (weights = keys. values = i)
  #using enumerate to keep track of iterations w key value pairs
  for i, weight in enumerate(weights):
        dict[weight] = i
  #iterating through table checking weights that meet limit
  for i, weight in enumerate(weights):
        if limit - weight in dict:
              j = dict[limit - weight]
              if i > j:
                  return (i, j)
              else:
                    return (j, i)

  #returning empty tuple for values not meeting limit
  return ()
                    




if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4,6,10,15,16], 21))
