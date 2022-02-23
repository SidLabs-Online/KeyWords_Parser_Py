# from collections import Counter
# import re

# f = open("somefile.txt", "r")     
# data = f.read()                   

# data = data.lower()

# data = re.sub("[^\w ]", "", data)

# def Convert(tup, di):
#     for a, b in tup:
#         di.setdefault(a, []).append(b)
#     return di
      
# output_data = {}


# words = data.split(" ")
# Counter(words)

# filtered = Counter(words).most_common(30)
# # print(filtered)

# Convert(filtered, output_data)
# # print(output_data)


# #driver
# for words, count in output_data.items():
#   print (words, ":", count)


# testing web parser
import urlParser

urlParser.theParser()