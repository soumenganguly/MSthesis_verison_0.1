import pickle
## 0:milano, 1:torino, 2:bologna, 3:polito

community_to_key_to_popularity_sameuser=pickle.load(open("community_to_key_to_popularity_sameuser_3582_oneweek.pkl","r"))

milan_keys=set(community_to_key_to_popularity_sameuser[0].keys())
turin_keys=set(community_to_key_to_popularity_sameuser[1].keys())

milan_not_turin=milan_keys-turin_keys
turin_not_milan=turin_keys-milan_keys

print "keys milan",len(milan_keys),"turin_ keys",len(turin_keys),"in milan but not in turin",len(milan_not_turin),"in turin not in milan",len(turin_not_milan)

cc=1
for key, value in sorted(community_to_key_to_popularity_sameuser[0].iteritems(), key = lambda (k,v):(v,k), reverse=True):
	if key not in turin_keys:
		print key,value
		cc+=1
	if cc>10:
		break
