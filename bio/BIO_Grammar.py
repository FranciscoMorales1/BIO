# Generated from BIO_Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,314,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,89,8,1,1,2,1,2,5,2,93,8,2,10,2,12,2,96,
        9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,106,8,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,121,8,5,10,5,12,5,124,9,
        5,1,5,1,5,3,5,128,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,3,11,160,8,11,1,11,1,11,1,12,1,12,1,12,1,12,
        3,12,168,8,12,1,12,1,12,1,12,1,13,1,13,1,13,5,13,176,8,13,10,13,
        12,13,179,9,13,1,14,1,14,1,15,1,15,1,15,5,15,186,8,15,10,15,12,15,
        189,9,15,1,16,1,16,1,16,5,16,194,8,16,10,16,12,16,197,9,16,1,17,
        1,17,1,17,5,17,202,8,17,10,17,12,17,205,9,17,1,18,1,18,1,18,5,18,
        210,8,18,10,18,12,18,213,9,18,1,19,1,19,1,19,5,19,218,8,19,10,19,
        12,19,221,9,19,1,20,1,20,1,20,5,20,226,8,20,10,20,12,20,229,9,20,
        1,21,1,21,1,21,3,21,234,8,21,1,22,1,22,1,22,1,22,1,22,3,22,241,8,
        22,1,23,1,23,5,23,245,8,23,10,23,12,23,248,9,23,1,24,1,24,3,24,252,
        8,24,1,24,1,24,1,24,1,24,1,24,3,24,259,8,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,3,25,271,8,25,1,26,1,26,1,26,3,26,
        276,8,26,1,26,1,26,1,27,1,27,1,27,5,27,283,8,27,10,27,12,27,286,
        9,27,1,28,1,28,1,28,1,28,5,28,292,8,28,10,28,12,28,295,9,28,3,28,
        297,8,28,1,28,1,28,1,29,1,29,1,29,1,29,5,29,305,8,29,10,29,12,29,
        308,9,29,3,29,310,8,29,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        0,5,1,0,45,46,1,0,47,50,1,0,51,52,1,0,53,55,1,0,13,32,326,0,63,1,
        0,0,0,2,88,1,0,0,0,4,90,1,0,0,0,6,99,1,0,0,0,8,103,1,0,0,0,10,109,
        1,0,0,0,12,129,1,0,0,0,14,135,1,0,0,0,16,145,1,0,0,0,18,148,1,0,
        0,0,20,151,1,0,0,0,22,156,1,0,0,0,24,163,1,0,0,0,26,172,1,0,0,0,
        28,180,1,0,0,0,30,182,1,0,0,0,32,190,1,0,0,0,34,198,1,0,0,0,36,206,
        1,0,0,0,38,214,1,0,0,0,40,222,1,0,0,0,42,230,1,0,0,0,44,240,1,0,
        0,0,46,242,1,0,0,0,48,258,1,0,0,0,50,270,1,0,0,0,52,272,1,0,0,0,
        54,279,1,0,0,0,56,287,1,0,0,0,58,300,1,0,0,0,60,62,3,2,1,0,61,60,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,69,3,6,3,0,69,70,5,43,
        0,0,70,89,1,0,0,0,71,72,3,28,14,0,72,73,5,43,0,0,73,89,1,0,0,0,74,
        75,3,20,10,0,75,76,5,43,0,0,76,89,1,0,0,0,77,78,3,22,11,0,78,79,
        5,43,0,0,79,89,1,0,0,0,80,89,3,10,5,0,81,89,3,12,6,0,82,89,3,14,
        7,0,83,89,3,24,12,0,84,89,3,16,8,0,85,89,3,18,9,0,86,89,3,8,4,0,
        87,89,3,4,2,0,88,68,1,0,0,0,88,71,1,0,0,0,88,74,1,0,0,0,88,77,1,
        0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,82,1,0,0,0,88,83,1,0,0,0,88,
        84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,3,1,0,0,
        0,90,94,5,40,0,0,91,93,3,2,1,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,41,0,0,
        98,5,1,0,0,0,99,100,5,59,0,0,100,101,5,44,0,0,101,102,3,28,14,0,
        102,7,1,0,0,0,103,105,5,9,0,0,104,106,3,28,14,0,105,104,1,0,0,0,
        105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,43,0,0,108,9,1,0,0,0,109,
        110,5,1,0,0,110,111,5,36,0,0,111,112,3,28,14,0,112,113,5,37,0,0,
        113,122,3,4,2,0,114,115,5,3,0,0,115,116,5,36,0,0,116,117,3,28,14,
        0,117,118,5,37,0,0,118,119,3,4,2,0,119,121,1,0,0,0,120,114,1,0,0,
        0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,127,1,0,0,
        0,124,122,1,0,0,0,125,126,5,2,0,0,126,128,3,4,2,0,127,125,1,0,0,
        0,127,128,1,0,0,0,128,11,1,0,0,0,129,130,5,4,0,0,130,131,5,36,0,
        0,131,132,3,28,14,0,132,133,5,37,0,0,133,134,3,4,2,0,134,13,1,0,
        0,0,135,136,5,5,0,0,136,137,5,36,0,0,137,138,3,6,3,0,138,139,5,43,
        0,0,139,140,3,28,14,0,140,141,5,43,0,0,141,142,3,6,3,0,142,143,5,
        37,0,0,143,144,3,4,2,0,144,15,1,0,0,0,145,146,5,10,0,0,146,147,5,
        43,0,0,147,17,1,0,0,0,148,149,5,11,0,0,149,150,5,43,0,0,150,19,1,
        0,0,0,151,152,5,12,0,0,152,153,5,36,0,0,153,154,3,28,14,0,154,155,
        5,37,0,0,155,21,1,0,0,0,156,157,5,15,0,0,157,159,5,36,0,0,158,160,
        3,54,27,0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,
        5,37,0,0,162,23,1,0,0,0,163,164,5,8,0,0,164,165,5,59,0,0,165,167,
        5,36,0,0,166,168,3,26,13,0,167,166,1,0,0,0,167,168,1,0,0,0,168,169,
        1,0,0,0,169,170,5,37,0,0,170,171,3,4,2,0,171,25,1,0,0,0,172,177,
        5,59,0,0,173,174,5,42,0,0,174,176,5,59,0,0,175,173,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,27,1,0,0,0,179,177,1,
        0,0,0,180,181,3,30,15,0,181,29,1,0,0,0,182,187,3,32,16,0,183,184,
        5,34,0,0,184,186,3,32,16,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,31,1,0,0,0,189,187,1,0,0,0,190,195,3,
        34,17,0,191,192,5,33,0,0,192,194,3,34,17,0,193,191,1,0,0,0,194,197,
        1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,33,1,0,0,0,197,195,1,
        0,0,0,198,203,3,36,18,0,199,200,7,0,0,0,200,202,3,36,18,0,201,199,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,35,1,
        0,0,0,205,203,1,0,0,0,206,211,3,38,19,0,207,208,7,1,0,0,208,210,
        3,38,19,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,37,1,0,0,0,213,211,1,0,0,0,214,219,3,40,20,0,215,216,
        7,2,0,0,216,218,3,40,20,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,
        1,0,0,0,219,220,1,0,0,0,220,39,1,0,0,0,221,219,1,0,0,0,222,227,3,
        42,21,0,223,224,7,3,0,0,224,226,3,42,21,0,225,223,1,0,0,0,226,229,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,41,1,0,0,0,229,227,1,
        0,0,0,230,233,3,44,22,0,231,232,5,56,0,0,232,234,3,42,21,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,43,1,0,0,0,235,236,5,52,0,0,236,241,
        3,44,22,0,237,238,5,35,0,0,238,241,3,44,22,0,239,241,3,46,23,0,240,
        235,1,0,0,0,240,237,1,0,0,0,240,239,1,0,0,0,241,45,1,0,0,0,242,246,
        3,50,25,0,243,245,3,48,24,0,244,243,1,0,0,0,245,248,1,0,0,0,246,
        244,1,0,0,0,246,247,1,0,0,0,247,47,1,0,0,0,248,246,1,0,0,0,249,251,
        5,36,0,0,250,252,3,54,27,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,
        1,0,0,0,253,259,5,37,0,0,254,255,5,38,0,0,255,256,3,28,14,0,256,
        257,5,39,0,0,257,259,1,0,0,0,258,249,1,0,0,0,258,254,1,0,0,0,259,
        49,1,0,0,0,260,261,5,36,0,0,261,262,3,28,14,0,262,263,5,37,0,0,263,
        271,1,0,0,0,264,271,3,52,26,0,265,271,3,58,29,0,266,271,3,56,28,
        0,267,271,5,57,0,0,268,271,5,58,0,0,269,271,5,59,0,0,270,260,1,0,
        0,0,270,264,1,0,0,0,270,265,1,0,0,0,270,266,1,0,0,0,270,267,1,0,
        0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,51,1,0,0,0,272,273,7,4,0,
        0,273,275,5,36,0,0,274,276,3,54,27,0,275,274,1,0,0,0,275,276,1,0,
        0,0,276,277,1,0,0,0,277,278,5,37,0,0,278,53,1,0,0,0,279,284,3,28,
        14,0,280,281,5,42,0,0,281,283,3,28,14,0,282,280,1,0,0,0,283,286,
        1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,55,1,0,0,0,286,284,1,
        0,0,0,287,296,5,38,0,0,288,293,3,28,14,0,289,290,5,42,0,0,290,292,
        3,28,14,0,291,289,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,
        1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,296,288,1,0,0,0,296,297,
        1,0,0,0,297,298,1,0,0,0,298,299,5,39,0,0,299,57,1,0,0,0,300,309,
        5,38,0,0,301,306,3,56,28,0,302,303,5,42,0,0,303,305,3,56,28,0,304,
        302,1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,
        310,1,0,0,0,308,306,1,0,0,0,309,301,1,0,0,0,309,310,1,0,0,0,310,
        311,1,0,0,0,311,312,5,39,0,0,312,59,1,0,0,0,27,63,88,94,105,122,
        127,159,167,177,187,195,203,211,219,227,233,240,246,251,258,270,
        275,284,293,296,306,309
    ]

class BIO_Grammar ( Parser ):

    grammarFileName = "BIO_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'si'", "'sino'", "'sino_si'", "'mientras'", 
                     "'para'", "'en'", "'rango'", "'funcion'", "'retornar'", 
                     "'break'", "'continue'", "'imprimir'", "'cargar'", 
                     "'guardar'", "'graficar'", "'sen'", "'cos'", "'tan'", 
                     "'asin'", "'acos'", "'atan'", "'potencia'", "'raiz'", 
                     "'mmult'", "'inversa'", "'transpuesta'", "'regresion_lineal'", 
                     "'crear_red'", "'entrenar'", "'clasificar'", "'agrupar'", 
                     "'predecir'", "'&&'", "'||'", "'!'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "';'", "'='", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'" ]

    symbolicNames = [ "<INVALID>", "SI", "SINO", "SINO_SI", "MIENTRAS", 
                      "PARA", "EN", "RANGO", "FUNCION", "RETORNAR", "BREAK", 
                      "CONTINUE", "IMPRIMIR", "CARGAR", "GUARDAR", "GRAFICAR", 
                      "SEN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "POTENCIA", 
                      "RAIZ", "MMULT", "INVERSA", "TRANSPUESTA", "REGRESION_LINEAL", 
                      "CREAR_RED", "ENTRENAR", "CLASIFICAR", "AGRUPAR", 
                      "PREDECIR", "AND", "OR", "NOT", "PAR_OPEN", "PAR_CLOSE", 
                      "COR_OPEN", "COR_CLOSE", "LLAVE_OPEN", "LLAVE_CLOSE", 
                      "COMA", "PUNTOYCOMA", "IGUAL", "EQ", "NEQ", "GT", 
                      "LT", "GTEQ", "LTEQ", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "POWER", "NUMERO", "STRING", "ID", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_bloque = 2
    RULE_asignacion = 3
    RULE_retornarStmt = 4
    RULE_siStmt = 5
    RULE_mientrasStmt = 6
    RULE_paraStmt = 7
    RULE_breakStmt = 8
    RULE_continueStmt = 9
    RULE_imprimirStmt = 10
    RULE_graficarStmt = 11
    RULE_funcionDef = 12
    RULE_params = 13
    RULE_expr = 14
    RULE_logical_or = 15
    RULE_logical_and = 16
    RULE_equality = 17
    RULE_comparison = 18
    RULE_addition = 19
    RULE_multiplication = 20
    RULE_exponent = 21
    RULE_unary = 22
    RULE_primary = 23
    RULE_postfix = 24
    RULE_atom = 25
    RULE_funcionNativa = 26
    RULE_argumentos = 27
    RULE_lista = 28
    RULE_matriz = 29

    ruleNames =  [ "program", "stmt", "bloque", "asignacion", "retornarStmt", 
                   "siStmt", "mientrasStmt", "paraStmt", "breakStmt", "continueStmt", 
                   "imprimirStmt", "graficarStmt", "funcionDef", "params", 
                   "expr", "logical_or", "logical_and", "equality", "comparison", 
                   "addition", "multiplication", "exponent", "unary", "primary", 
                   "postfix", "atom", "funcionNativa", "argumentos", "lista", 
                   "matriz" ]

    EOF = Token.EOF
    SI=1
    SINO=2
    SINO_SI=3
    MIENTRAS=4
    PARA=5
    EN=6
    RANGO=7
    FUNCION=8
    RETORNAR=9
    BREAK=10
    CONTINUE=11
    IMPRIMIR=12
    CARGAR=13
    GUARDAR=14
    GRAFICAR=15
    SEN=16
    COS=17
    TAN=18
    ASIN=19
    ACOS=20
    ATAN=21
    POTENCIA=22
    RAIZ=23
    MMULT=24
    INVERSA=25
    TRANSPUESTA=26
    REGRESION_LINEAL=27
    CREAR_RED=28
    ENTRENAR=29
    CLASIFICAR=30
    AGRUPAR=31
    PREDECIR=32
    AND=33
    OR=34
    NOT=35
    PAR_OPEN=36
    PAR_CLOSE=37
    COR_OPEN=38
    COR_CLOSE=39
    LLAVE_OPEN=40
    LLAVE_CLOSE=41
    COMA=42
    PUNTOYCOMA=43
    IGUAL=44
    EQ=45
    NEQ=46
    GT=47
    LT=48
    GTEQ=49
    LTEQ=50
    PLUS=51
    MINUS=52
    MUL=53
    DIV=54
    MOD=55
    POWER=56
    NUMERO=57
    STRING=58
    ID=59
    COMMENT=60
    WS=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BIO_Grammar.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.StmtContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.StmtContext,i)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BIO_Grammar.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013311402217045810) != 0):
                self.state = 60
                self.stmt()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(BIO_Grammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(BIO_Grammar.AsignacionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(BIO_Grammar.PUNTOYCOMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def imprimirStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.ImprimirStmtContext,0)


        def graficarStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.GraficarStmtContext,0)


        def siStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.SiStmtContext,0)


        def mientrasStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.MientrasStmtContext,0)


        def paraStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.ParaStmtContext,0)


        def funcionDef(self):
            return self.getTypedRuleContext(BIO_Grammar.FuncionDefContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.ContinueStmtContext,0)


        def retornarStmt(self):
            return self.getTypedRuleContext(BIO_Grammar.RetornarStmtContext,0)


        def bloque(self):
            return self.getTypedRuleContext(BIO_Grammar.BloqueContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BIO_Grammar.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.asignacion()
                self.state = 69
                self.match(BIO_Grammar.PUNTOYCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.expr()
                self.state = 72
                self.match(BIO_Grammar.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.imprimirStmt()
                self.state = 75
                self.match(BIO_Grammar.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.graficarStmt()
                self.state = 78
                self.match(BIO_Grammar.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.siStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.mientrasStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.paraStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.funcionDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.breakStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.continueStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.retornarStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 87
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_OPEN(self):
            return self.getToken(BIO_Grammar.LLAVE_OPEN, 0)

        def LLAVE_CLOSE(self):
            return self.getToken(BIO_Grammar.LLAVE_CLOSE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.StmtContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.StmtContext,i)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = BIO_Grammar.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BIO_Grammar.LLAVE_OPEN)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013311402217045810) != 0):
                self.state = 91
                self.stmt()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(BIO_Grammar.LLAVE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BIO_Grammar.ID, 0)

        def IGUAL(self):
            return self.getToken(BIO_Grammar.IGUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = BIO_Grammar.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(BIO_Grammar.ID)
            self.state = 100
            self.match(BIO_Grammar.IGUAL)
            self.state = 101
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornarStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(BIO_Grammar.RETORNAR, 0)

        def PUNTOYCOMA(self):
            return self.getToken(BIO_Grammar.PUNTOYCOMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_retornarStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornarStmt" ):
                listener.enterRetornarStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornarStmt" ):
                listener.exitRetornarStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetornarStmt" ):
                return visitor.visitRetornarStmt(self)
            else:
                return visitor.visitChildren(self)




    def retornarStmt(self):

        localctx = BIO_Grammar.RetornarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_retornarStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BIO_Grammar.RETORNAR)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013310302705410048) != 0):
                self.state = 104
                self.expr()


            self.state = 107
            self.match(BIO_Grammar.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(BIO_Grammar.SI, 0)

        def PAR_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.PAR_OPEN)
            else:
                return self.getToken(BIO_Grammar.PAR_OPEN, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ExprContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ExprContext,i)


        def PAR_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.PAR_CLOSE)
            else:
                return self.getToken(BIO_Grammar.PAR_CLOSE, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.BloqueContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.BloqueContext,i)


        def SINO_SI(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.SINO_SI)
            else:
                return self.getToken(BIO_Grammar.SINO_SI, i)

        def SINO(self):
            return self.getToken(BIO_Grammar.SINO, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_siStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSiStmt" ):
                listener.enterSiStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSiStmt" ):
                listener.exitSiStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSiStmt" ):
                return visitor.visitSiStmt(self)
            else:
                return visitor.visitChildren(self)




    def siStmt(self):

        localctx = BIO_Grammar.SiStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_siStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BIO_Grammar.SI)
            self.state = 110
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 111
            self.expr()
            self.state = 112
            self.match(BIO_Grammar.PAR_CLOSE)
            self.state = 113
            self.bloque()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 114
                self.match(BIO_Grammar.SINO_SI)
                self.state = 115
                self.match(BIO_Grammar.PAR_OPEN)
                self.state = 116
                self.expr()
                self.state = 117
                self.match(BIO_Grammar.PAR_CLOSE)
                self.state = 118
                self.bloque()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 125
                self.match(BIO_Grammar.SINO)
                self.state = 126
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(BIO_Grammar.MIENTRAS, 0)

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(BIO_Grammar.BloqueContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_mientrasStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientrasStmt" ):
                listener.enterMientrasStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientrasStmt" ):
                listener.exitMientrasStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientrasStmt" ):
                return visitor.visitMientrasStmt(self)
            else:
                return visitor.visitChildren(self)




    def mientrasStmt(self):

        localctx = BIO_Grammar.MientrasStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mientrasStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BIO_Grammar.MIENTRAS)
            self.state = 130
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 131
            self.expr()
            self.state = 132
            self.match(BIO_Grammar.PAR_CLOSE)
            self.state = 133
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(BIO_Grammar.PARA, 0)

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.AsignacionContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.AsignacionContext,i)


        def PUNTOYCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.PUNTOYCOMA)
            else:
                return self.getToken(BIO_Grammar.PUNTOYCOMA, i)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(BIO_Grammar.BloqueContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_paraStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParaStmt" ):
                listener.enterParaStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParaStmt" ):
                listener.exitParaStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaStmt" ):
                return visitor.visitParaStmt(self)
            else:
                return visitor.visitChildren(self)




    def paraStmt(self):

        localctx = BIO_Grammar.ParaStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paraStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(BIO_Grammar.PARA)
            self.state = 136
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 137
            self.asignacion()
            self.state = 138
            self.match(BIO_Grammar.PUNTOYCOMA)
            self.state = 139
            self.expr()
            self.state = 140
            self.match(BIO_Grammar.PUNTOYCOMA)
            self.state = 141
            self.asignacion()
            self.state = 142
            self.match(BIO_Grammar.PAR_CLOSE)
            self.state = 143
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BIO_Grammar.BREAK, 0)

        def PUNTOYCOMA(self):
            return self.getToken(BIO_Grammar.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BIO_Grammar.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BIO_Grammar.BREAK)
            self.state = 146
            self.match(BIO_Grammar.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BIO_Grammar.CONTINUE, 0)

        def PUNTOYCOMA(self):
            return self.getToken(BIO_Grammar.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BIO_Grammar.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(BIO_Grammar.CONTINUE)
            self.state = 149
            self.match(BIO_Grammar.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(BIO_Grammar.IMPRIMIR, 0)

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_imprimirStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimirStmt" ):
                listener.enterImprimirStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimirStmt" ):
                listener.exitImprimirStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimirStmt" ):
                return visitor.visitImprimirStmt(self)
            else:
                return visitor.visitChildren(self)




    def imprimirStmt(self):

        localctx = BIO_Grammar.ImprimirStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_imprimirStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(BIO_Grammar.IMPRIMIR)
            self.state = 152
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 153
            self.expr()
            self.state = 154
            self.match(BIO_Grammar.PAR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraficarStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAFICAR(self):
            return self.getToken(BIO_Grammar.GRAFICAR, 0)

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def argumentos(self):
            return self.getTypedRuleContext(BIO_Grammar.ArgumentosContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_graficarStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficarStmt" ):
                listener.enterGraficarStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficarStmt" ):
                listener.exitGraficarStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficarStmt" ):
                return visitor.visitGraficarStmt(self)
            else:
                return visitor.visitChildren(self)




    def graficarStmt(self):

        localctx = BIO_Grammar.GraficarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_graficarStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BIO_Grammar.GRAFICAR)
            self.state = 157
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013310302705410048) != 0):
                self.state = 158
                self.argumentos()


            self.state = 161
            self.match(BIO_Grammar.PAR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(BIO_Grammar.FUNCION, 0)

        def ID(self):
            return self.getToken(BIO_Grammar.ID, 0)

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(BIO_Grammar.BloqueContext,0)


        def params(self):
            return self.getTypedRuleContext(BIO_Grammar.ParamsContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_funcionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionDef" ):
                listener.enterFuncionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionDef" ):
                listener.exitFuncionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionDef" ):
                return visitor.visitFuncionDef(self)
            else:
                return visitor.visitChildren(self)




    def funcionDef(self):

        localctx = BIO_Grammar.FuncionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(BIO_Grammar.FUNCION)
            self.state = 164
            self.match(BIO_Grammar.ID)
            self.state = 165
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 166
                self.params()


            self.state = 169
            self.match(BIO_Grammar.PAR_CLOSE)
            self.state = 170
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.ID)
            else:
                return self.getToken(BIO_Grammar.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.COMA)
            else:
                return self.getToken(BIO_Grammar.COMA, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BIO_Grammar.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BIO_Grammar.ID)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 173
                self.match(BIO_Grammar.COMA)
                self.state = 174
                self.match(BIO_Grammar.ID)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_or(self):
            return self.getTypedRuleContext(BIO_Grammar.Logical_orContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BIO_Grammar.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.logical_or()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.Logical_andContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.Logical_andContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.OR)
            else:
                return self.getToken(BIO_Grammar.OR, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_logical_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_or" ):
                listener.enterLogical_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_or" ):
                listener.exitLogical_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_or" ):
                return visitor.visitLogical_or(self)
            else:
                return visitor.visitChildren(self)




    def logical_or(self):

        localctx = BIO_Grammar.Logical_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logical_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.logical_and()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 183
                self.match(BIO_Grammar.OR)
                self.state = 184
                self.logical_and()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.EqualityContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.AND)
            else:
                return self.getToken(BIO_Grammar.AND, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_logical_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_and" ):
                listener.enterLogical_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_and" ):
                listener.exitLogical_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and" ):
                return visitor.visitLogical_and(self)
            else:
                return visitor.visitChildren(self)




    def logical_and(self):

        localctx = BIO_Grammar.Logical_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logical_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.equality()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 191
                self.match(BIO_Grammar.AND)
                self.state = 192
                self.equality()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ComparisonContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ComparisonContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.EQ)
            else:
                return self.getToken(BIO_Grammar.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.NEQ)
            else:
                return self.getToken(BIO_Grammar.NEQ, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = BIO_Grammar.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.comparison()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45 or _la==46:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.comparison()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.AdditionContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.AdditionContext,i)


        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.GT)
            else:
                return self.getToken(BIO_Grammar.GT, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.LT)
            else:
                return self.getToken(BIO_Grammar.LT, i)

        def GTEQ(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.GTEQ)
            else:
                return self.getToken(BIO_Grammar.GTEQ, i)

        def LTEQ(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.LTEQ)
            else:
                return self.getToken(BIO_Grammar.LTEQ, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = BIO_Grammar.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.addition()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2111062325329920) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2111062325329920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.addition()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.MultiplicationContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.MultiplicationContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.PLUS)
            else:
                return self.getToken(BIO_Grammar.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.MINUS)
            else:
                return self.getToken(BIO_Grammar.MINUS, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)




    def addition(self):

        localctx = BIO_Grammar.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.multiplication()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51 or _la==52:
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==51 or _la==52):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self.multiplication()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ExponentContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ExponentContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.MUL)
            else:
                return self.getToken(BIO_Grammar.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.DIV)
            else:
                return self.getToken(BIO_Grammar.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.MOD)
            else:
                return self.getToken(BIO_Grammar.MOD, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_multiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)




    def multiplication(self):

        localctx = BIO_Grammar.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.exponent()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 63050394783186944) != 0):
                self.state = 223
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63050394783186944) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.exponent()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(BIO_Grammar.UnaryContext,0)


        def POWER(self):
            return self.getToken(BIO_Grammar.POWER, 0)

        def exponent(self):
            return self.getTypedRuleContext(BIO_Grammar.ExponentContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = BIO_Grammar.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.unary()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 231
                self.match(BIO_Grammar.POWER)
                self.state = 232
                self.exponent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(BIO_Grammar.MINUS, 0)

        def unary(self):
            return self.getTypedRuleContext(BIO_Grammar.UnaryContext,0)


        def NOT(self):
            return self.getToken(BIO_Grammar.NOT, 0)

        def primary(self):
            return self.getTypedRuleContext(BIO_Grammar.PrimaryContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = BIO_Grammar.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_unary)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(BIO_Grammar.MINUS)
                self.state = 236
                self.unary()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(BIO_Grammar.NOT)
                self.state = 238
                self.unary()
                pass
            elif token in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 36, 38, 57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BIO_Grammar.AtomContext,0)


        def postfix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.PostfixContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.PostfixContext,i)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = BIO_Grammar.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.atom()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36 or _la==38:
                self.state = 243
                self.postfix()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def argumentos(self):
            return self.getTypedRuleContext(BIO_Grammar.ArgumentosContext,0)


        def COR_OPEN(self):
            return self.getToken(BIO_Grammar.COR_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def COR_CLOSE(self):
            return self.getToken(BIO_Grammar.COR_CLOSE, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)




    def postfix(self):

        localctx = BIO_Grammar.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(BIO_Grammar.PAR_OPEN)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013310302705410048) != 0):
                    self.state = 250
                    self.argumentos()


                self.state = 253
                self.match(BIO_Grammar.PAR_CLOSE)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(BIO_Grammar.COR_OPEN)
                self.state = 255
                self.expr()
                self.state = 256
                self.match(BIO_Grammar.COR_CLOSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(BIO_Grammar.ExprContext,0)


        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def funcionNativa(self):
            return self.getTypedRuleContext(BIO_Grammar.FuncionNativaContext,0)


        def matriz(self):
            return self.getTypedRuleContext(BIO_Grammar.MatrizContext,0)


        def lista(self):
            return self.getTypedRuleContext(BIO_Grammar.ListaContext,0)


        def NUMERO(self):
            return self.getToken(BIO_Grammar.NUMERO, 0)

        def STRING(self):
            return self.getToken(BIO_Grammar.STRING, 0)

        def ID(self):
            return self.getToken(BIO_Grammar.ID, 0)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BIO_Grammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atom)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(BIO_Grammar.PAR_OPEN)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(BIO_Grammar.PAR_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.funcionNativa()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.matriz()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.lista()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(BIO_Grammar.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.match(BIO_Grammar.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.match(BIO_Grammar.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionNativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_OPEN(self):
            return self.getToken(BIO_Grammar.PAR_OPEN, 0)

        def PAR_CLOSE(self):
            return self.getToken(BIO_Grammar.PAR_CLOSE, 0)

        def SEN(self):
            return self.getToken(BIO_Grammar.SEN, 0)

        def COS(self):
            return self.getToken(BIO_Grammar.COS, 0)

        def TAN(self):
            return self.getToken(BIO_Grammar.TAN, 0)

        def ASIN(self):
            return self.getToken(BIO_Grammar.ASIN, 0)

        def ACOS(self):
            return self.getToken(BIO_Grammar.ACOS, 0)

        def ATAN(self):
            return self.getToken(BIO_Grammar.ATAN, 0)

        def POTENCIA(self):
            return self.getToken(BIO_Grammar.POTENCIA, 0)

        def RAIZ(self):
            return self.getToken(BIO_Grammar.RAIZ, 0)

        def MMULT(self):
            return self.getToken(BIO_Grammar.MMULT, 0)

        def INVERSA(self):
            return self.getToken(BIO_Grammar.INVERSA, 0)

        def TRANSPUESTA(self):
            return self.getToken(BIO_Grammar.TRANSPUESTA, 0)

        def REGRESION_LINEAL(self):
            return self.getToken(BIO_Grammar.REGRESION_LINEAL, 0)

        def CREAR_RED(self):
            return self.getToken(BIO_Grammar.CREAR_RED, 0)

        def ENTRENAR(self):
            return self.getToken(BIO_Grammar.ENTRENAR, 0)

        def CLASIFICAR(self):
            return self.getToken(BIO_Grammar.CLASIFICAR, 0)

        def AGRUPAR(self):
            return self.getToken(BIO_Grammar.AGRUPAR, 0)

        def PREDECIR(self):
            return self.getToken(BIO_Grammar.PREDECIR, 0)

        def GRAFICAR(self):
            return self.getToken(BIO_Grammar.GRAFICAR, 0)

        def CARGAR(self):
            return self.getToken(BIO_Grammar.CARGAR, 0)

        def GUARDAR(self):
            return self.getToken(BIO_Grammar.GUARDAR, 0)

        def argumentos(self):
            return self.getTypedRuleContext(BIO_Grammar.ArgumentosContext,0)


        def getRuleIndex(self):
            return BIO_Grammar.RULE_funcionNativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionNativa" ):
                listener.enterFuncionNativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionNativa" ):
                listener.exitFuncionNativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionNativa" ):
                return visitor.visitFuncionNativa(self)
            else:
                return visitor.visitChildren(self)




    def funcionNativa(self):

        localctx = BIO_Grammar.FuncionNativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funcionNativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8589926400) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 273
            self.match(BIO_Grammar.PAR_OPEN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013310302705410048) != 0):
                self.state = 274
                self.argumentos()


            self.state = 277
            self.match(BIO_Grammar.PAR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ExprContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.COMA)
            else:
                return self.getToken(BIO_Grammar.COMA, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = BIO_Grammar.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.expr()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 280
                self.match(BIO_Grammar.COMA)
                self.state = 281
                self.expr()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COR_OPEN(self):
            return self.getToken(BIO_Grammar.COR_OPEN, 0)

        def COR_CLOSE(self):
            return self.getToken(BIO_Grammar.COR_CLOSE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ExprContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.COMA)
            else:
                return self.getToken(BIO_Grammar.COMA, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = BIO_Grammar.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(BIO_Grammar.COR_OPEN)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1013310302705410048) != 0):
                self.state = 288
                self.expr()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 289
                    self.match(BIO_Grammar.COMA)
                    self.state = 290
                    self.expr()
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 298
            self.match(BIO_Grammar.COR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COR_OPEN(self):
            return self.getToken(BIO_Grammar.COR_OPEN, 0)

        def COR_CLOSE(self):
            return self.getToken(BIO_Grammar.COR_CLOSE, 0)

        def lista(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BIO_Grammar.ListaContext)
            else:
                return self.getTypedRuleContext(BIO_Grammar.ListaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BIO_Grammar.COMA)
            else:
                return self.getToken(BIO_Grammar.COMA, i)

        def getRuleIndex(self):
            return BIO_Grammar.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = BIO_Grammar.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BIO_Grammar.COR_OPEN)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 301
                self.lista()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 302
                    self.match(BIO_Grammar.COMA)
                    self.state = 303
                    self.lista()
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 311
            self.match(BIO_Grammar.COR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





