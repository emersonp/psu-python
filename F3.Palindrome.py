def palindrome(sequence):
  return sequence == list(reversed(sequence))

print(True == palindrome([1,2,3,3,2,1]))
print(False == palindrome(['a','b','b','b']))
print(False == palindrome([1,'2',2,'1']))
