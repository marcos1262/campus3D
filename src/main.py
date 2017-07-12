from OpenGL.GL import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QMainWindow
from PyQt5.QtGui import QMouseEvent

from Audio import Audio
from CarregaModelos import CarregaModelos
from NavMesh import NavMesh
from Objeto import Jogador, Campus
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
        # self.ticketCont = 0

        self.camera = None

        self.jogador = None
        self.objCampus = None
        # self.objSkybox = None

        self.cena = []

        self.navMesh = NavMesh()

        self.audio = Audio(app, self)
        self.audio.toca_musica_fundo()

        self.startTimer(20)

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

        self.light_position = [0, -20, 0, 0.0]
        self.light_ambient_color = [0.2, 0.2, 0.2, 1.0]
        self.light_diffuse_color = [0.8, 1, 0.8, 1.0]
        self.light_specular_color = [0.2, 0.2, 0.2, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.light_ambient_color)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.light_diffuse_color)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.light_specular_color)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)

        glShadeModel(GL_SMOOTH)

        glClearColor(0, 0, 0, 0)

        self.camera = CameraPerspectiva()

        # CarregaModelos(self, ui).start()
        print("Loading Models...")

        self.jogador = Jogador(self, OBJ("../objs/segway.obj", swapyz=False), 0, -30)

        self.objCampus = Campus([OBJ("../objs/campus3dv6.obj", swapyz=False)])
        self.cena.append(self.objCampus)

        # self.objSkybox = Skybox(OBJ("../objs/skybox.obj", swapyz=False))
        # self.cena.append(self.objSkybox)

        print("Models Loaded!")

        self.iniciaJogo = True

    def timerEvent(self, QTimerEvent):
        self.update()

    def paintGL(self):
        """
        Desenha a cena.
        Limpa tela, desenha objetos da cena, verifica ocorrrências de colisão, mostra pontuação e atualiza tela.
        :return: None
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        if not self.iniciaJogo:
            glFlush()
            return

        self.jogador.desenha()

        # sobe/desce jogador
        if -315 < self.jogador.x < -300 \
                and 450 > self.jogador.y > 435 \
                and 105 > self.jogador.angulo % 360 > 75:
            if self.jogador.z == 40:
                ui.labelCenter.setText("Aperte espaço para descer!")
            else:
                ui.labelCenter.setText("Aperte espaço para subir!")
        # mensagem legal
        elif -280 < self.jogador.x < -260 \
                and 1105 > self.jogador.y > 1090 \
                and self.jogador.z == 40 \
                and 295 > self.jogador.angulo % 360 > 255:
            ui.labelCenter.setText("TOC, TOC! Olá professor Daniel?!")
        else:
            ui.labelCenter.setText("")

        glRotate(-self.jogador.angulo, 0, 0, 1)  # rotação do jogador
        glTranslate(-self.jogador.x, -self.jogador.y, -self.jogador.z)  # movimentação do jogador

        for objeto in self.cena:
            objeto.desenha()

        # self.navMesh.desenha()

        glFlush()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:  self.jogador.esquerda = True
        if event.key() == Qt.Key_Right: self.jogador.direita = True
        if event.key() == Qt.Key_Up:    self.jogador.frente = True
        if event.key() == Qt.Key_Down:  self.jogador.tras = True
        if event.key() == Qt.Key_A:     self.jogador.esquerda = True
        if event.key() == Qt.Key_D:     self.jogador.direita = True
        if event.key() == Qt.Key_W:     self.jogador.frente = True
        if event.key() == Qt.Key_S:     self.jogador.tras = True
        if event.key() == Qt.Key_Space:
            if -315 < self.jogador.x < -300 \
                    and 450 > self.jogador.y > 435 \
                    and 105 > self.jogador.angulo % 360 > 75:
                if self.jogador.z == 40:
                    self.jogador.z = 0
                    self.jogador.angulo += 180
                else:
                    self.jogador.z = 40
                    self.jogador.angulo += 180

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:  self.jogador.esquerda = False
        if event.key() == Qt.Key_Right: self.jogador.direita = False
        if event.key() == Qt.Key_Up:    self.jogador.frente = False
        if event.key() == Qt.Key_Down:  self.jogador.tras = False
        if event.key() == Qt.Key_A:     self.jogador.esquerda = False
        if event.key() == Qt.Key_D:     self.jogador.direita = False
        if event.key() == Qt.Key_W:     self.jogador.frente = False
        if event.key() == Qt.Key_S:     self.jogador.tras = False
        if event.key() == Qt.Key_Space:
            print(self.jogador.x, self.jogador.y, self.jogador.z, self.jogador.angulo % 360)

            # def mousePressEvent(self, e: QMouseEvent):
            #     p = e.pos()
            #     print("pressed here:", p.x(), ",", p.y())
            #
            # def mouseMoveEvent(self, e: QMouseEvent):
            #     p = e.pos()
            #     print("moved here:", p.x(), ",", p.y())
            #
            # def mouseReleaseEvent(self, e: QMouseEvent):
            #     p = e.pos()
            #     print("released here:", p.x(), ",", p.y())


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
