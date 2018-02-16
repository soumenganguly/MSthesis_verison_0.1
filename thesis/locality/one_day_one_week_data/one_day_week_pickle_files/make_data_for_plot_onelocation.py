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

def make_day2(day,path,keyword_to_popularity1,keyword_to_popularity2,user_set):
	a=0
	b=0
	temp_counter=1
	daily_keywords_to_popularity=defaultdict(int)
	lista=os.listdir(path)
	counter=1
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
		#for key,value in sorted(user_to_newslist.iteritems(), key= lambda (k,v):(k,len(v)), reverse=True):
			user=key

			for couple in value:
				news=couple[0]
				if news not in news_to_title_text_keywords:
					continue
				title=news_to_title_text_keywords[news][1]
				text=news_to_title_text_keywords[news][2]
				if len(text.split())<20:
					continue
				titletext=(title+' '+text)
				keywords_to_popularity=keywords(titletext)
				user_set.add(key)
				if (counter%2):
					for key in keywords_to_popularity:
						keyword_to_popularity1[key]+=keywords_to_popularity[key]
						a+=1

				else:
					for key in keywords_to_popularity:
						keyword_to_popularity2[key]+=keywords_to_popularity[key]
						b+=1
				counter+=1
				#print "temp user set",len(user_set)

day_list=[13,14,15,16,17,18,19]
#day_list=[15]
paths=["/mnt/mplanestore/scavo_contentcuring/PUL/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/UMB/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/PDF/2015/04-Apr/","/mnt/mplanestore/scavo_contentcuring/POLI/2015/"]


community_to_day_to_users={}
threads=[]
user_set=set()
for path in paths:
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

#print "Minimunm number of user in all communities:",min_users
threads=[]
keyword_to_popularity1=defaultdict(int)
keyword_to_popularity2=defaultdict(int)
path="/mnt/mplanestore/scavo_contentcuring/POLI/2015/"
for d in day_list:
	t=threading.Thread(target=make_day2, args=(d,path,keyword_to_popularity1,keyword_to_popularity2,user_set))
	threads.append(t)
	t.start()
for j in threads:
	j.join()

final_key_to_pop_pop={}
for key in keyword_to_popularity1:
	if key not in keyword_to_popularity2:
		final_key_to_pop_pop[key]=[keyword_to_popularity1[key],0]
	else:
		final_key_to_pop_pop[key]=[keyword_to_popularity1[key],keyword_to_popularity2[key]]

for key in keyword_to_popularity2:
	if key not in keyword_to_popularity1:
		final_key_to_pop_pop[key]=[0,keyword_to_popularity2[key]]
print len(keyword_to_popularity1),len(keyword_to_popularity2)
pickle.dump(final_key_to_pop_pop,open("POLI_POLI_oneweek.pkl","w"))
