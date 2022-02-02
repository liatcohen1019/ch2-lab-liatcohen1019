#Part A
weeks = 16
print("weeks:", weeks, type(weeks))
classes = 5
print ("classes:", classes, type(weeks))
tuition = 6000
print("tuition:", tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week= 2
print("Classes per week:", classes_per_week, type(classes_per_week))
cost_per_class=(cost_per_week/ classes_per_week)
print("cost_per_class:", cost_per_class)

#Part B
import random 
list=["apples", "oranges", "bananas", "carrots", "cucumbers"]
rand_food =(random.choice(list))
print ("you should eat", rand_food)
