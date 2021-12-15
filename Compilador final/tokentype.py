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
    SIFI = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    OFO=121
    POFOR=122
    CAFAMBIFIOFO=123
    IMPIRIFIMIFIRIFIR=124
    SIFIOFONOFO=125
    CAFASOFO=126
    MIFIEFENTEFERAFAS=127
    REFEPEFETIFIR=128
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