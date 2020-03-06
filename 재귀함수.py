
def recursive(age):
    if(age == 0): 
        return age
    else:
        print("My age is %s" % age) 
        recursive(age-1)
        print("age %s is over" % age)
        return

recursive(5)
