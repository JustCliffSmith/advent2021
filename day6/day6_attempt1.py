import numpy as np
#from numba import jit

with open("input6.txt", "r") as f:
    lines = f.readlines()

# In this case there's only one line.
starting_state = lines[0].strip().split(",")
starting_state = [int(x) for x in starting_state]
state = np.array(starting_state)
print("Initial state:", state)

# Change this for day 1 (80 days) or day 2 (256 days).
days = 160
#for day in range(1, days+1):
#    zero_count = state[state == 0].shape[0]
#    if zero_count > 0 :
#        state = state -1
#        state[state == -1] = 6
#        state = np.append(state, [8] * zero_count)
#    else:
#        state = state - 1
#    if day %  16 == 0:
#        print(f"After {day} days:", state, state.shape[0]
#
for day in range(1, days+1):
     state = np.append(state, [9] * state[state == 0].shape[0])
     state = state -1
     state[state == -1] = 6
     if day %  16 == 0:
         print(f"After {day} days:", state, state.shape[0])


#@jit(nopython=True)
#def lanternfish_growth(days, state):
#    for day in range(1, days+1):
#         state = np.append(state, [9] * state[state == 0].shape[0])
#         state = state -1
#         state[state == -1] = 6
#    return state.shape[0]
#
#count = lanternfish_growth(days, state)
#print(count)
