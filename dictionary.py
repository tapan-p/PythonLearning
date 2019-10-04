TestUser ={}
TestUser['first'] = 'TestFirst'
TestUser['last']= 'TestLast'

TestUser1 = {'first':'testfirst', 'last':'testlast'}
people = [TestUser,TestUser1]
people.append({'first':'someUserfirst','last':'someuserlast'})
print(people)
print()
presenters = people[0:2] #creates the brand new list.. doesn't affect the original
print(presenters) 
print(len(presenters))
print(len(people))