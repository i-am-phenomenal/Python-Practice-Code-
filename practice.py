# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import requests
#
# url = "https://projects.propublica.org/nonprofits/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# table = soup.findAll("table", {"id": "highest-bidders"})
# tr = soup.findAll("tr")
# div = soup.findAll("div", {"class": "highest-bidders" })
# for div in div:
#      table = div.find("table")
#
# for tr in table:
#      tr = tr.find("tr")
#      if not (tr == -1):
#          th = tr.findAll("th")
#      print("666666666", th)
#
#
# print(table)
# # print(span)
# dataList = []
# file = pd.read_excel("wildlife.xlsx")
# for data in file.index:
#     dataList.append(data)
#
# print(len(dataList))


# class DummyClass:
#     def __init__(self, first_number, second_number):
#         self.first_number = first_number
#         self.second_number = second_number
#         # print(self.first_number)
#         # print(self.second_number)
#         def add(self):
#             print(self.first_number + self.second_number)
#
#         def subtract(self):
#             if self.first_number >= self.second_number:
#                 return self.first_number - self.second_number
#             else:
#                 return self.second_number - self.first_number
#
#
# # first_number = int(input("Enter the first number"))
# # second_number = int(input("Enter the second number"))
# class_object = DummyClass(2, 3)
# operator = input("Enter the operator")
# if operator == "+":
#     print(class_object.add())
#     # print(result)
# else:
#     print(class_object.subtract())
#     # print(result)


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-10, 10, 100)
# y = np.sin(x)
# printplt.plot(x, y, marker="x")

# import sys
#
# print(sys.version)
# from scipy.stats import wasserstein_distance
# from PIL import Image
# import skimage
# import numpy as np
# import os
# from pyemd import emd, emd_samples
#
# # print(os.path.join(skimage.data_dir, "image.png"))
# print()
# img1 = skimage.io.imread(os.path.join(os.getcwd(), "image.png"))
# img2 = skimage.io.imread(os.path.join(os.getcwd(), "imahe2.png"))
#
# images = [img.ravel() for img in [img1, img2]]
#
# emd_samples(images[0], images[1])
#
# print(wasserstein_distance(images[0], images[1]))

#
# def get_histo(img):
#     h, w = img.size
#     hist = [0.0] * 256
#     print(img)
#     # for i in range(h):
#     #     for j in range(w):
#     #         print([i, j])
#     #         hist[img[i, j]] += 1
#     # return np.array(hist) / (h * w)
#
#
# a = Image.open("image.png")
# print(a.size)
# b = Image.open("imahe2.png")
# a_hist = get_histo(a)
# b_hist = get_histo(b)
#
# distance = wasserstein_distance(a_hist, b_hist)
# print(distance)
#
# import re
#
#
# def replace_consonants(char):
#     c1 = ["b", "f", "p", "v"]
#     c2 = ["c", "g", "j", "k", "q", "s", "x", "z"]
#     c3 = ["d", "t"]
#     c4 = ["m", "n"]
#     # for char in word:
#     if char in c1:
#         return "1"
#     elif char in c2:
#         return "2"
#     elif char in c3:
#         return "3"
#     elif char == "l":
#         return "4"
#     elif char in c4:
#         return "5"
#     elif char == "r":
#         return "6"
#     else:
#         return "-1"
#
#
# def drop_vowels(word):
#     global vowel
#     new = word
#     for char in word:
#         if char in vowel:
#             new = word.replace(char, "")
#         else:
#             pass
#     return new
#
#
# def retain_one_duplicate(word):
#     list1 = list(word)
#     last_word = list1[len(list1) - 1]
#     last_iter = ""
#     string = ""
#     for ele in list1:
#         print("ele -> ", ele)
#         index = list1.index(ele)
#         if list1[(index + 1)] == ele:
#             del list1[index + 1]
#             print("TRUE", list1)
#         else:
#             pass
#
#     for ele in list1:
#         string += ele
#
#     return string
#
#
# vowel = ["a", "e", "i", "o", "u", "h", "y", "w"]
# word1 = "ashcraft"
# word2 = "ashcroft"
# consonants_replaced1 = ""
# consonants_replaced2 = ""
#
# # Step1
# first_letter1 = word1[0]
# first_letter2 = word2[0]
# vowels_removed1 = drop_vowels(word1)
# vowels_removed2 = drop_vowels(word2)
#
# for char in vowels_removed1:
#     consonants_replaced1 = consonants_replaced1 + replace_consonants(char)
# consonants_replaced1 = first_letter1 + consonants_replaced1
# print(consonants_replaced1, "consonants_replaced1")
#
#
# for char in vowels_removed2:
#     consonants_replaced2 = consonants_replaced2 + replace_consonants(char)
# consonants_replaced2 = first_letter2 + consonants_replaced2
# print(consonants_replaced2, "consonants_replaced2")
#
# # Step 3
# match1 = re.search(r"(.)\1", word1)
# if match1 is None:
#     pass
# else:
#     retain_one_duplicate(word1)
#
# match2 = re.search(r"(.)\1", word2)
# if match2 is None:
#     pass
# else:
#     retain_one_duplicate(word2)


# import matplotlib.pyplot as plt
# import librosa
#
#
# audio_path = "C:/waveformrs/target/release/file_example_WAV_2MG.wav"
#
# x, sample_rate = librosa.load(audio_path, sr=44100)
#
# print(type(x), type(sample_rate))


# print(os.getcwd())
# print("+++++++++++++=")
# wav_file = wave.open((os.getcwd() + "/audio_file.wav"), "r")
# print("*************")
# signal = wav_file.readframes(-1)
# signal = np.frombuffer(signal, "Int16")
#
# if wav_file.getnchannels() == 2:
#     print("Just Mono Channels")
#     sys.exit(0)
#
# plt.figure(1)
# plt.title("Signal Wave...")
# plt.plot(signal)
# plt.show()


# K-MEANS CLUSTERING
#
# import json
# import random
#
#
# def get_least_distances():
#     distances = []
#     for ele in min_distances:
#         distances.append(ele["distance"])
#     return distances
#
#
# def calculate_distance(min_value):
#     global max_values
#     for max_value in max_values:
#         distance = max_value - min_value
#         min_distances.append(
#             {"max_value": max_value, "min_value": min_value, "distance": distance}
#         )
#
#
# counter = 0
# clusters = []
# rms_values = []
# min_values = []
# max_values = []
# data_clusters = []
# min_distances = []  # {"min_value": "", "rms_value": "" "distance": 0}
# file = open("C:/practice Programs/rhyme-scheme/dataset/numbers_wav/1/95.json", "r")
# json_file = json.load(file)
# audio_samples = json_file["samples"]
#
# for index in range(0, len(audio_samples)):
#     current_dict = audio_samples[index]
#     if counter < len(audio_samples):
#         rms_values.append(current_dict["rms"])
#         min_values.append(current_dict["min"])
#         max_values.append(current_dict["max"])
#         counter += 1
#     else:
#         pass
#
# for iter in range(0, 5):
#     random_rms = random.choice(rms_values)
#     clusters.append({"rms": random_rms, "data_point": ""})
#     # clusters.append({'rms': random_rms, 'min_distance': {}})
#
# for value in min_values:
#     calculate_distance(value)
#     break
#
#
# def assign_cluster(min_distance):
#     global data_clusters
#     difference = 0
#     diff_array = []
#     # print(clusters[0])
#     # print(min_distance["distance"])
#     smallest_difference = clusters[0]["rms"] - min_distance["distance"]
#     print("CLUSTERS", clusters)
#     for cluster in clusters:
#         difference = cluster["rms"] - min_distance["distance"]
#         if difference <= smallest_difference:
#             data_clusters.append(
#                 {"distance": min_distance["distance"], "rms_value": difference}
#             )
#             smallest_difference = difference
#
#
# for min_distance in min_distances:
#     assign_cluster(min_distance)
#
#
# print(data_clusters)
#
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
#
# url = "https://stackoverflow.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# for element in soup.find_all("a", href=True):
#     print(element["href"])

# print(len(divContent))

# print(len(soup.findAll("div")))
# print(innerContent)
# for element in innerContent:
#     print(element)

# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# import re, datetime
# from dateutil.parser import parse

# # import lxml

# response = requests.get("https://www.data.gov/metrics")
# soup = BeautifulSoup(response.text, "html.parser")
# datasets = soup.find_all(
#     "td", {"class": "datasets_published_per_month_table_row_fields"}
# )
# data = []
# for element in datasets:
#     data.append(element.string)


# def checkIfNone(element):
#     return element != None and element != "//"


# def check_if_date(element):
#     fuzzy = False
#     try:
#         parse(element, fuzzy=fuzzy)
#         return True
#     except ValueError:
#         return False


# def keep_dates(element):
#     try:
#         int(element)
#         return True
#     except ValueError:
#         return False


# dates = []
# data = filter(checkIfNone, data)
# data = list(data)
# data = data[15:]

# for ele in data:
#     is_date = check_if_date(ele.string)
#     if is_date:
#         dates.append(ele.string)
#     else:
#         pass

# updated_dates = filter(keep_dates, dates)
# print(dates)
# match = re.search("\d{2}-\d{2}-\d{4}", ele)
# dates.append(match.group())

# for ele in datasets:
#     print(ele["href"])
# print(datasets[0]["href"])


# l = ["death", "ok", "dog", "darth","vader"]
# a = []
# for i in l:
#     if 'd' not in i:
#         l.remove(i)
#     # else:
#     #     a.append(i)
# print(2/0)


# from flask import Flask
# app = Flask(__name__)
# @app.route('/dummy_router')
# def dummy_function():
#     return "Dummy function is here "


# if __name__ == '__main__':
#     app.run()

# app.add_url_rule('/', 'Dummy Message', dummy_function)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix, accuracy_score
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# data_frame = pd.read_csv("diabetes.csv")
# print(data_frame)
# x_value = data_frame.drop('Glucose', axis=1)
# y_value = data_frame['Glucose']
# x_train, x_test, y_train, y_test = train_test_split(
#     x_value, y_value, test_size=0.33, random_state=1)
# logmodel = LogisticRegression()
# logmodel.fit(x_train, y_train)
# predictions = logmodel.predict(x_test)

# print(predictions)
# data_classification_report = classification_report(y_test, predictions)
# data_confusion_matrix = confusion_matrix(y_test, predictions)
# data_accuracy_score = accuracy_score(y_test, predictions)

# print(" CLASSIFICATION REPORT ", data_classification_report)
# print(" CONFUSION MATRIX ", data_confusion_matrix)
# print(" ACCURACY SCORE ", data_accuracy_score)
