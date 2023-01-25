#hybrid
class state:
    type1="andhrapradesh"
    type2="telangana"
class andhrapradesh(state):
    pass
class telangana(state):
    pass
class Telugu(andhrapradesh,telangana):
    pass
obj=Telugu()
print(obj.type1)
print(obj.type2)
    
