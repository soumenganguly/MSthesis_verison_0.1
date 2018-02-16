import pickle
from collections import defaultdict
import os
import threading
from keywordsmod import *



def make_day1(day,path,community_index, community_to_day_to_users):
	daily_user_set=set()
	lista=os.listdir(path)
	for folder in sorted(lista):
		rday=int(str(folder).split("_")[2])
		hour=int(folder.split("_")[3])
		if rday!=day:
			continue
		input_pickle=pickle.load(open(path+"/"+folder+"/user_to_urlNEWS_timestamp_fixed.pkl","r"))
		for k in input_pickle.keys():
			daily_user_set.add(k)
			#daily_user_set.add(input_pickle.keys())
	community_to_day_to_users[community_index][day]=daily_user_set
	#print "community:",community_index,"day:",day,"users:",len(daily_user_set)

def make_day2(day,path,community_index, community_to_day_to_keywords_to_popularity,scanned_users):
	daily_keywords_to_popularity=defaultdict(int)
	lista=os.listdir(path)
	for folder in sorted(lista):
		rday=int(str(folder).split("_")[2])
		hour=int(folder.split("_")[3])
		if rday!=day:
			continue
		if "POLI" not in path:
			news_to_title_text_keywords=pickle.load(open(path+"/"+folder+"/fastweb_url_to_popularity_title_text.pkl","r"))
		else:
			news_to_title_text_keywords=pickle.load(open(path+"/"+folder+"/polito_url_to_popularity_title_text.pkl","r"))
		user_to_newslist=pickle.load(open(path+"/"+folder+"/user_to_urlNEWS_timestamp_fixed.pkl","r"))
		for key,value in sorted(user_to_newslist.iteritems(), key= lambda (k,v):(k,len(v)), reverse=True):
			user=key
			for couple in value:
				news=couple[0]
				if news not in news_to_title_text_keywords:
					continue
				title=news_to_title_text_keywords[news][1]
				text=news_to_title_text_keywords[news][2]
				if len(text.split())<20:
					continue
				if len(scanned_users[community_index])>min_users:
					break
				scanned_users[community_index].add(user)
				titletext=(title+' '+text)
				keywords_to_popularity=keywords(titletext)
				for key in keywords_to_popularity:
					daily_keywords_to_popularity[key]+=keywords_to_popularity[key]
	community_to_day_to_keywords_to_popularity[community_index][day]=daily_keywords_to_popularity

day_list=[13,14,15,16,17,18,19,20]
#day_list=[15]
paths=["/mnt/mplanestore/scavo_contentcuring/PUL/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/UMB/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/PDF/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/POLI/2015/"]

community_to_day_to_users={}
threads=[]
scanned_users=[]
for path in paths:
	u=set()
	scanned_users.append(u)
	community_to_day_to_users[paths.index(path)]={}
	for d in day_list:
		community_to_day_to_users[paths.index(path)][d]=defaultdict(set)
		t=threading.Thread(target=make_day1, args=(d,path,paths.index(path),community_to_day_to_users))
		threads.append(t)
		t.start()
for j in threads:
	j.join()

users=[]
for community in community_to_day_to_users:
	temp_users=set()
	for day in community_to_day_to_users[community]:
		temp_users=temp_users.union(community_to_day_to_users[community][day])
	users.append(len(temp_users))
min_users=min(users)
print "Minimunm number of user in all communities:",min_users


community_to_day_to_keywords_to_popularity={}
for path in paths:
	community_to_day_to_keywords_to_popularity[paths.index(path)]={}
	for d in day_list:
		community_to_day_to_keywords_to_popularity[paths.index(path)][day]={}
		t=threading.Thread(target=make_day2, args=(d,path,paths.index(path),community_to_day_to_keywords_to_popularity,scanned_users))
		threads.append(t)
		t.start()
for j in threads:
	j.join()

print "done, merging the days"
community_to_key_to_popularity={}
for community in community_to_day_to_keywords_to_popularity:
	community_to_key_to_popularity[community]=defaultdict(int)
	#keywords_to_popularity=defaultdict(int)
	for day in community_to_day_to_keywords_to_popularity[community]:
		for key in community_to_day_to_keywords_to_popularity[community][day]:
			#keywords_to_popularity[key]+=community_to_day_to_keywords_to_popularity[community][day][key]
			community_to_key_to_popularity[community][key]+=community_to_day_to_keywords_to_popularity[community][day][key]
	#print keywords_to_popularity
	#community_to_key_to_popularity[community]=keywords_to_popularity
print "done, pickling"
pickle.dump(community_to_key_to_popularity,open("community_to_key_to_popularity_sameuser_"+str(min_users)+"_oneweek.pkl","w"))

print [len(x) for x in scanned_users]