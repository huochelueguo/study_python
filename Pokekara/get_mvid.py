import requests
import json
import jsonpath

"""
获取歌曲榜单MV_ID
"""

song_list = [2128317582,
125102489,
1536380621,
713388093,
868469495,
1202032132,
25736,
2044109622,
254566449,
1939678742

]


def get_rank(song_id):
    url = 'https://api.pokekara.com/x/ranking/music_video?cursor=0&tab=popularity&v=2.9.6&group=song&refer=default&group_id='
    url2 = url + str(song_id)
    response = requests.get(url2)
    mv_id = jsonpath.jsonpath(response.json(), '$.data.ranking[*].mv_id')[0:10]
    return mv_id

l = []
for i in song_list:
    id = get_rank(i)
    l.append(id)
    l.append('\n')
print(l)