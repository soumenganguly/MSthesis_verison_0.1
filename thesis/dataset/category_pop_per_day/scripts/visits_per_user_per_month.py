from __future__ import division
import pickle
import sys

views_per_month_file = open(sys.argv[1],'rb')
users_per_month_file = open(sys.argv[2],'rb')
output_file = open(sys.argv[3],'wb')

views_per_month = pickle.load(views_per_month_file)
users_per_month = pickle.load(users_per_month_file)

views_per_users = {}

for month in views_per_month:
    total_views = int(sum(views_per_month[month].values()))
    total_users = users_per_month[month]
    views_per_users[month] = total_views/len(total_users)

pickle.dump(views_per_users, output_file)

views_per_month_file.close()
users_per_month_file.close()
output_file.close()
