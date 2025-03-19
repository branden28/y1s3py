'''X = [' i2', 'o4', '23 ', '\te5', '99', 'e7\t', ' o9', 'i1', 'e7']

i_list = [s for s in X if s.lstrip()[0] == 'i']
o_list = [s for s in X if s.lstrip()[0] == 'o']
e_list = [s for s in X if s.lstrip()[0] == 'e']
other_list = [s for s in X if s.lstrip()[0] not in ('i', 'o', 'e')]

print("i_list =", i_list)
print("o_list =", o_list)
print("e_list =", e_list)
print("other_list =", other_list)'''

import time

try:
    for i in range(1, 11):
        print(i, end=' ', flush=True)
        time.sleep(0.5)  
except KeyboardInterrupt:
    print("\ncrtl+C is detected")
finally:
    print("done")
