parser grammar BIO_Grammar;

options { tokenVocab=BIO_Lexer; }

// =========================================
// PROGRAMA
// =========================================

program
    : stmt* EOF
    ;

stmt
    : asignacion PUNTOYCOMA
    | expr PUNTOYCOMA
    | imprimirStmt PUNTOYCOMA
    | graficarStmt PUNTOYCOMA
    | siStmt
    | mientrasStmt
    | paraStmt
    | funcionDef
    | breakStmt
    | continueStmt
    | retornarStmt               // <<< NUEVO
    | bloque
    ;

bloque
    : LLAVE_OPEN stmt* LLAVE_CLOSE
    ;

// =========================================
// ASIGNACIÓN
// =========================================

asignacion
    : ID IGUAL expr
    ;

// =========================================
// RETURN
// =========================================

retornarStmt
    : RETORNAR expr? PUNTOYCOMA
    ;

// =========================================
// IF / ELSE / ELSE IF
// =========================================

siStmt
    : SI PAR_OPEN expr PAR_CLOSE bloque
      (SINO_SI PAR_OPEN expr PAR_CLOSE bloque)*
      (SINO bloque)?
    ;

// =========================================
// MIENTRAS
// =========================================

mientrasStmt
    : MIENTRAS PAR_OPEN expr PAR_CLOSE bloque
    ;

// =========================================
// FOR
// =========================================

paraStmt
    : PARA PAR_OPEN asignacion PUNTOYCOMA expr PUNTOYCOMA asignacion PAR_CLOSE bloque
    ;

// =========================================
// BREAK / CONTINUE
// =========================================

breakStmt
    : BREAK PUNTOYCOMA
    ;

continueStmt
    : CONTINUE PUNTOYCOMA
    ;

// =========================================
// IMPRIMIR
// =========================================

imprimirStmt
    : IMPRIMIR PAR_OPEN expr PAR_CLOSE
    ;

// =========================================
// GRAFICAR
// =========================================

graficarStmt
    : GRAFICAR PAR_OPEN argumentos? PAR_CLOSE
    ;

// =========================================
// FUNCIONES DEFINIDAS POR EL USUARIO
// =========================================

funcionDef
    : FUNCION ID PAR_OPEN params? PAR_CLOSE bloque
    ;

params
    : ID (COMA ID)*
    ;

// =========================================
// EXPRESIONES (PRECEDENCIA COMPLETA)
// =========================================

expr
    : logical_or
    ;

logical_or
    : logical_and (OR logical_and)*
    ;

logical_and
    : equality (AND equality)*
    ;

equality
    : comparison ((EQ | NEQ) comparison)*
    ;

comparison
    : addition ((GT | LT | GTEQ | LTEQ) addition)*
    ;

addition
    : multiplication ((PLUS | MINUS) multiplication)*
    ;

multiplication
    : exponent ((MUL | DIV | MOD) exponent)*
    ;

exponent
    : unary (POWER exponent)?
    ;

unary
    : MINUS unary
    | NOT unary
    | primary
    ;

// =========================================
// PRIMARY ROBUSTO (POSTFIX: llamadas y accesos)
// =========================================

primary
    : atom postfix*
    ;

postfix
    : PAR_OPEN argumentos? PAR_CLOSE
    | COR_OPEN expr COR_CLOSE
    ;

atom
    : PAR_OPEN expr PAR_CLOSE
    | funcionNativa
    | matriz
    | lista
    | NUMERO
    | STRING
    | ID
    ;

// =========================================
// FUNCIONES NATIVAS
// =========================================

funcionNativa
    : (SEN | COS | TAN | ASIN | ACOS | ATAN
      | POTENCIA | RAIZ
      | MMULT | INVERSA | TRANSPUESTA
      | REGRESION_LINEAL | CREAR_RED | ENTRENAR
      | CLASIFICAR | AGRUPAR | PREDECIR
      | GRAFICAR
      | CARGAR | GUARDAR
      )
      PAR_OPEN argumentos? PAR_CLOSE
    ;

argumentos
    : expr (COMA expr)*
    ;

// =========================================
// LISTAS Y MATRICES
// =========================================

lista
    : COR_OPEN (expr (COMA expr)*)? COR_CLOSE
    ;

matriz
    : COR_OPEN (lista (COMA lista)*)? COR_CLOSE
    ;
