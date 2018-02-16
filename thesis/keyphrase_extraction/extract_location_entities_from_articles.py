import pickle
import spotlight
import sys

input_file = open(sys.argv[1],'rb')
output_file = open(sys.argv[2],'wb')

url_list = pickle.load(input_file)

url_location_entities = {}

count = 0
for url in url_list:
    title = url_list[url][0]
    text = url_list[url][1]

    link_text = title + ' ' + text
    loc_filter = {'types':"DBpedia:Place"}
    try:
        entities = spotlight.annotate('http://model.dbpedia-spotlight.org/it/annotate', link_text, confidence=0.45, filters=loc_filter)
        loc_entities = []
        for entity in entities:
            loc_entities.append(entity['surfaceForm'])
        url_location_entities[url] = loc_entities
        print url, loc_entities
    except spotlight.SpotlightException:
        continue
    count+=1
    print "%d of %d"%(count,len(url_list))
    

pickle.dump(url_location_entities, output_file)
input_file.close()
output_file.close()


        
