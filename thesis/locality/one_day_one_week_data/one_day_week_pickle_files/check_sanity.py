import pickle

community_to_key_to_popularity=pickle.load(open("community_to_key_to_popularity_sameuser_3582_oneweek.pkl","r"))

for community in community_to_key_to_popularity:
	print community
	for key,value in sorted(community_to_key_to_popularity[community].iteritems(), key = lambda (k,v):(v,k), reverse=True)[:20]:
		print key,value