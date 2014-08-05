set = {3, 4, 5}
temp_set = []
master_set = []

def permu(set, temp_set):
  if len(set) == 0:
    master_set.append(temp_set)
    return
  for index in set:
    print("Set:", set)
    print("Temp_Set:", temp_set)
    print("Index:", index)
    print("Master_Set:", master_set)
    if index not in temp_set:
      new_set = set.difference({index})
      new_temp_set = temp_set
      new_temp_set.append(index)
      permu(new_set, new_temp_set)

permu(set, temp_set)
print(master_set)
