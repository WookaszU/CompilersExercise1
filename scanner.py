
import ply.lex as lex


literals = ['+', '-', '*', '/', '(', ')','[',']','{','}','=','<','>',':',',',';']

# List of token names.   This is always required
tokens = (
   'IF',
   'ELSE',
   'FOR',
   'WHILE',
   'BREAK',
   'CONTINUE',
   'RETURN',
   'EYE',
   'ZEROS',
   'ONES',
   'PRINT',
   'ID',
   'INTNUM',
   'FLOATNUM',

   'DOTADD',
   'DOTSUB',
   'DOTMUL',
   'DOTDIV',
   'ADDASSIGN',
   'SUBASSIGN',
   'MULASSIGN',
   'DIVASSIGN',
   'LE',
   'GE',
   'NE',
   'E',
   'TRANSPOSE',
   'COMMENT'
   

)

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
}

#When building the master regular expression, rules are added in the following order:

#1 All tokens defined by functions are added in the same order as they appear in the lexer file.
#2 Tokens defined by strings are added next by sorting them in order of decreasing regular expression length
#  (longer expressions are added first).


t_DOTADD    = r'\.\+'
t_DOTSUB   = r'\.-'
t_DOTMUL   = r'\.\*'
t_DOTDIV  = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_TRANSPOSE = r'\''

t_LE = r'\<='
t_GE = r'\>='
t_NE = r'!='
t_E = r'=='


# t_IF = r'if'
# t_ELSE = r'else'
# t_FOR = r'for'
# t_WHILE = r'while'
#
# t_BREAK = r'break'
# t_CONTINUE = r'continue'
# t_RETURN = r'return'
#
# t_EYE = r'eye'
# t_ZEROS = r'zeros'
# t_ONES = r'ones'
# t_PRINT = r'print'

#ignorowaneSymbole
t_ignore = '  \t'

t_ignore_COMMENT = r'\#.*'


def t_FLOATNUM(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t





def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()
