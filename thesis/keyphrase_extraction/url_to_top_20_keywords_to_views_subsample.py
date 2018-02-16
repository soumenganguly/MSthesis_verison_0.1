import pickle
import sys

url_to_keywords_file = open(sys.argv[1],'rb') # URL to keywords
url_to_views_file = open(sys.argv[2],'rb') # URL to view count (sub sample version)
output = open(sys.argv[3],'wb')

url_to_keywords = pickle.load(url_to_keywords_file)
url_to_views = pickle.load(url_to_views_file)


url_keyword_view = {}

for url in url_to_views:
    if url in url_to_keywords and url not in url_keyword_view:
        keyword_view = []
        keyword_view.append(url_to_keywords[url])
        keyword_view.append(url_to_views[url])
        url_keyword_view[url] = keyword_view
    else:
        pass


pickle.dump(url_keyword_view, output)
output.close()
url_to_keywords_file.close()
url_to_views_file.close()

        
