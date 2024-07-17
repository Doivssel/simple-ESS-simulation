import numpy as np

class ESS(object):

    def __init__(self,max_food,food_init,loss_food,value_food,rep_food,fight_penalty,pop_size,prob_egoist,num_day):
        """
        Parameters:
        Look at the README
        """
        self.max_food=max_food
        self.food_init=food_init
        self.loss_food=loss_food
        self.value_food=value_food
        self.rep_food=rep_food
        self.fight_penalty=fight_penalty
        self.pop_size=pop_size
        self.prob_egoist=prob_egoist
        self.num_day=num_day
        self.init_pop=[[food_init,(np.random.uniform(0,1)<prob_egoist)*1] for _ in range(pop_size)]
        self.egoist=[]
        self.altruist=[]
        self.prop_ego=[]
        self.prop_alt=[]

    def generate_food(self):
        """
        Parameters:
        None
        
        Goal:
        Generate a random amount of food between 1 and self.max_food
        
        Note:
        Maybe I should make it constant."""
        qty_food=np.random.randint(1,self.max_food)
        food_day=[[[],[]] for _ in range(qty_food)]
        return(qty_food,food_day)

    def interested_in(self,qty_food,food_day):
        """
        Parameters:
        qty_food: int, the quantity of food for the day from generate food
        food_day: array, food of the day from generate food
        
        Goal:
        Each individual choose randomly a food then their choice is stored in food day
        with their gene"""
        for j in range(len(self.init_pop)):
            ind_loc=np.random.randint(0,qty_food)
            food_day[ind_loc][0].append(j)
            food_day[ind_loc][1].append(self.init_pop[j][1])
        return(food_day)
    
    def generate_part(self,nb_egoist):
        """
        Parameters:
        nb_egoist: int, number of egoist individual on a food
        
        Goal:
        Divide the food in part of random size amongst the egoist"""
        prob=np.random.uniform(0,1,nb_egoist)
        return(prob/np.sum(prob))

    def current_food_update(self,food_day):
        """
        Parameters:
        Same as before
        
        Goal:
        Update the current food parameters for each individual following a few simples rules
        described in the README"""
        for food in food_day:
            ind_comp=len(food[0])
            if(ind_comp==1):                                                #only one ind  on a food, it get all the food
                self.init_pop[food[0][0]][0]+=self.value_food
            elif(ind_comp>1):                                               #many ind on a food, must attribute it following certain rules
                nb_egoist=np.sum((np.array(food[1])==1)*1)
                if(nb_egoist==0):                                           #no egoist, then food shared equally
                    for ind in food[0]:
                        self.init_pop[ind][0]+=np.round(self.value_food/ind_comp,2)
                elif(nb_egoist==1):                                         #one egoist, the egoist get all the food
                    egoist=np.argwhere(np.array(food[1])).flatten()
                    ind=food[0][egoist[0]]
                    self.init_pop[ind][0]+=self.value_food
                elif(nb_egoist>1):                                          #multiple egoists, divide unequally among them and get a penalty for the fight
                    egoist=np.argwhere(np.array(food[1])).flatten()
                    part=self.generate_part(nb_egoist)
                    for j in range(nb_egoist):
                        ind=food[0][egoist[j]]
                        self.init_pop[ind][0]+=np.round(self.value_food*part[j]-self.fight_penalty,2)
        for i in range(len(self.init_pop)):                                      #all get a penalty at the end of the day
            self.init_pop[i][0]-=self.loss_food

    def death_birth(self):
        """
        Parameters:
        None
        
        Goal:
        Kill an individual if current food inf to zero if it's superior
        to rep food duplicate the individual while setting current_food to init_food for
        both inds"""
        temp_pop=[]
        for i in range(len(self.init_pop)):
            if(self.init_pop[i][0]>=self.rep_food):
                temp_pop.append([self.food_init,self.init_pop[i][1]])
                temp_pop.append([self.food_init,self.init_pop[i][1]])
            elif(self.init_pop[i][0]>=0):
                temp_pop.append(self.init_pop[i])
        self.init_pop=temp_pop

    def evolution_pop(self):
        """
        Parameters:
        None
        
        Goal:
        Used to gather some stats like the number of indivuduals for each gene and their prop
        """
        ego=0
        sha=0
        for ind in self.init_pop:
            if(ind[1]==0):
                sha+=1
            else:
                ego+=1
        l=len(self.init_pop)
        self.egoist.append(ego)
        self.altruist.append(sha)
        self.prop_ego.append(ego/l)
        self.prop_alt.append(sha/l)

    def simulation(self):
        """
        Parameters:
        None
        
        Goal:
        Simulate the evolution of the population under the descibed rules"""
        for i in range(self.num_day):
            qty_food,food_day=self.generate_food()
            food_day=self.interested_in(qty_food,food_day)
            self.current_food_update(food_day)
            self.death_birth()
            self.evolution_pop()


