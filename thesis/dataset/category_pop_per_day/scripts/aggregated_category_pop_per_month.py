import sys
import pickle

input_file = open(sys.argv[1],'rb')
output_file = open(sys.argv[2],'wb')

results = pickle.load(input_file)


def get_category_pop(month):
    category_pop = {}
    for days in results[month]:
        for category in days:
            if category in category_pop:
                category_pop[category] = float(category_pop[category]) + float(days[category])
            else:
                        category_pop[category] = float(days[category])
    category_pop_per_month[int(month)] = category_pop

            
if __name__ == '__main__':
    category_pop_per_month = {}
    for month in results:
        if month == '1':
            get_category_pop('1')
        elif month == '2':
            get_category_pop('2')
        elif month == '3':
            get_category_pop('3')
        elif month == '4':
            get_category_pop('4')
        elif month == '5':
            get_category_pop('5')
        elif month == '6':
            get_category_pop('6')
        elif month == '7':
            get_category_pop('7')
        elif month == '8':
            get_category_pop('8')
        elif month == '9':
            get_category_pop('9')
        elif month == '10':
            get_category_pop('10')
        elif month == '11':
            get_category_pop('11')
        elif month == '12':
            get_category_pop('12')
        else:
            continue
        
            
    pickle.dump(category_pop_per_month, output_file)
    input_file.close()
    output_file.close()
