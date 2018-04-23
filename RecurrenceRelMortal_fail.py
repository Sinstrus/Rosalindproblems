#Same as RecurrenceRel but now the rabbits die after 3 months (only reproduce twice before dying)

n = 80
k = 1
lifespan = 18

# I must take a different approach. Thinking forward, instead of recursively.


#THIS ATTEMPT FAILED BECAUSE OF BAD APPROACH. PROCESSING TIME GREW EXPONENTIALLY AS INPUT GREW LINEARLY
#The fatal flaw is that the program iterates over every single rabbit and makes a decision
#Is there a way to treat these subpopulations of rabbit pairs as groups instead?
class Rabbitpair:

    def __init__(self):
        self.age = 0
        self.alive = True

#start with one pair of living rabbits, age 1 (non-reproductive)
#for month in range(1,number of months)
    #for rabbit in list:
    #   if rabbit pair is alive and of reproductive age (age>1):
    #       add an age 1, living rabbit pair to the end of the list
    #       add 1 month to rabbit pair's age
    #       if rabbit pair age > 3:
    #           rabbit pair is now dead

rabbitlist = []
prog = Rabbitpair()
rabbitlist.append(prog)

for month in range(0,n):
    # print month
    if month > 0:
        newborn_rabbits = []
        for rabbit in rabbitlist:
            # print rabbit.alive
            # print rabbit.age
            # if len(rabbitlist) > 50:
            #     break
            if rabbit.alive and rabbit.age == 0:
                rabbit.age = rabbit.age + 1
            elif rabbit.alive and rabbit.age > 0:
                new_rabbit = Rabbitpair()
                newborn_rabbits.append(new_rabbit)
                # print "New rabbit pair born!"
                rabbit.age = rabbit.age + 1
            if rabbit.age > (lifespan - 1):
                rabbitlist.remove(rabbit)

        # for rabbit in rabbitlist:
        #     if not rabbit.alive:
        #         rabbitlist.remove(rabbit)

        rabbitlist = rabbitlist + newborn_rabbits

    print len(rabbitlist)

    # count = 0
    # for rabbit in rabbitlist:
    #     if rabbit.alive:
    #         count +=1
    # print count

count = len(rabbitlist)
# for rabbit in rabbitlist:
#     if rabbit.alive:
#         count +=1
print "The final number of rabbit pairs at month %s is %s." % (n,count)
