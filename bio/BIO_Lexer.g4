lexer grammar BIO_Lexer;

// Palabras reservadas
SI          : 'si';
SINO        : 'sino';
SINO_SI     : 'sino_si';
MIENTRAS    : 'mientras';
PARA        : 'para';
EN          : 'en';
RANGO       : 'rango';
FUNCION     : 'funcion';
RETORNAR    : 'retornar';
BREAK       : 'break';
CONTINUE    : 'continue';

// Funciones internas
IMPRIMIR    : 'imprimir';
CARGAR      : 'cargar';
GUARDAR     : 'guardar';
GRAFICAR    : 'graficar';

// Matemáticas
SEN         : 'sen';
COS         : 'cos';
TAN         : 'tan';
ASIN        : 'asin';
ACOS        : 'acos';
ATAN        : 'atan';
POTENCIA    : 'potencia';
RAIZ        : 'raiz';

// Matrices
MMULT       : 'mmult';
INVERSA     : 'inversa';
TRANSPUESTA : 'transpuesta';

// Deep Learning
REGRESION_LINEAL : 'regresion_lineal';
CREAR_RED        : 'crear_red';
ENTRENAR         : 'entrenar';
CLASIFICAR       : 'clasificar';
AGRUPAR          : 'agrupar';
PREDECIR         : 'predecir';

// Operadores lógicos
AND         : '&&';
OR          : '||';
NOT         : '!';

// Símbolos
PAR_OPEN    : '(';
PAR_CLOSE   : ')';
COR_OPEN    : '[';
COR_CLOSE   : ']';
LLAVE_OPEN  : '{';
LLAVE_CLOSE : '}';
COMA        : ',';
PUNTOYCOMA  : ';';
IGUAL       : '=';

// Comparadores
EQ      : '==';
NEQ     : '!=';
GT      : '>';
LT      : '<';
GTEQ    : '>=';
LTEQ    : '<=';

// Aritméticos
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';
POWER   : '^';

// Literales
NUMERO  : [0-9]+ ('.' [0-9]+)?;
STRING  : '"' (~["\r\n])* '"' ;
ID      : [a-zA-Z_][a-zA-Z_0-9]*;

// Comentarios
COMMENT : '/*' .*? '*/' -> skip;

// Espacios
WS : [ \t\r\n]+ -> skip;
