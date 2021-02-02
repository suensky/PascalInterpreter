from parser import Parser
from lexer import Lexer

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        result = parser.expr()
        print(result)

if __name__ == '__main__':
    main()