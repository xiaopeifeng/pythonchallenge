import re

data = "" # 此处为http://www.pythonchallenge.com/pc/def/ocr.html中find rare characters in the mess below下面的片段
          # so shit,太长了，好恶心啊 

print "".join(re.findall("[A-Za-z]", data))