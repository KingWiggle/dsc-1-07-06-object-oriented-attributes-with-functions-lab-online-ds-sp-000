class School:
    def __init__(self, name = None, roster = {}):
        self._name = name
        self._roster = roster
        
    def get_roster(self):
        return self._roster
    
    def set_roster(self, roster):
        self._roster = roster
        
    roster = property(get_roster, set_roster)
    
    def add_student(self, student, grade):
        grade_list = self.roster.get(str(grade),[])
        grade_list.append(student)
        self.roster[str(grade)] = grade_list
        
    def grade(self, grade):
        return self.roster[str(grade)]
    
    def sort_roster(self):
        for key in self.roster.keys():
            self.roster[key].sort()
        return self.roster
        