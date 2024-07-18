# simple-ESS-simulation

The goal of these files is to produce a tkinter windows showing the evolution of a population where each individual have either an egoist gene or an altruist gene. In particular, this show that for certain parameters it is possible to obtain an equilibrum between the egoist population and the altruist population. In other word it show in a very simple simulation that altruism can be a consequence of evolution. Obviously, this is a simple simulation like I said, in reality many more parameters would have to be taken into account. In a future project, I intend to train neural nets using reinforcement learning in a simliar situation, to see if such strategies could emerge from simple neural networks.

## The tkinter windows

Here is the result of executing simple_ESS_visual.py what it does is self explanatory, for more details about the parameters look at the next section. I may implement a visual in a later part where the individuals go get their food/fight/get it.

![ESS_window](https://github.com/user-attachments/assets/17588b9c-38ae-462b-bf5b-cf10c3345532)


## How it work

At the beginning a population of size **pop_size** is generated. The repartition of egoist and altruist in the initial population is determined by the probability of being egoist **prop_egoist**. Each individual begin with a set ammount of food, that ammount is the same for every individual and is determined by **food_init**

Then for each day a certain number of food is created, the exact number is obtained by drawing a number from the uniform distribution between one and **max_food**. Maybe I should implement a fixed ammount of food here.

When the food for the day has been decided, each individual in the population choose randomly a certain food. Here again that choice is made by drawing a number from the uniform distribution. It is important to note that there may be multilple individuals on the same food or none.

If there is only one individual on a certain food. Then that individual take all the food for himself, adding to it's current ammount food a certain quantity determined by **food_value**. Now if there is multiple individuals on the same food the repartition is done according to the following rules:
1. If there is only altruists individuals the the food is shared equaly amongst them
2. If there is altruists and egoists then the altruists don't get anything
3. If there is multiple egoists on a food they fight, this fight make them use some of their current food, as such a penalty is deduced of their current food, this penalty is controled by **fight_penalty**
4. After the fight the food is distributed in unequal part randomly between the egoist.

At the end of each day a penalty is deduced from the current food of all the individuals, representing the consumption for the day. The value of that penalty is controlled by **loss_food**. Moreover at the end of the day if an individual has less or equal to zero current food he die. On the contrary an individual having more than **rep_food** current food duplicate and the current food of the two individuals is set to **food_init**.

Finaly this is repeated for **num_day** number of time.
