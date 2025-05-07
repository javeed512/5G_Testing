# declare global variable 
message = 'Hello' 

def greet(): 
# declare local variable 

    message = "Thank you"  #here local var will be given first priority

    print('Local', message) 
greet() 

print('Global', message)