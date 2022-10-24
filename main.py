#fazendo os importes das funcoes feitas para os movimentos e das bibliotecas Turtle e Screen
from turtleMovements import * 
from turtle import Turtle, Screen

#instancia dois objetos do tipo Turtle e outro do tipo Screen
tartaruga = Turtle()
tela = Screen()

#faz a tartaruga se mover para frente
def moveForward():
    tartaruga.forward(40)

#faz a tartaruga se mover para tras
def backwards():
    tartaruga.backward(40)

#faz a tartaruga girar no sentido horario
def clockWise():
    tartaruga.right(15)

#faz a tartaruga girar no sentido antihorario
def antiClockWise():
    tartaruga.left(15)

#limpa a tela e volta a tartaruga para o centro
def clearDrawing():
    tartaruga.reset()
    tartaruga.clear()      


#faz com que a tela comece a receber inputs (listen)
tela.listen()

#configura para que quando o usuario pressionar 'W' ele ative a funcao de andar para frente
tela.onkey(key='w',fun=moveForward)
tela.onkey(key='s',fun=backwards)
tela.onkey(key='a',fun=antiClockWise)
tela.onkey(key='d',fun=clockWise)
tela.onkey(key='c',fun=clearDrawing)

#a tela só vai sair no clique
tela.exitonclick()




