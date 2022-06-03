import re


'''
deternmine the url inside of text
'''
def find_url(string):
    # 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url
    
print(find_url('''0.58 XZZ:/ 女孩子主动找你，是因为她喜欢你，她不再主动找你，是因为你回的太敷衍，不是她不喜欢你了，是你让她觉得她很多余
%情感 %治愈 %热门 %爱情 %正能量 %励志 %动漫 %文案%小陌治愈驿站  https://v.douyin.com/FEUgdxn/ 复制此链接，打开Dou音搜索，直接观看视频！'''))