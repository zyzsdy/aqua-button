import json
import os
import sys
import pandas as pd


# 路径处理

dirName= os.path.split(os.path.abspath(sys.argv[0]))[0]

# 读入category

rawCategory = pd.read_csv(os.path.join(dirName,'category.csv'))
rawVoice = pd.read_csv(os.path.join(dirName,'voice.csv'))
# dataFrame obj




# 读入Voice
voice = rawVoice.to_dict(orient="index")


# Start from "1"
for index in range(len(voice)):
    voice[index]["name"] = "o-" + str(index + 1)
    voice[index]["path"] = "o-" + str(index + 1) + ".mp3"
    voice[index]["descirption"] = {}
    voice[index]["descirption"]["zh-CN"] = voice[index]["cn"]
    voice[index]["descirption"]["ja-JP"] = voice[index]["jp"]
    voice[index]["descirption"]["en-US"] = voice[index]["us"]
    del voice[index]["cn"]
    del voice[index]["jp"]
    del voice[index]["us"]



print(type(voice))
print(voice)




# append