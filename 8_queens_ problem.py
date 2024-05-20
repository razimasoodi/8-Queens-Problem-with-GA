import random

parents=[]
population=[]
bp=[]
best_childern=[]

def random_choromosome():
    choromosome=[]
    while len(choromosome)!=8:
        i=0
        x=random.randint(1,8)
        if x not in choromosome:
             choromosome.append(x)
        else:
             i+=1
    #print(choromosome)     
    return choromosome


def fitness(choromosome):
    fitness_value=0
    i=0
    for i in range (i,7):
        for j in range (i+1,8):
            if abs(i-j)==abs(choromosome[i]-choromosome[j]):
                fitness_value+=1
    #print("fitness=",fitness_value)            
    return fitness_value
  

def parent_select(parents):
    best_parent=[]
    parents.sort(key = fitness )
    #print("new parents using fitness",parents)
    best_parent.extend(parents[3:5])
    #print("best_parent",best_parent)
    return best_parent

def recombination(choromosome1,choromosome2):
    child1=[]
    child2=[]
    crossover=random.randint(0,7)
    #print(crossover)
    child1.extend(choromosome1[0:crossover+1])
    child2.extend(choromosome2[0:crossover+1])
    while len(child1)!=8:
        for i in range(crossover+1,8):
             if choromosome2[i] not in child1:
                child1.append(choromosome2[i])
        for i in range(0,crossover+1):
             if choromosome2[i] not in child1:  
                child1.append(choromosome2[i])
                         
    while len(child2)!=8:              
        for i in range(crossover+1,8):
             if choromosome1[i] not in child2:
                child2.append(choromosome1[i])
        for i in range(0,crossover+1):
             if choromosome1[i] not in child2:  
                child2.append(choromosome1[i])
                  
    return(child1,child2)

def mutate(choromosome):
     x=random.randint(0,7)
     #print("x=",x)
     y=random.randint(0,7)
     #print("y=",y)
     m=0
     if x==y:
         pass
        #print("mutation is not possible")
     else:
        m=choromosome[x]
        choromosome[x]=choromosome[y]
        choromosome[y]=m
     #print("choromosome after mutate=",choromosome)
     #if fitness(choromosome)==0:
         
     return choromosome
    
def survivor_select(population):
    best_child=[]
    f=[]
    population.append(mutate(childern[0]))
    population.append(mutate(childern[1]))
    for i in population:
        population.sort(key = fitness, reverse=True)
    del population[0:2]
    for i in population:
        if fitness(i)==0:
            best_child.append(i)
        f.append(fitness(i))    
    return (population,best_child,min(f))
ff=[]
for i in range(100):
    population.append(random_choromosome())
    
for k in range(10000):
    print("k=",k)
    for j in range(5):
        z=random.randint(1,99)
        parents.append(population[z])
    bp=parent_select(parents)
    childern=recombination(bp[0],bp[1])
    population,best_childern,f= survivor_select(population)
    ff.append(f)
    if best_childern!=[]:
        break
   
    
print('ff=',ff)
if best_childern==[]:
    #solutions=population[99]
    print(" choromosomes that have the best fitness=",population[90:99])
else:
    print ("solutions = ",best_childern)
    print ("solution_num = ",len(best_childern))
for i in best_childern:
    for t in i:
        for j in range(1,9):
            if(j==t):
               print(" o"*(j-1)+" x"+" o"*(8-j)) 
    print() 
       
