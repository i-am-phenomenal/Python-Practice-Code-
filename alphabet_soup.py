def AlphabetSoup(str):
  to_list = [] 
  to_string = ""
  for character in str: 
    to_list.append(character)

  to_list.sort()
  for character in to_list:
    to_string = to_string + character

  # code goes here
  return to_string

# keep this function call here 
print(AlphabetSoup(input()))
