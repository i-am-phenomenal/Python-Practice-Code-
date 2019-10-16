# import fuzzy
# import re
# import collections
# soundex = fuzzy.Soundex(4)
# lyrics = [
#          "I can't tell you what it really is",
#          "I can only tell you what it feels like",
#          "And right now, it's a steel knife in my windpipe",
#          "I can't breathe but I still fight while I can fight",
#          "As long as the wrong feels right it's like I'm in flight",
#          "High off her love, drunk from her hate",
#          "It's like I'm huffing paint and I love her the more I suffer, I suffocate"
#          ]
#
# def get_words(line):
#     list_of_words = line.split(" ")
#     list_of_soundex_codes = []
#     dictionary = {}
#     reverse_dict = {}
#     for word in list_of_words:
#         list_of_soundex_codes.append(soundex(word))
#
#     dictionary = dict(zip(list_of_words, list_of_soundex_codes))
#     reverse_dict = {}
#     for key, value in dictionary.items():
#         try:reverse_dict[value].append(key)
#         except:reverse_dict[value] = [key]
#
#     print(reverse_dict)
#     # dictionary = collections.defaultdict(set)
#     # print(dictionary)
#     # for soundex_code in list_of_soundex_codes:
#     #     if (re.search(r"(.)\1", soundex_code)) is None:
#     #          pass
#     #     else
#
# for line in lyrics:
#      get_words(line)
#
# print(soundex("ashcraft"))
# print(soundex("ashcroft"))


dummy = (str(input("Sentence:"))).split(" ")
max = 0
for iter in dummy:
    if len(iter) > max:
        max = len(iter)
    else:
        max

print(max)
