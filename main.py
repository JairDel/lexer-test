import sly

class L2Lexer(sly.Lexer):
    # Define the set of token names
    tokens = { A,B,C }

    # Ignore spaces
    ignore = ' \t'

    # Regular expressions for the tokens
    A = r'a+'
    B = r'b|c'
    #C = r'c'
    C = r'd+'
    def C(self,t):
        print('Goat')
        exit(0)

    # Error handling
    def error(self, t):
        print(f'Fuck U Pussy')
        self.index += 1
        exit(0)

# Testing the lexer
if __name__ == '__main__':
    lexer = L2Lexer()
    data = input("Cadena: ")  # Test input string
    for tok in lexer.tokenize(data):
        print(f'type={tok.type}, value={tok.value}')
