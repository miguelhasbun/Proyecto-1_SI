Keywords = {
    'ls' : 'KW_LS',
    'grep' : 'KW_GREP',
    'ping' : 'KW_PING'
}

class Lexer:
    lexeme = ""
    argument = []

    def __init__(self, argument):
        self.argument = list(argument)
    
    def getToken(self):
        for _, char in enumerate(self.argument):
            if char.isalpha():
                self.lexeme += char
            else:
                return 'ERROR'
        if self.lexeme in Keywords:
            return Keywords[self.lexeme]
        else:
            return 'ID'

    def getLexeme(self):
        return self.lexeme