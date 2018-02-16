import pickle
import sys
import matplotlib.pyplot as plt

a=open(sys.argv[1],'rb') # Absolute category pop per week

p=pickle.load(a)


tech = []
regional = []
science = []
people = []
politics = []
entertainment = []
economics = []
gallery = []
health = []
auto = []
foreign = []
crime = []
sport = []
editors = []
travel = []

if __name__ == '__main__':

    for i in p:
        keys = p[i].keys()
        if 'cronaca' in keys:
            crime.append(p[i]['cronaca'])
        else:
            crime.append(0)
        if 'tecnologia' in keys:
            tech.append(p[i]['tecnologia'])
        else:
            tech.append(0)
        if 'reginone' in keys:
            reginonal.append(p[i]['reginone'])
        else:
            regional.append(0)
        if 'scienza' in keys:
            science.append(p[i]['scienza'])
        else:
            science.append(0)
        if 'persone' in keys:
            people.append(p[i]['persone'])
        else:
            people.append(0)
        if 'politica' in keys:
            politics.append(p[i]['politica'])
        else:
            politics.append(0)
        if 'spettacolo' in keys:
            entertainment.append(p[i]['spettacolo'])
        else:
            entertainment.append(0)
        if 'economia' in keys:
            economics.append(p[i]['economia'])
        else:
            economics.append(0)
        if 'gallerie' in keys:
            gallery.append(p[i]['gallerie'])
        else:
            gallery.append(0)
        if 'salute' in keys:
            health.append(p[i]['salute'])
        else:
            health.append(0)
        if 'motori' in keys:
            auto.append(p[i]['motori'])
        else:
            auto.append(0)
        if 'esteri' in keys:
            foreign.append(p[i]['esteri'])
        else:
            foreign.append(0)
        if 'sport' in keys:
            sport.append(p[i]['sport'])
        else:
            sport.append(0)
        if 'rubriche' in keys:
            editors.append(p[i]['rubriche'])
        else:
            editors.append(0)
        if 'viaggi' in keys:
            travel.append(p[i]['viaggi'])
        else:
            travel.append(0)

    x=range(1,53)

    #xTickMarks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    plt.plot(x,crime, '-', label='Crime')
    plt.plot(x,tech,'--', label='Technology')
    plt.plot(x,regional,'-.', label='Regional')
    plt.plot(x,science,':', label='Science')
    plt.plot(x,people, '.',label='People')
    plt.plot(x,politics, '-o',label='Politics')
    plt.plot(x,entertainment, '-v', label='Entertainment')
    plt.plot(x,economics, '-^', label='Economics')
    plt.plot(x,gallery, '-*',label='Photo gallery')
    plt.plot(x,health, '-+',label='Health')
    plt.plot(x,auto, '-x',label='Automobile')
    plt.plot(x,foreign, '-|', label='Foreign')
    plt.plot(x,sport, '-_',  label='Sport')
    plt.plot(x,editors, '->', label='Editors column')
    plt.plot(x,travel, '-<', label='Travel')

    #plt.xticks(x, xTickMarks)

    plt.grid()

    plt.xticks(range(1,53,4))
    plt.title('ISP-City2-b')
    plt.xlabel('Weeks')
    plt.ylabel('No. of Views')

    #plt.legend([crime,tech,regional,science,people,politics,entertainment[0],economics,gallery,health,auto,foreign,sport,editors,travel], ['Crime','Technology','Regional','Science','People','Politics','Entertainment','Economics','Photo gallery','Health','Automobile','Foreign','Sport','Editors','Travel'])

    plt.legend()

    
    
    plt.show()

    a.close()

        

        
        
