from random import *
items = []
for i in range(10):
    items.append(randint(1, 20))

print(items)

for x in range(len(items) - 1):
    print(f"checking elem #{x} = {items[x]}")
    
    for o in range(x + 1, len(items)):
        print(f"\t with elem #{o} = {items[o]}")
        
        if items[x] < items[o]:
            print(f"\t\t swapping...")            
            a = items[x]
            items[x] = items[o]
            items[o] = a
            print(f"\t {items}")
            print(f"\t checking elem #{x} = {items[x]}")
            
print(items)