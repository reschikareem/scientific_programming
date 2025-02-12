import time
import random
import pandas as pd
from collections import Counter

# Create list to save results
trials_list = []

# Initialize counter of trials with occurence of '6'
no_six = 0

# Trials
for i in range(1, 1000, 1):
     
    # Generates a random number from 1 and 6
    no = random.randint(1,6)
     
    if no == 1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
    if no == 2:
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
    if no == 3:
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
    if no == 4:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
    if no == 5:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
    if no == 6:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")

    # Store results
    trials_list.append(no)

    # Count occurence of '6'
    if no == 6:
        no_six += 1

    # Break
    if no_six >= 20:
        break

    # Wait a second
    time.sleep(0.25)

# Analyse results
out = dict(Counter(trials_list))
print(pd.DataFrame.from_dict(out, 
                             columns=['Counts'], 
                             orient='index').sort_index())