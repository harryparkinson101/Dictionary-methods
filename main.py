dict = {
  '123': [1,2,3],
  '123': 'hello'
}

# this will print 'hello' because keys must have diffferent values or ele the key gets overwritten to the most recent value eg 'hello'

print(dict['123'])

# dictionary methods
# .get()

user = {
  'basket': [1,2,3],
  'greet': 'hello'
}


# this will check if age is a key in user. will return None
print(user.get('age',22))
# adding the 22 after age will assign 22 to the key 'age' but if age exists and is 20 for example calling print(user['age']) will return 20

user2 = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 34
}

# this checks to see if 'basket' is a key in user. because it is a key this returns True
print('basket' in user)

# this will return false as it is checking to see if 'size' is a ket value pair in user.
print('size' in user)

# this will return True as age is a key in user
print('age' in user.keys())

# this returns True as 'hello' is a value within user
print('hello' in user.values())

# this clears the dictionary but doesnt return anthing
#user.clear()
# this will return user as an empty dictionary
print(user)
# this clears the dictionary returns None 
#print(user.clear())


harry = {
  'age': 22,
  'height': 180,
  'weight': 210,
  'superpower': 'shapeshifting'
}
# this copies the contents of harry and creates harry_clone
harry_clone = harry.copy()
print(harry_clone)
# this removes the key 'age' from harry and returns the value of age which it has removed

print(harry.pop('age'))
# this shows the contents of harry, now with age key value pair removed
print(harry)
# this prints harry_clone which has not been changed from the original harry 
print(harry_clone)

# .popitem()

jiada = {
  'age': 23,
  'superpower' : 'teleportation',
  'weakness': 'sausages'
  
}

# This method used to remove a random key value pair from a dictionary. After v3.7 this method now removes the last key value pair from a dictionary
jiada.popitem()
# this will print jiada without her weakness as .popitem() removed the last pair
print(jiada)

# .update()

# This updates the value of the age key to 33
jiada.update({'age': 33})
print(jiada)

# As it turns out jiada does have a weakness!
 # we can add it in with .update() 

jiada.update({'weakness': 'harrys cock'})
print(jiada)