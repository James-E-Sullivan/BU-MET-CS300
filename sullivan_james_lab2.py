'''
Postconditions
1 (Welcome): A welcome message is on the console
2 (Complaint): A complaint was entered by the user in response to a prompt
AND Eliza has responded "I am sorry to hear you report <the complaint entered
by the user>"
'''

# Prints a welcome message and user prompt to the console
print("Thank you for using Eliza300, a fun therapy program.")
print("Please state your emotional complaint then hit ENTER:")

# Keyboard input from user is stored as variable 'complaint'
complaint = input()

# Prints a response from Eliza300, which includes the complaint text
print('I am sorry to hear you report ' + '"' + str(complaint)
      + '"!')
