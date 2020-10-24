class people:
    def __init__(this,name):
        this.name = name
        this.lover = None
    def love(this,obj):
        this.lover = obj
        
I = people('I')
you = people('you')
while True:
    
    I.love(you)

