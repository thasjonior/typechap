# exersice class
# exrecise string
# next exercise 
# previuous exercise 
# errors

class Exercise:
    def __init__(self):
        self.current_exercise=0
        self.missed_chars=0
        self.next_char=0

    
    @property    
    def ex_container(self):
        exercise1="asdf;lkjasdf;lkjasdf;lkjasdf;lkjasdf;lkj fdsajkl;fdsajkl;fdsajkl;fdsajkl;fdsajkl;"
        exercise2="asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj fdsa jkl; fdsa jkl; fdsa jkl; fdsa jkl;"
        exercise3="sad lad dad all add ask ass as;asks alas fall dads flak lass lads add;"
        exercise4="salad; a flask; a jaffa; flak falls;a lass adds a jaffa as a lad asks as sad as a lass; a flask falls all salads add jaffas as dad asks alas a sad dad; a lass adds a flask a lass adds; a dad asks all; ask a lad"
        exercise5="asdfgfd ;lkjhjk asdfgfd ;lkjhjk asdfgfd ;lkjhjkfgf jhj agf ;hj fgf jhj agf ;hj fgf jhj agf ;hj"
        exercise6="hag fag jag sag lag has gas ashglad shag flag lash sash hall half hag;shall glass sagas galas galls slash flash gash;"
        exercise7="a lass has had half a jaffaglass shall flash; all flags falla lad has had a fall; slash a gasha flag has a slash; all sagas add dashdad has had shag; alas a lad has a gasha glad lass has a gala; a sad lad had a saga"
        exercise8="ded ;ed led ked jed hed ded ;ed led ked jed hede;d eld ekd ejd ehd ead e;d eld ekd ejd ehd ead"
        exercise9="ed led keg leg elf elk she he;seed heed feed shed fled head lead helddeeds hedge ladle shade shelf legal leaks sheaf"
        exercise10="ash seeds fall; gales lash lakeshe half haggles as he sells a deskshe sells sea shells; he sells aleshe feels safe as he leashes a sledgehe has had hake; she fed eels as dad askedshe has a gashed leg; he has a slashed head"
        return [exercise1,exercise2,exercise3,exercise4,exercise5,exercise6,exercise7,exercise8,exercise9,exercise10]

    def next_exercise(self ,current_exercise):
        return current_exercise +1

    def previous_exercise(self,current_exercise):
        return current_exercise -1

    def check_correctness(self):
        if char = picked_char:
            self.missed_chars+1
        return self.missed_chars

    def get_results(self,exercise):
         chars=len(exercise)
         result=((chars-self.missed_chars)/chars)*100
         return f"{result}%"

    def pick_char(self):
        pass

    
