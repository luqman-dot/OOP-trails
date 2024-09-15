class laptop:
    def __init__ (self,name,model,color,brand):
        self.name = name
        self.model = model
        self.color = color
        self.brand = brand
        
laptop1 = laptop("vostro",4300,"red","dell")
laptop2 = laptop("pro",43,"silver","hp")
laptop3 = laptop("thinkpad",1,"black","lenovo")
laptop4 = laptop("yoga",0,"gray","lenovo")
laptop1 = laptop("macbook",4300,"pink","apple")

print(laptop1.name)
print(laptop2.color)
print(laptop3.model)