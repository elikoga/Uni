grammar Lang;
program: statement* EOF;
statement
    : let_statement
    | expression_statement
    | comment;
comment: Comment;
Comment
  :  '#' ~( '\r' | '\n' )*
  ;
let_statement: LET IDENTIFIER_LOWERCASE_START COLON type EQUAL expression_without_block SEMICOLON?;
expression: expression_with_block | expression_without_block;
expression_statement
    : expression_without_block SEMICOLON
    | expression_with_block SEMICOLON?;
expression_with_block
    : block_expression
    | loop_expression
    | while_expression
    | if_expression;
expression_without_block
    : literal_expression
    | variable_expression
    | function_call_expression
    | negation_expression
    | grouped_expression
    | break_expression
    | expression_without_block math_operator expression_without_block
    | expression_without_block comparison_operator expression_without_block
    | expression_without_block logical_operator expression_without_block
    | variable_expression assignment_operator expression_without_block;
block_expression: LBRACE
  ( statement+
  | statement* expression_without_block
) RBRACE;
loop_expression: LOOP block_expression;
while_expression: WHILE expression_without_block block_expression;
if_expression: IF expression block_expression (ELSE block_expression)?;
literal_expression
    : INTEGER
    | FLOAT
    | STRING
    | BOOLEAN;
variable_expression: IDENTIFIER_LOWERCASE_START;
function_call_expression: IDENTIFIER_LOWERCASE_START LPAREN (expression (COMMA expression)*)? RPAREN;
negation_expression: '!' expression | '-' expression;
grouped_expression: LPAREN expression RPAREN;
math_operator: '+' | '-' | '*' | '/' | '%' | '**';
comparison_operator: '==' | '!=' | '<' | '<=' | '>' | '>=';
logical_operator: '&&' | '||';
assignment_operator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    | '%=';

break_expression: 'break';
type: IDENTIFIER_CAPITAL_START;
INTEGER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;
STRING: '"' ~('\r' | '\n' | '"')* '"';
BOOLEAN: 'true' | 'false';
WHILE: 'while';
LET: 'let';
LOOP: 'loop';
IF: 'if';
ELSE: 'else';
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMICOLON: ';';
COMMA: ',';
COLON: ':';
WS: [ \t\n\r]+ -> skip;
EQUAL: '=';
IDENTIFIER_LOWERCASE_START: [a-z] [a-zA-Z0-9_]*;
IDENTIFIER_CAPITAL_START: [A-Z] [a-zA-Z0-9_]*;
