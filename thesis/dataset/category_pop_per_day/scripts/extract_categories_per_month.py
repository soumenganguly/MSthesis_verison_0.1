import sys
import pickle

input_file = open(sys.argv[1],'rb')
output_file = open(sys.argv[2],'wb')

results_per_month = input_file.read()
results = results_per_month.split('\n')

results.pop(-1)

jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
otb = []
nov = []
dec = []

def get_category_pop_per_month(result):
    cat = {}
    tmp = result.split(' ')
    tmp.pop(-1)
    tmp.pop(0)
    tmp.pop(0)
    tmp.pop(0)
    for i in range(len(tmp)):
        if i % 2 == 0:
            cat[tmp[i]] = tmp[i+1]
    return cat

if __name__ == '__main__':
    category_per_month = {}
    for index in range(len(results)):
        try:
            month = results[index].split(' ')[1]
            year = results[index].split(' ')[2]
            if month == '1,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                jan.append(cat_dict)
            elif month == '2,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                feb.append(cat_dict)
            elif month == '3,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                mar.append(cat_dict)
            elif month == '4,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                apr.append(cat_dict)
            elif month == '5,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                may.append(cat_dict)
            elif month == '6,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                jun.append(cat_dict)
            elif month == '7,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                jul.append(cat_dict)
            elif month == '8,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                aug.append(cat_dict)
            elif month == '9,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                sep.append(cat_dict)
            elif month == '10,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                otb.append(cat_dict)
            elif month == '11,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                nov.append(cat_dict)
            elif month == '12,' and year == '2015)':
                cat_dict = get_category_pop_per_month(results[index])
                dec.append(cat_dict)
            else:
                continue
        except IndexError:
            continue
    category_per_month['1'] = jan
    category_per_month['2'] = feb
    category_per_month['3'] = mar
    category_per_month['4'] = apr
    category_per_month['5'] = may
    category_per_month['6'] = jun
    category_per_month['7'] = jul
    category_per_month['8'] = aug
    category_per_month['9'] = sep
    category_per_month['10'] = otb
    category_per_month['11'] = nov
    category_per_month['12'] = dec

    pickle.dump(category_per_month, output_file)

    input_file.close()
    output_file.close()
    
        
        
        
        
        
        
        
        
        
        
