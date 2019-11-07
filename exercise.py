

class Exercise:
    """
    An exercise:
    - Part of the domain

    - An exercise should keep its own state including passes, percentage score, etc
    - This class shouldn't know anything about a widget
    - This exercise is assignable to a person, so they can keep track of the progress they make for 
      particular exercises.
    """
    def __init__(self, name, text):

        if text is None:
            return 'no text'
            
        self.name = name
        self.text = text
        self.passes = 0
        self.current_char_index=0
        self.length = len(self.text)
    
    def next_char(self):
        self.current_char_index += 1

    @property
    def current_char(self):
        return self.text[self.current_char_index]

    def add_passes(self):
        self.passes += 1

    @property
    def percentage_score(self):
        return f"{self.passes / self.length * 100:.2f}"

    @property
    def live_score(self):
        return f"{self.passes / (self.current_char_index) * 100:.2f}"


    

    