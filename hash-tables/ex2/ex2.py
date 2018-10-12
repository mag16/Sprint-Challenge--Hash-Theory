def reconstruct_trip(tickets):
  #start hash table
  dict = {}
  # initialize list 
  trips_end = []
  # iterating thru tickets
  for ticket in tickets:
        dict[ticket[0]] = ticket[1] #setting keyts to start and values to destinations
  
  current_tick = dict[None]
  #looping until destination is none to return list(array)
  while current_tick != None:
        trips_end.append(current_tick)
        if current_tick in dict:
              current_tick = dict[current_tick]
  #return list            
  return trips_end













if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(reconstruct_trip([
      ('PIT', 'ORD'),
      ('XNA', 'CID'),
      ('SFO', 'BHM'),
      ('FLG', 'XNA'),
      (None, 'LAX'),
      ('LAX', 'SFO'),
      ('CID', 'SLC'),
      ('ORD', None),
      ('SLC', 'PIT'),
      ('BHM', 'FLG'),
  ]))
