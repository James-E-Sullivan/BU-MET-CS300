# A list of key words for depression
key_words = ['depress', 'sad', 'down']

def get_complaint_type(a_user_complaint):
    '''
    Precondition: a_user_complaint is a string

    Postcondition:
    Either a_user_complaint contains one of key_words
        AND observed_complaint_type is the set consisting of "Depression"
    OR observed_complaint_type is the empty set

    Returns: complaint_set #observed_complaint_type defined outside the scope
    of this function

    Example: user entered "I've been saddened by world conflicts"
    and ("Depression") was returned.
    '''

    # An empty set is created to store complaint types
    complaint_set = set()

    # Loops through elements in key_words
    for key_words_element in key_words:

        # Element is added to complaint_set if it's part of a_user_complaint
        if str(key_words_element) in a_user_complaint.lower():
            complaint_set.add(key_words_element)

    return complaint_set


'''
Postconditions
1 (Welcome): A welcome message is on the console
2 (user_complaint): user_complaint is the user's response in reply to "Please
state your complaint:"
3 (observed_complaint_type): observed_complaint_type =
get_complaint_type(user_complaint)
4 (Advice displayed): EITHER "You have depression" OR nothing is displayed
according to observed_complaint_type
'''



# (Welcome): Postcondition 1

print("Thank you for using Eliza300, a fun therapy program.")

# (user_compalint): Postcondition 2

print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3

observed_complaint_type = get_complaint_type(user_complaint)

# (Advice Displayed): Postcondition 4

if len(observed_complaint_type) > 0:
    print("You have depression")

