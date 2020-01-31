alphabet_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


def format_string(string):
  vowels = ["a", "e", "i", "o", "u"]
  formatted = ""
  for character in string: 
    if character in vowels: 
      formatted += character.upper()
    else: 
      formatted += character

  return formatted 

def get_key_from_value(code):
  global alphabet_dict
  for key, value in alphabet_dict.items():
    if value == code: 
      return key
    else: 
      pass 
  
  return ""

def LetterChanges(str):
  global alphabet_dict
  replaced = ""
  for character in str: 
    if character in alphabet_dict:
      character_code = alphabet_dict[character]      
      next_character = get_key_from_value(character_code + 1)
      # print("CHARACTER CODE -> ", character_code )
      replaced += next_character
    else: 
      replaced += character 
      # replaced = replaced.replace(" ", "")
  # code goes here
  formatted = ""
  formatted = format_string(replaced)
  return formatted

# keep this function call here 
print(LetterChanges(input()))
