little_pig_count = 3

def knock():
    print(f"There are {little_pig_count} little pigs.")

    # this step is optional and gives us a chance to
    # play around with trying to _update_ a global
    # variable within a function rather than just reading
    # from it

    # this line would fail; we can't update the global
    # little_pig_count = 4

    # unless we use the global keyword to tell python this
    # is the symbol from the global scope
    
    # global little_pig_count
    # little_pig_count = 4

    # suggest playing around with and without the global
    # keyword and placement of declaration and update to
    # show the variety of errors that can happen here

    # at the end of the day, strong discourage using the
    # global keyword because of the confusion it brings
    
knock()


print(f"{little_pig_count=}")

