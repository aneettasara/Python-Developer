class person:
    def __init__(self):
        self.profile_name = None
        self.followers_count = None
    def set(self,name,count):
        self.profile_name = name
        self.followers_count = count
    def account(self):
        print("Instagram Account "+self.profile_name+" has "+str(self.followers_count)+" followers")
        
class pet:
    friend = person()
    def abc(self):
        print("Name of Pet: "+pet.id)
        
class robot:
    def display(self,name):
        print("Robot Name: "+name)
        
class shop:
    name = "Status"    
    def printName(self):
        print("Name of Shop using class name - shop.name: "+shop.name)
        print("Name of Shop using self - self.name: "+self.name)

print("Classes and Objects PART 2")

s1 = shop()
s2 = shop()
s1.printName()
print("SHOP 1 s1: "+s1.name+"\nSHOP 2 s2: "+s2.name)

r1 = robot()
r1.display("Blue") 
 
p1 = person()
p2 = person()
p1.set("AJ",909)
p2.set("Sara",121)
p1.account()
p2.account()
p1.following = p2
print("p1.following :")
p1.following.account()

pet1 = pet()
pet1.friend = p2
print("Profile name of pet 1:")
print(pet1.friend.profile_name)
