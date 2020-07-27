import json
import os
import sys
import pandas as pd
# from collections import Counter

# 路径处理

dirName= os.path.split(os.path.abspath(sys.argv[0]))[0]

# 读入category

rawCategory = pd.read_csv(os.path.join(dirName,'category.csv'),encoding='utf-8-sig')
rawVoice = pd.read_csv(os.path.join(dirName,'voice.csv'),encoding='utf-8-sig')
# dataFrame obj



#reform category

category =  rawCategory.to_dict(orient="index")


for index in range(len(category)):
    category[index]["categoryName"] = category[index]["name"]
    category[index]["categoryDescription"] = {}
    category[index]["categoryDescription"]["zh-CN"] = category[index]["cn"]
    category[index]["categoryDescription"]["en-US"] = category[index]["us"]
    category[index]["categoryDescription"]["ja-JP"] = category[index]["jp"]
    del category[index]["name"]
    del category[index]["cn"]
    del category[index]["us"]
    del category[index]["jp"]
    category[index]["voiceList"] = []

print(category)
# 读入Voice
voice = rawVoice.to_dict(orient="index")

voiceDescription_CN = {}

# Start from "1"
for index in range(len(voice)):
    voice[index]["name"] = "o-" + str(index + 1)
    voice[index]["path"] = "o-" + str(index + 1) + ".mp3"
    voice[index]["description"] = {}
    # Conflict Dealing
    if voice[index]["cn"] in voiceDescription_CN.keys():
        voice[index]["us"] = voice[index]["us"] + " " + str(voiceDescription_CN[voice[index]["cn"]])
        voice[index]["jp"] = voice[index]["jp"] + " " + str(voiceDescription_CN[voice[index]["cn"]])
        voiceDescription_CN[voice[index]["cn"]] += 1
        voice[index]["cn"] = voice[index]["cn"] + " " + str(voiceDescription_CN[voice[index]["cn"]]-1)
    else:
        voiceDescription_CN[voice[index]["cn"]] = 2

    voice[index]["description"]["zh-CN"] = voice[index]["cn"]
    voice[index]["description"]["ja-JP"] = voice[index]["jp"]
    voice[index]["description"]["en-US"] = voice[index]["us"]
    del voice[index]["cn"]
    del voice[index]["jp"]
    del voice[index]["us"]

# ADD 1
for key,item in voiceDescription_CN.items():
    if item != 2:
        for vk,vi in voice.items():
            if vi["description"]["zh-CN"] == key:
                vi["description"]["en-US"] = vi["description"]["en-US"] + " 1"
                vi["description"]["ja-JP"] = vi["description"]["ja-JP"] + " 1"
                vi["description"]["zh-CN"] = vi["description"]["zh-CN"] + " 1"


# for k,item in voice.items():
#     item[""]

# print("=conflict=")
# a = dict(Counter(voice))

print(voice)

#merge

for i,cat in category.items():
    for j,vocal in voice.items():
        if vocal["category"] == cat["categoryName"]:
            del vocal["category"]
            cat["voiceList"].append(vocal)


# append

result = {}
result["voices"] = []

for k,item in category.items():
    result["voices"].append(item)


print(result)
with open("autogen-voices.json",'w', encoding='utf-8-sig') as out:
    json.dump(obj=result, fp=out, indent=2,ensure_ascii=False)