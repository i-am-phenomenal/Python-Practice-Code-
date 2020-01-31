number_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def slice_array(first_index, string): 
    global number_characters 
    sliced = string[first_index]
    for iter in range((first_index + 1), len(string)):
      if string[iter] in number_characters: 
          sliced = sliced + string[iter]
          return sliced 
      else: 
          sliced = sliced + string[iter]

    return sliced

def check_if_sum_equals_10(sliced_string):
  first_number = int(sliced_string[0])
  last_number = int(sliced_string[len(sliced_string) - 1])
  return ((first_number + last_number) == 10)

def check_for_question_marks(sliced_string): 
  character_counter = 0
  for character in sliced_string: 
      if character == "?":
        character_counter += 1
      else: 
        pass 

  if character_counter == 3: 
    return True 
  else: 
    return False

def does_contain_single_digit(sliced): 
  global number_characters
  counter = 0
  for character in sliced: 
    if character in number_characters: 
      counter += 1
    else: 
      pass

  if counter == 1: 
    return True 
  else: 
    return False

def match_pattern(sliced):
  counter = 0 
  for character in sliced: 
    if character == "?": 
      counter += 1
    else: 
      pass 
  
  if counter == 3: 
    return True 
  else: 
    return False


def QuestionsMarks(str):
  output = "false"
  for iter in range(0, len(str)):
    if str[iter] in number_characters: 
      sliced_string = slice_array((iter), str)
      if len(sliced_string) < 2: 
        pass
      else: 
       if does_contain_single_digit(sliced_string):
          if match_pattern(sliced_string): 
            output = "true"
          else: 
            return output
       else: 
          if check_if_sum_equals_10(sliced_string): 
            if check_for_question_marks(sliced_string): 
              output = "true"
            else:
              pass
    else: 
      pass 

  # code goes here
  return output

# keep this function call here 
print(QuestionsMarks(input()))
