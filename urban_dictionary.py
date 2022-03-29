# -*- coding: utf-8 -*-
import requests
import sys
import json

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# querystring = {"term":sys.stdin}
querystring = {"term":"wood"}

headers = {
    'x-rapidapi-key': "0e483cd0d4msh6797a8eb38297d2p1d26a2jsn0731d2d0c4d5",
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

res = json.loads(response.text)['list']

# print(res)

def get_definitions(res_list):
    definitions = []
    c = 1
    for i in res_list: 
        # Python 2 version
        d = i['definition'].replace('[', '').replace(']','').encode('utf-8')
        e = i['example'].replace('[', '').replace(']','').encode('utf-8')
        vote = str(str(i['thumbs_up'])+" ▲ | ▼ "+str(i['thumbs_down']).encode('utf-8'))
        date = i['written_on'][:10].encode('utf-8')
        output = str(str(c)+'.\n\n'+d+'\n\n'+'Example:\n'+e+'\n\n\n'+vote+'\n\n'+date).replace('\n','[<>]')
        definitions.append(output)
        c+=1

        # Python 3 version
        # d = i['definition'].replace('[', '').replace(']','')
        # e = i['example'].replace('[', '').replace(']','')
        # vote = str(str(i['thumbs_up'])+" ▲ | ▼ "+str(i['thumbs_down']))
        # date = i['written_on'][:10]
        # output = str(str(c)+'.\n\n'+d+'\n\n'+'Example:\n'+e+'\n\n\n'+vote+'\n\n'+date).replace('\n','[<>]')
        # definitions.append(output)
        # c+=1
    
    return definitions

res_list = get_definitions(res)


for i in res_list:
        print(str(i))
