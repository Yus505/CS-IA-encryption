# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

import random

heads_tails = random.randint(0, 1)
if heads_tails == 1:
    print("tails")
else:
    print("heads")