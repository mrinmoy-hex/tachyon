from token_types import TokenType
from tokens import Token
from utils import Error

class Lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []    # list to store scanner tokens

        self.start = 0
        self.current = 0
        self.line = 1

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_tokens(self):
        while not self.is_at_end():
            # we are at the beginning of the next lexeme
            # self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))

    # recognizing lexemes
    def scan_token(self):
        char = self.advance()

        if char == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif char == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '{':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '}':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == ',':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '.':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '-':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '+':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == ';':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '*':
            self.add_token(TokenType.ASTERISK)

        else:
            # handling unexpected characters
            Error.report(self.line, "", f"Unexpected chracter: '{char}'.")




    def add_token(self, type_, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type_, text, literal, self.line))









    # helper methods
    def advance(self):
        char = self.source[self.current]
        self.current += 1
        return char











