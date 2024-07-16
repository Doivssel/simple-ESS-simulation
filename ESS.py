import numpy as np
import matplotlib.pyplot as plt

max_food=100
food_init=5
loss_food=0.4
value_food=1
rep_food=10
fight_penalty=0.8

pop_size=100
prob_egoist=0.5


num_day=1000

init_pop=[[food_init,(np.random.uniform(0,1)<prob_egoist)*1] for _ in range(pop_size)]

def generate_food(max_food):
    qty_food=np.random.randint(1,max_food)
    food_day=[[[],[]] for _ in range(qty_food)]
    return(qty_food,food_day)

def interested_in(qty_food,food_day):
    for j in range(len(init_pop)):
        ind_loc=np.random.randint(0,qty_food)
        food_day[ind_loc][0].append(j)
        food_day[ind_loc][1].append(init_pop[j][1])
    return(food_day)

def current_food_update(init_pop,food_day,value_food):
    for food in food_day:
        ind_comp=len(food[0])
        if(ind_comp==1):                                                #only one ind  on a food, it get all the food
            init_pop[food[0][0]][0]+=value_food
        elif(ind_comp>1):                                               #many ind on a food, must attribute it following certain rules
            nb_egoist=np.sum((np.array(food[1])==1)*1)
            if(nb_egoist==0):                                           #no egoist, then food shared equally
                for ind in food[0]:
                    init_pop[ind][0]+=np.round(value_food/ind_comp,2)
            elif(nb_egoist==1):                                         #one egoist, the egoist get all the food
                egoist=np.argwhere(np.array(food[1])).flatten()
                ind=food[0][egoist[0]]
                init_pop[ind][0]+=value_food
            elif(nb_egoist>1):                                          #multiple egoists, divide unequally among them and get a penalty for the fight
                egoist=np.argwhere(np.array(food[1])).flatten()
                part=generate_part(nb_egoist)
                for j in range(nb_egoist):
                    ind=food[0][egoist[j]]
                    init_pop[ind][0]+=np.round(value_food*part[j]-fight_penalty,2)
    for i in range(len(init_pop)):                                      #all get a penalty at the end of the day
        init_pop[i][0]-=loss_food
    return(init_pop)

def death_birth(init_pop):
    temp_pop=[]
    for i in range(len(init_pop)):
        if(init_pop[i][0]>=rep_food):
            temp_pop.append([food_init,init_pop[i][1]])
            temp_pop.append([food_init,init_pop[i][1]])
        elif(init_pop[i][0]>=0):
            temp_pop.append(init_pop[i])
    return(temp_pop)

def generate_part(nb_egoist):
    prob=np.random.uniform(0,1,nb_egoist)
    return(prob/np.sum(prob))

E=[]
S=[]
def evolution_pop(init_pop):
    ego=0
    sha=0
    for ind in init_pop:
        if(ind[1]==0):
            sha+=1
        else:
            ego+=1
    # E.append(ego)
    # S.append(sha)
    E.append(ego/len(init_pop))
    S.append(sha/len(init_pop))

for i in range(num_day):
    qty_food,food_day=generate_food(max_food)
    food_day=interested_in(qty_food,food_day)
    init_pop=current_food_update(init_pop,food_day,value_food)
    init_pop=death_birth(init_pop)
    evolution_pop(init_pop)

plt.plot(np.linspace(0,num_day,num_day),E,label="Egoist")
plt.plot(np.linspace(0,num_day,num_day),S,label="Share")
plt.legend()
plt.show()
