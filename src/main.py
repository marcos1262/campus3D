from OpenGL.GL import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QMainWindow
from PyQt5.QtGui import QMouseEvent

from Audio import Audio
from CarregaModelos import CarregaModelos
from campus3DUI import Ui_MainWindow
from CameraPerspectiva import CameraPerspectiva
from objloader import OBJ


class Campus3D(QOpenGLWidget):
    """
    Representa o jogo.
    """

    def __init__(self, parent):
        QOpenGLWidget.__init__(self, parent)
        self.jogoLargura = 1300
        self.jogoAltura = 700
        self.iniciaJogo = False
        self.ticketCont = 0

        self.camera = None

        # self.texturaJogador = 1

        self.objSegway = None

        # TODO criar classe Bob
        # self.jogador = Bob(0, 0)
        self.cena = []

        self.audio = Audio(app, self)
        # self.audio.toca_musica_fundo()

        self.startTimer(30)

    def initializeGL(self):
        """
        Configurações inicias (tela e câmera).
        Habilita transparência, teste de profundidade, iluminaçao,
        define cor de fundo, modo de superfície e inicializa câmera.
        :return: None
        """
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(GL_NOTEQUAL, 0.0)

        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

        # light_position = [0, 0, 0, 1]
        light_position = [-40, 200, 100, 0.0]
        light_ambient_color = [0.2, 0.2, 0.2, 1.0]
        # light_diffuse_color = [.8, 1, .8, 1]
        light_diffuse_color = [0.5, 0.5, 0.5, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient_color)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse_color)
        # glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.4)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)

        glShadeModel(GL_SMOOTH)

        glClearColor(0, 0, 0, 0)

        self.camera = CameraPerspectiva()

        # CarregaModelos(self, ui).start()
        self.objSegway = OBJ("../objs/segway.obj", swapyz=False)
        self.objCampus = OBJ("../objs/campus3dv3.obj", swapyz=False)
        self.iniciaJogo = True

    def timerEvent(self, QTimerEvent):
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:  self.jogador.esquerda = True
        if event.key() == Qt.Key_Right: self.jogador.direita = True
        if event.key() == Qt.Key_Up:    self.jogador.cima = True
        if event.key() == Qt.Key_Down:  self.jogador.baixo = True
        if event.key() == Qt.Key_A:     self.jogador.esquerda = True
        if event.key() == Qt.Key_D:     self.jogador.direita = True
        if event.key() == Qt.Key_W:     self.jogador.cima = True
        if event.key() == Qt.Key_S:     self.jogador.baixo = True
        if event.key() == Qt.Key_Shift:
            self.jogador.velocidade = 20

    def paintGL(self):
        """
        Desenha a cena.
        Limpa tela, desenha objetos da cena, verifica ocorrrências de colisão, mostra pontuação e atualiza tela.
        :return: None
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        self.desenha_skybox()

        # self.camera.atualiza(self.jogador.x, self.jogador.y, self.jogador.angulo)

        if not self.iniciaJogo:
            glFlush()
            return

        # self.remove_invisiveis()

        for objeto in self.cena:
            objeto.desenha()

        # self.jogador.desenha()

        # self.detecta_colisoes()

        self.mostra_status()

        glPushMatrix()

        glPushMatrix()
        glRotate(-90, 0, 0, 1)
        glCallList(self.objCampus.gl_list)
        glPopMatrix()

        glTranslate(2, 5, 0)
        glCallList(self.objSegway.gl_list)

        glPopMatrix()

        glFlush()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:  self.jogador.esquerda = False
        if event.key() == Qt.Key_Right: self.jogador.direita = False
        if event.key() == Qt.Key_Up:    self.jogador.cima = False
        if event.key() == Qt.Key_Down:  self.jogador.baixo = False
        if event.key() == Qt.Key_A:     self.jogador.esquerda = False
        if event.key() == Qt.Key_D:     self.jogador.direita = False
        if event.key() == Qt.Key_W:     self.jogador.cima = False
        if event.key() == Qt.Key_S:     self.jogador.baixo = False
        if event.key() == Qt.Key_Shift:
            self.jogador.velocidade = 10

    def mousePressEvent(self, e: QMouseEvent):
        p = e.pos()
        print("pressed here:", p.x(), ",", p.y())

    def mouseMoveEvent(self, e: QMouseEvent):
        p = e.pos()
        print("moved here:", p.x(), ",", p.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        p = e.pos()
        print("released here:", p.x(), ",", p.y())

    def desenha_skybox(self):
        # TODO desenhar skybox
        pass

    def encerrar_partida(self):
        # TODO resetar para estado inicial
        pass

    def detecta_colisoes(self):
        # TODO verificar se pegou ticket
        pass

    def mostra_status(self):
        # TODO elaborar jogatina
        pass

        # if self.iniciaJogo:
        #     ui.labelTickets.setText("Tickets: " + str(self.score))


app = None
ui = None
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, Campus3D)
    MainWindow.show()
    sys.exit(app.exec_())
