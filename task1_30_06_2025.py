#Create a class DataFrame that behaves in the following way: (Task 1 from lesson 1 - 30.06.2025)
#df = DataFrame({"name": ["Гошо", "Пешо"], "age": [30, 16]})
#print(df.shape)       # (2, 2)
#print(df["name"])         # ["Гошо", "Пешо"]
#df["height"] = [175, "по-висок от Стан"]
#print(df.shape)       # (2, 3)
#print(df)
## DataFrame (2x3)
## name | age | height
## Гошо | 30 | 175
## Пешо | 16 | по-висок от Стан
###############################################################
class DataFrame:
    def __init__(self, dic):
        self.dic=dic
        self.shape=(len(self.dic["name"]), len(self.dic))
    def __getitem__(self, key):
        return self.dic[key]
    def __setitem__(self, key, value):
        self.dic[key] = value
        self.shape=(len(self.dic["name"]), len(self.dic))
    def __str__(self):
        return f"{self.__class__.__name__} ({self.shape[0]}x{self.shape[1]})\nname | age | height\n{self.dic["name"][0]} | {self.dic["age"][0]} | {self.dic["height"][0]}\n{self.dic["name"][1]} | {self.dic["age"][1]} | {self.dic["height"][1]}"
        
        
df = DataFrame({"name" : ["Гошо", "Пешо"], "age": [30, 16]})
print(df.shape)
print(df["name"])
df["height"] = [175, "по-висок от Стан"]
print(df.shape)
print(df)
