class Employe:
    # class is made by object, class method, static method, constructer method like __init__(self)
    no_of_project_done = 22#class object or variable
    Powerment = 70
    def __init__(self, name, age, skill):#init is constructer 
        self.name = name
        self.age = age
        self.skill = skill

    def print_info(self):
        print(f"name of member is {self.name} and his age is {self.age}, he/she know {self.skill}")

    @classmethod#need to change class varibale/object value 
    def changing_member_no(cls, no):
        cls.no_of_project_done = no
    
    @classmethod#get argument using differnt thing like  one string that we can parse and pass the class constructer init
    def make_simple(cls, string):#another constructer
        # params = string.split("-")
        # # print(params)
        # return cls(*params)
        return cls(*string.split("-"))

    @staticmethod
    def something(string):
        return f"This is {string}"



class EsportPlayer: 
    no_of_games = 2
    Powerment = 90
    def __init__(self, Esport_name, games):
        self.Esport_name = Esport_name
        self.games = games

    def print_details(self):
        print(f"The Name of Player is {self.Esport_name} and he/she also plays Esport games like { self.games}")




class CoolProgrammer(Employe, EsportPlayer):   #order of class make imfact 
    CoolProgrammer_skills = "He/She knows Programming Langauges with also gaming.."
    Powerment = 100
    def skill_matter(self):
        super().print_info()
        # super().print_details()


    
        


Mahesh = Employe("Mahesh", 21, ["Python", "C"])#Employe Instance
ErMapsh = EsportPlayer("ErMapsh", ["PUBG PC", "Valorent"])#EsportPlayer instance

Er = CoolProgrammer("Mahesh", 21, ["Python", "C"])#CoolProgrammer inherited both class 
Er.skill_matter() 
print(Er.Powerment)