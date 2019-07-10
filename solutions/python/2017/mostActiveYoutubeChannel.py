# STILL ERROR on HIDDEN ANSWERS
"""
You've been YouTube surfing lately a lot, and after a while noticed that most of the videos you've seen so far were posted by the same channel.
You want to find the most active channel, i.e. the channel that posted the majority of the videos you've seen.

Given videoIDs list representing the unique video identifiers, return the title of the most active channel.
If there is a tie, return the lexicographically smallest title.

Useful APIs = https://developers.google.com/youtube/v3/docs/

In this task you should use the YouTube Data API.

Example

For videoIDs = ["Rd9ZKwNCYtM", "YQJKgtAktLQ", "VL0eeXONpOs", "YaK8J0cxL8c", "JcAWr4gZgeI"],

the output should be

mostActiveYoutubeChannel(videoIDs) = "CodeFights".

The 1st, 3rd and 4th videos are from the "CodeFights" channel, and all the other videos are from "Marvel Entertainment".
So, the title of the most active channel is "CodeFights".
"""

# VERSION 1 - failed
# import urllib2, json
# from collections import Counter
#
# def mostActiveYoutubeChannel(videoIDs):
#     url = "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=%s&format=json"
#    author_names = []
#    for vid in videoIDs:
#        try:
#            resp = urllib2.urlopen(url % vid)
#            data = json.loads(resp.read().decode())
#            author_names.append(data.get('author_name'))
#        except:
#            pass
#
#    c = Counter(author_names)
#    return c.most_common(1)[0][0]
#
#
# VERSION 2 - failed
# import urllib2 as U, collections as C #, json as J
#
# def mostActiveYoutubeChannel(ids):
#    y = 'http://www.youtube.com'
#    u = y+'/oembed?url='+y+'/watch?v=%s'
#
#    n = []
#    for v in ids:
#        try:
#            d = json.loads(U.urlopen(u % v).read().decode())
#            n.append(d.get('author_name'))
#        except:
#            pass
#
#    c = C.Counter(n)
#    return c.most_common(1)[0][0]
#
#
# VERSION 3 - failed
# i = eval(dir()[0])[0]
#
# import urllib2 as U, collections as C
#
# y = 'http://www.youtube.com'
# u = y+'/oembed?url='+y+'/watch?v=%s'
# n = []
#
# for v in i:
#    try:
#        d = json.loads(U.urlopen(u % v).read())
#        n.append(d.get('author_name'))
#    except: pass
#
# c = C.Counter(n)
# return c.most_common(1)[0][0]

# VERSION 4 - correct
i = eval(dir()[0])[0]
u = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=%s&key=AIzaSyB7gWVfK3eCamK1Lnk_oxGciKwEe-DGscA'
n = []

import urllib2 as U, collections as C

for v in i:
    try:
        d = json.loads(U.urlopen(u % v).read())
        n.append(d['items'][0]['snippet']['channelTitle'])
    except: pass

c = C.Counter(n)
return c.most_common(1)[0][0]
