import pickle
import sys

a = open('pdf15_url_to_views.pkl','rb')
b = open('pdf16_url_to_views.pkl','rb')
c = open('poli15_url_to_views.pkl','rb')
d = open('pul15_url_to_views.pkl','rb')
e = open('pul16_url_to_views.pkl','rb')
f = open('umb15_url_to_views.pkl','rb')
g = open('umb16_url_to_views.pkl','rb')
h = open('poli16_url_to_views.pkl','rb')

m = pickle.load(a)
n = pickle.load(b)
o = pickle.load(c)
p = pickle.load(d)
q = pickle.load(e)
r = pickle.load(f)
s = pickle.load(g)
t = pickle.load(h)

#input_file = open(sys.argv[1],'rb')
output_file = open(sys.argv[1],'wb')

#ref = pickle.load(input_file)

m.update(n)
m.update(o)
m.update(p)
m.update(q)
m.update(r)
m.update(s)
m.update(t)

#all_urls_scraped = {}
'''
for i in ref:
    if i in m:
        all_urls_scraped[i] = m[i]
    else:
        pass

'''

pickle.dump(m, output_file)

a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
g.close()
h.close()
#input_file.close()
output_file.close()
        
