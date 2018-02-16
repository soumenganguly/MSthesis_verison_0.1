import pickle
import itertools
import sys
import matplotlib.pyplot as plt

a=open(sys.argv[1],'rb') # Absolute category per month
#b = open(sys.argv[2],'rb') #Views_per_user file

p=pickle.load(a)
#q = pickle.load(b)

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

    x=[1,2,3,4,5,6,7,8,9,10,11,12]

    xTickMarks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #ax1.set_ylim([0,50000])
    ax1.set_ylim([0,30])

    marker = itertools.cycle((',', '+', '.', 'o', '*'))
    
    ax1.plot(x,crime, label='Crime', marker=marker.next())
    #ax1.plot(x,tech,'--', label='Technology')
    #ax1.plot(x,regional,'-.', label='Regional')
    ax1.plot(x,science, label='Science',marker=marker.next())
    #ax1.plot(x,people, label='People',marker=marker.next())
    ax1.plot(x,politics, label='Politics',marker=marker.next())
    ax1.plot(x,entertainment,  label='Entertainment',marker=marker.next())
    ax1.plot(x,economics,  label='Economics',marker=marker.next())
    #ax1.plot(x,gallery, '-*',label='Photo gallery')
    #ax1.plot(x,health, '-+',label='Health')
    #ax1.plot(x,auto, '-x',label='Automobile')
    ax1.plot(x,foreign,  label='International',marker=marker.next())
    ax1.plot(x,sport, label='Sport',marker=marker.next())
    ax1.plot(x,editors,  label='Editors column',marker=marker.next())
    ax1.plot(x,travel, '-<', label='Travel')

    plt.xticks(x, xTickMarks)

    plt.grid()

    #plt.title('ISP-City2-b')
    ax1.set_xlabel('Month',fontsize=22)
    ax1.set_ylabel('% of Views',fontsize=22)


    '''
    Not required for this analysis
    y2 = q.values()

    ax2 = ax1.twinx()
    ax2.set_ylim([0,7])
    ax2.plot(x, y2, 'red')
    ax2.set_ylabel('Views/users', color='red')
    for tl in ax2.get_yticklabels():
        tl.set_color('red')
    '''

    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),ncol=3, fancybox=True, shadow=True)
    plt.tight_layout()
    
    plt.show()

    a.close()

        

        
        
