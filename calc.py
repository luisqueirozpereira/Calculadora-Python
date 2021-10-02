#Autor: Luis Queiroz S2
def soma(x,y): #função para soma
    result=x+y
    return result
def subtrai(x,y): #função para subtração
    result=x-y
    return result
def multiplica(x,y): #função para multiplicação
    result=x*y
    return result
def divide(x,y): #função paradivisão
    result=x/y
    return result

print("Calculadora simples:)")
n1=int(input("Digite o primeiro número: "))#solicitando o primeiro valor ao user
opera=input("Selecione a operação, digite +, -, x ou / ") #solicitando a operação ao user
n2=int(input("Digite o segundo número: "))#solicitando o segundo valor ao usuário
if opera=="+": #estrutura condicional para checar a operação a ser realizada.
    print(soma(n1, n2))
elif opera =="-":
    print(subtrai(n1, n2))
elif opera=="x":
    print(multiplica(n1, n2))
elif opera=="/":
    print(divide(n1,n2))
