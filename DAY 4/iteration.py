import itertools 

def loop_data(iter):
    return itertools.cycle(iter)

result = loop_data(['Tom','Ben','Charles','Dave'])
for i in result:
    print(i)

