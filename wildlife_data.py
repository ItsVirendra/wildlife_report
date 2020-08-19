



class WildLife_data:
    def add_new_animal():
        selOpt = """
        1. Add animal Detail 
        2. Add animal type"""
        print(selOpt)
        try:
            sel_data = int(input("select option: "))
        except:
            print("Please mention the number")
        if(sel_data == 1):
            self._add_animal_details()
        elif(sel_data == 2):
            self._add_animal_type()
        
    def _add_animal_details(self):
        print("animal details")
    
    def _add_animal_type(self):
        print("animal type")
        