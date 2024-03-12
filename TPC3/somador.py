import re

class automatoSoma:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.total = 0
    
    def process(self, string):
        palavra = re.split(r'(\s+)', string)
        for i in palavra:
            if re.match(self.alphabet['on'], i):
                self.current_state = 'ON'
            elif re.match(self.alphabet['off'], i):
                self.current_state = 'OFF'
            elif re.match(self.alphabet['='], i):
                print('total: ' + str(self.total))
            elif re.match(self.alphabet['\d+'], i) and self.current_state == 'ON':
                self.total += int(i)

states = {'ON', 'OFF'}
alphabet = {'\d+': re.compile(r'\d+'), 'off': re.compile("[Oo][Ff]{2}"), 'on': re.compile("[Oo][Nn]"), '=': re.compile("=")}
transitions = {
    'ON': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('ON', 'output')
    },
    'OFF': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('OFF', 'output')
    }
}

automato = automatoSoma(states, alphabet, transitions, 'OFF', {'ON'})
f = open('teste.txt', 'r')
text = f.read()
automato.process(text)