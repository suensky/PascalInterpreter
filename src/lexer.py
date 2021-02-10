from token import *

RESERVED_WORDS = {
    'BEGIN': Token(BEGIN, 'BEGIN'),
    'END': Token(END, 'END')
}

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

    def peek(self):
        next_pos = self.pos + 1
        if next_pos >= len(self.text):
            return None
        return self.text[next_pos]

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


    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        return RESERVED_WORDS.get(result, Token(ID, result))

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
            token = self.get_next_token()

        elif current_char.isalpha():
            token = self._id()

        elif current_char == ':' and self.peek() == '=':
            self.advance()
            self.advance()
            token = Token(ASSIGN, ':=')

        elif current_char == ';':
            self.advance()
            token = Token(SEMI, ';')

        elif current_char == '.':
            self.advance()
            token = Token(DOT, '.')

        elif current_char.isdigit():
            token = Token(INTEGER, self.integer())

        elif current_char == '+':
            token = Token(PLUS, current_char)
            self.advance()

        elif current_char == '-':
            token = Token(MINUS, current_char)
            self.advance()

        elif current_char == '*':
            token = Token(MUL, current_char)
            self.advance()

        elif current_char == '/':
            token = Token(DIV, current_char)
            self.advance()

        elif current_char == '(':
            token = Token(LPAREN, current_char)
            self.advance()

        elif current_char == ')':
            token = Token(RPAREN, current_char)
            self.advance()

        else:
            self.error()

        print(token)
        return token