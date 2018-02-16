import pickle
## 0:milano, 1:torino, 2:bologna, 3:polito

comm1=1
comm2=3


community_to_key_to_popularity_sameuser=pickle.load(open("community_to_key_to_popularity_sameuser_986_oneday.pkl","r"))

final_key_to_pop_pop={}
for key in community_to_key_to_popularity_sameuser[comm1]:
	if key not in community_to_key_to_popularity_sameuser[comm2]:
		final_key_to_pop_pop[key]=[community_to_key_to_popularity_sameuser[comm1][key],0]
	else:
		final_key_to_pop_pop[key]=[community_to_key_to_popularity_sameuser[comm1][key],community_to_key_to_popularity_sameuser[comm2][key]]

for key in community_to_key_to_popularity_sameuser[comm2]:
	if key not in community_to_key_to_popularity_sameuser[comm1]:
		final_key_to_pop_pop[key]=[0,community_to_key_to_popularity_sameuser[comm2][key]]

pickle.dump(final_key_to_pop_pop,open("UMB_POLI_oneday.pkl","w"))

