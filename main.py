playing = True
from cat import*
# instance: a specific occurance of a class
mimi = cat("mimi","brown")
print (mimi.name)
print (mimi.colour)

chilli = cat("chilli","black")
print (chilli.name)
print (chilli.colour)

new_cat = input("would you like to add a new cat")
if new_cat.lower() == "y" or "yes":
    name_cat = input("what is the cats name?: ")
    cat_colour = input("what is the colour of this cat?: ")
    name = name_cat
    colour = cat_colour
    my_cat = cat(name, colour)
    print (my_cat.name)
    print (my_cat.colour)






