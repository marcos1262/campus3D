from OpenGL.GL import *

from math import sin, cos, radians

class Objeto():
    def __init__(self, obj, x=0.0, y=0.0):
        self.obj = obj
        self.x = x
        self.y = y

    def desenha(self):
        pass

    def colidiu(self, objeto):
        pass
        # d = math.sqrt((objeto.x - self.x) ** 2 + (objeto.y - self.y) ** 2)
        #
        # raio1 = min(self.largura, self.altura) / 2
        # raio2 = min(objeto.largura, objeto.altura) / 2
        #
        # if d <= raio1 + raio2:
        #     return True
        # else:
        #     return False


class Jogador(Objeto):
    def __init__(self, jogo, obj, x=0.0, y=0.0, z=0.0, angulo=0):
        Objeto.__init__(self, obj, x, y)

        self.jogo = jogo

        self.z = z
        self.angulo = angulo
        self.velocidade = 10.0

        self.frente = False
        self.tras = False
        self.direita = False
        self.esquerda = False


    def desenha(self):
        self.move()

        glPushMatrix()
        glTranslate(0, 7, 0)
        glRotate(90, 0, 0, 1)
        glScale(10, 10, 10)
        glCallList(self.obj.gl_list)
        glPopMatrix()

    def move(self):
        x, y = 0.0, 0.0
        if self.frente:
            x = self.velocidade * sin(radians(self.angulo))
            y = self.velocidade * cos(radians(self.angulo))
            self.velocidade += 0.5
        elif self.tras:
            x = -self.velocidade * sin(radians(self.angulo))
            y = -self.velocidade * cos(radians(self.angulo))
            self.velocidade += 0.5
        else:
            self.velocidade = 5.0

        if self.direita:
            self.angulo -= 10
        elif self.esquerda:
            self.angulo += 10

        # dentro = false
        # for quad in self.jogo.navMesh:
        #     # se o jogador está fora da zona permitida para andar
        #     if x < quad[0].x and y < quad[0].y \
        #         and :


        self.x -= x
        self.y += y

class Campus(Objeto):

    def desenha(self):
        glPushMatrix()
        glRotate(-90, 0, 0, 1)
        glScale(10, 10, 10)
        glCallList(self.obj[0].gl_list)
        glPopMatrix()