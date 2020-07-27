import json
import os
import sys
import pandas as pd


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


# Start from "1"
for index in range(len(voice)):
    voice[index]["name"] = "o-" + str(index + 1)
    voice[index]["path"] = "o-" + str(index + 1) + ".mp3"
    voice[index]["description"] = {}
    voice[index]["description"]["zh-CN"] = voice[index]["cn"]
    voice[index]["description"]["ja-JP"] = voice[index]["jp"]
    voice[index]["description"]["en-US"] = voice[index]["us"]
    del voice[index]["cn"]
    del voice[index]["jp"]
    del voice[index]["us"]

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