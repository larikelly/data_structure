# Exercício 9:
# Converter expressão aritmética em forma prefixada para formas infixa e pós-fixada equivalentes.

class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            raise Exception("Pilha vazia!")
        return self.data.pop()

    def top(self):
        if not self.data:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

def infix_to_postfix(expr):
    prec = {
        '+': 1, '-': 1,
        '*': 2, '/': 2
    }

    output = []
    op_stack = Stack()

    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()

    for token in tokens:
        if token.isdigit(): 
            output.append(token)

        elif token in prec:  
            while (not op_stack.is_empty() and
                   op_stack.top() in prec and
                   prec[op_stack.top()] >= prec[token]):
                output.append(op_stack.pop())
            op_stack.push(token)

        elif token == '(':
            op_stack.push(token)

        elif token == ')':
            while op_stack.top() != '(':
                output.append(op_stack.pop())
            op_stack.pop()  

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output


def eval_postfix(post):
    stack = Stack()

    for token in post:
        if token.isdigit():
            stack.push(int(token))
        else:  # operador
            b = stack.pop()
            a = stack.pop()

            if token == '+': stack.push(a + b)
            elif token == '-': stack.push(a - b)
            elif token == '*': stack.push(a * b)
            elif token == '/': stack.push(a // b) 

    return stack.pop()


def calcular(expr):
    postfix = infix_to_postfix(expr)
    resultado = eval_postfix(postfix)
    return resultado

if __name__ == "__main__":
    expr = "3 + 5 * ( 2 - 8 )"
    print("Expressão:", expr)
    print("Resultado:", calcular(expr))
