# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 1

possible_actions = ['taking up yoga.', 'sleeping eight hours a night.',
                    'relaxing.', 'not working on weekends.',
                    'spending two hours a day with friends.']

'''
Precondition: possible_actions is the list defined above

Postconditions:
1. (Welcome): A welcome message is on the console
2. (user_complaint): user_complaint is the user's response to a prompt for the
user's complaint
3. (how_long): how_long is the user's string response to "How many months have
you experience ...?" AND Eliza300 sympathized, mentioning duration
4. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_actions are on separate lines
on the console, each preceded by "Try ".
'''

# Welcome message from Eliza300 is printed on the console
print("Thank you for using Eliza300, a fun therapy program.")

# User prompted to input their emotional complaint
# User complaint stored as string in variable 'user_complaint'
print("Please describe your emotional complaint--in one punctuation-free line:")
user_complaint = input()

# User prompted to input number of months they have experienced their complaint
# User input stored as string in variable 'how_long'
print("How many months have you experienced '" + user_complaint + "'?")
how_long = input()

# Eliza300 sympathetic response, mentioning during, printed to console
print(how_long + " months is significant. Sorry to hear it.")

# Eliza advice, which is dependent on value of how_long, printed to console
# If how_long < 3, Eliza suggests user comes back when how_long is 3
# Otherwise, Eliza provides suggestions from list of possible_actions
if int(how_long) < 3:
    print("Please return in " + str(3 - int(how_long)) + " months.")
else:
    for possible_actions_index in range(5):
        print("Try " + possible_actions[possible_actions_index])
