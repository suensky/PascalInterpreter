from token import *

class Lexer():
    def __init__(self, text):
        # client string input, e.g., 3+5
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos]

    ##########################################################
    # Lexer code                                             #
    ##########################################################
    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = 0
        while self.current_char is not None and self.current_char.isdigit():
            result = result * 10 + int(self.current_char)
            self.advance()
        return result

    def get_next_token(self):
        """Lexical analyzer, also known as tokenizer or scanner

        This method breaks a sentence apart into tokens. One token
        at a time.
        """
        text = self.text
        if self.pos >= len(text):
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isspace():
            self.skip_whitespaces()
            return self.get_next_token()

        if current_char.isdigit():
            return Token(INTEGER, self.integer())

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.advance()
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.advance()
            return token

        if current_char == '*':
            token = Token(MUL, current_char)
            self.advance()
            return token

        if current_char == '/':
            token = Token(DIV, current_char)
            self.advance()
            return token

        if current_char == '(':
            token = Token(LPAREN, current_char)
            self.advance()
            return token

        if current_char == ')':
            token = Token(RPAREN, current_char)
            self.advance()
            return token

        self.error()