import pickle
import sys

input_file = open(sys.argv[1],"rb")

output_file = open("url_to_agent_timestamp.pkl","wb")

pickle_file = pickle.load(input_file)

url_to_agent_timestamp = {}

for key in pickle_file:
        for url in pickle_file[key]:
                if url[0] not in url_to_agent_timestamp:
                        url_to_agent_timestamp[url[0]] = []
                        tmp = (key[0], key[1], url[1])
                        url_to_agent_timestamp[url[0]].append(tmp)
                else:
                        tmp = (key[0], key[1], url[1])
                        url_to_agent_timestamp[url[0]].append(tmp)

pickle.dump(url_to_agent_timestamp, output_file)
input_file.close()
output_file.close()




































