# Se define la funcion para codificar la data
def codificar(data):
    # Se inicializa la variable 'resultado' donde se guardara la data codificada.
    resultado = ""

    # Se itera cada caracter de 'data' y se codifica hasta finalizar.
    for caracter in data:
        # Se definen los diferentes casos a recibir y se agrega el valor codificado a 'resultado'.
        if caracter == 'a':
            resultado += 'q'
        elif caracter == 'b':
            resultado += 'G'
        elif caracter == 'c':
            resultado += 'x'
        elif caracter == 'd':
            resultado += 'S'
        elif caracter == 'e':
            resultado += '#'
        elif caracter == 'f':
            resultado += 'r'
        elif caracter == 'g':
            resultado += 'B'
        elif caracter == 'h':
            resultado += 'y'
        elif caracter == 'i':
            resultado += '8'
        elif caracter == 'j':
            resultado += 'm'
        elif caracter == 'k':
            resultado += ','
        elif caracter == 'l':
            resultado += '>'
        elif caracter == 'm':
            resultado += '_'
        elif caracter == 'n':
            resultado += ':'
        elif caracter == 'o':
            resultado += 'l'
        elif caracter == 'p':
            resultado += ';'
        elif caracter == 'q':
            resultado += '1'
        elif caracter == 'r':
            resultado += '$'
        elif caracter == 's':
            resultado += 'W'
        elif caracter == 't':
            resultado += 'g'
        elif caracter == 'u':
            resultado += '7'
        elif caracter == 'v':
            resultado += 'f'
        elif caracter == 'w':
            resultado += '@'
        elif caracter == 'x':
            resultado += 's'
        elif caracter == 'y':
            resultado += '6'
        elif caracter == 'z':
            resultado += 'A'
        elif caracter == ' ':
            resultado += '-'
        elif caracter == '1':
            resultado += '!'
        elif caracter == '2':
            resultado += 'w'
        elif caracter == '3':
            resultado += '#'
        elif caracter == '4':
            resultado += 'R'
        elif caracter == '5':
            resultado += '€'
        elif caracter == '6':
            resultado += '^'
        elif caracter == '7':
            resultado += '&'
        elif caracter == '8':
            resultado += '*'
        elif caracter == '9':
            resultado += '('
        elif caracter == '0':
            resultado += ')'
        elif caracter == 'A':
            resultado += 'z'
        elif caracter == 'B':
            resultado += ':'
        elif caracter == 'C':
            resultado += 'D'
        elif caracter == 'D':
            resultado += 'C'
        elif caracter == 'E':
            resultado += '{'
        elif caracter == 'F':
            resultado += 'V'
        elif caracter == 'G':
            resultado += 't'
        elif caracter == 'H':
            resultado += 'n'
        elif caracter == 'I':
            resultado += 'K'
        elif caracter == 'J':
            resultado += '.'
        elif caracter == 'K':
            resultado += 'i'
        elif caracter == 'L':
            resultado += '?'
        elif caracter == 'M':
            resultado += '/'
        elif caracter == 'N':
            resultado += ' '
        elif caracter == 'O':
            resultado += 'L'
        elif caracter == 'P':
            resultado += '['
        elif caracter == 'Q':
            resultado += '}'
        elif caracter == 'R':
            resultado += 'F'
        elif caracter == 'S':
            resultado += 'X'
        elif caracter == 'T':
            resultado += ']'
        elif caracter == 'U':
            resultado += '+'
        elif caracter == 'V':
            resultado += '='
        elif caracter == 'W':
            resultado += '`'
        elif caracter == 'X':
            resultado += '|'
        elif caracter == 'Y':
            resultado += 'H'
        elif caracter == 'Z':
            resultado += 'h'
        elif caracter == 'ñ':
            resultado += '~'
        elif caracter == 'Ñ':
            resultado += 'P'

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado

def decodificar(data):
    # Se inicializa la variable 'resultado' donde se guardara la data decodificada.
    resultado = ""

    # Se itera cada caracter de 'data' y se decodifica hasta finalizar.
    for caracter in data:
        # Se definen los diferentes casos a recibir y se agrega el valor decodificado a 'resultado'.
        if caracter == 'q':
            resultado += 'a'
        elif caracter == 'G':
            resultado += 'b'
        elif caracter == 'x':
            resultado += 'c'
        elif caracter == 'S':
            resultado += 'd'
        elif caracter == '#':
            resultado += 'e'
        elif caracter == 'r':
            resultado += 'f'
        elif caracter == 'B':
            resultado += 'g'
        elif caracter == 'y':
            resultado += 'h'
        elif caracter == '8':
            resultado += 'i'
        elif caracter == 'm':
            resultado += 'j'
        elif caracter == ',':
            resultado += 'k'
        elif caracter == '>':
            resultado += 'l'
        elif caracter == '_':
            resultado += 'm'
        elif caracter == ':':
            resultado += 'n'
        elif caracter == 'l':
            resultado += 'o'
        elif caracter == ';':
            resultado += 'p'
        elif caracter == '1':
            resultado += 'q'
        elif caracter == '$':
            resultado += 'r'
        elif caracter == 'W':
            resultado += 's'
        elif caracter == 'g':
            resultado += 't'
        elif caracter == '7':
            resultado += 'u'
        elif caracter == 'f':
            resultado += 'v'
        elif caracter == '@':
            resultado += 'w'
        elif caracter == 's':
            resultado += 'x'
        elif caracter == '6':
            resultado += 'y'
        elif caracter == 'A':
            resultado += 'z'
        elif caracter == '-':
            resultado += ' '
        elif caracter == '!':
            resultado += '1'
        elif caracter == 'w':
            resultado += '2'
        elif caracter == '#':
            resultado += '3'
        elif caracter == 'R':
            resultado += '4'
        elif caracter == '€':
            resultado += '5'
        elif caracter == '^':
            resultado += '6'
        elif caracter == '&':
            resultado += '7'
        elif caracter == '*':
            resultado += '8'
        elif caracter == '(':
            resultado += '9'
        elif caracter == ')':
            resultado += '0'
        elif caracter == 'z':
            resultado += 'A'
        elif caracter == ':':
            resultado += 'B'
        elif caracter == 'D':
            resultado += 'C'
        elif caracter == 'C':
            resultado += 'D'
        elif caracter == '{':
            resultado += 'E'
        elif caracter == 'V':
            resultado += 'F'
        elif caracter == 't':
            resultado += 'G'
        elif caracter == 'n':
            resultado += 'H'
        elif caracter == 'K':
            resultado += 'I'
        elif caracter == '.':
            resultado += 'J'
        elif caracter == 'i':
            resultado += 'K'
        elif caracter == '?':
            resultado += 'L'
        elif caracter == '/':
            resultado += 'M'
        elif caracter == ' ':
            resultado += 'N'
        elif caracter == 'L':
            resultado += 'O'
        elif caracter == '[':
            resultado += 'P'
        elif caracter == '}':
            resultado += 'Q'
        elif caracter == 'F':
            resultado += 'R'
        elif caracter == 'X':
            resultado += 'S'
        elif caracter == ']':
            resultado += 'T'
        elif caracter == '+':
            resultado += 'U'
        elif caracter == '=':
            resultado += 'V'
        elif caracter == '`':
            resultado += 'W'
        elif caracter == '|':
            resultado += 'X'
        elif caracter == 'H':
            resultado += 'Y'
        elif caracter == 'h':
            resultado += 'Z'
        elif caracter == '~':
            resultado += 'ñ'
        elif caracter == 'P':
            resultado += 'Ñ'

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado
