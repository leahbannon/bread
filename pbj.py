slices_of_bread=2
has_peanut_butter=True
has_jelly=True

if slices_of_bread>=4:#Note: I have enough bread to make multiple sandwiches.#
    print "You can make {0} sandwiches.".format(slices_of_bread/2) #.format takes what is in the () and puts it in the {} 

    if has_peanut_butter==True and has_jelly==False:
        print "You can make a peanut butter sandwich."
    elif (has_peanut_butter and has_jelly==True):
        print "You can make a peanut butter and jelly sandwich."
       
elif slices_of_bread==2:#Note: I have enough bread to make one sandwich.#
    print "You can make {0} sandwich.".format(slices_of_bread/2)

    if has_peanut_butter==True and has_jelly==False:
        print "You can make a peanut butter sandwich."
    elif (has_peanut_butter and has_jelly==True):
        print "You can make a peanut butter and jelly sandwich."
    
elif slices_of_bread<2:
    print "You can't make any sandwiches."

else:
    print "You might be able to make half sandwiches."
