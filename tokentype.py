# definir todos los tokens enumerados
import enum
class TokenType(enum.Enum):
    EOF = 1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    ##KEYWORDS
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    #OPERADORES-
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

    import sys
from tokentype import *

class Lexer:
    #Constructor 
    def __init(self, input):
        self.source=input
        self.curChar = ""
        self.curPos = -1
        self.nextChar()

    #Procesa el caracter actual 
    def nextChar(self):
        self.curPos+=1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source(self.curPos)

    #Anticipa el caracter que sigue
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    #Muestra el error por si hay token invalido
    def about(self, message):
        sys.exit("Error de léxico" + message)

    #saltar los espacios en blanco
    def skipWhiteespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\R':
            self.curChar()

    #Saltar comentario
    def skipComment(self):
        if self.curChar == '#':
            self.nextChar