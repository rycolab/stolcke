

class Stolcke(object):


    def __init__(self):
        pass

    def attach(self):
        pass

    def predict(self):
        pass

    def scan(self):
        pass

    def parse(self, sentence):
        chart = Chart()
        agenda = Agenda()
        for k in range(len(sentence)):
            item = agenda.pop()
            if len(item.b) == 0:
                attach()
            elif item.b[0] in self.grammar.terminals:
                scan()
            else:
                predict()
                
            
