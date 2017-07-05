from threading import Thread

from objloader import OBJ


class CarregaModelos(Thread):
    def __init__(self, jogo, ui):
        Thread.__init__(self)
        self.jogo = jogo
        self.ui = ui

    def run(self):
        print("Loading Models...")
        self.ui.labelLoading.setText("Loading Models...")

        # self.carrega_textura("../images/Spacecrafts/tie-figher.png", self.texturaJogador)

        # self.jogo.objSegway = OBJ("../objs/tinker.obj", swapyz=True)
        # self.jogo.objCampus = OBJ("../objs/campus3dv3.obj", swapyz=False)

        self.ui.labelLoading.setText("")
        print("Models Loaded!")

        self.jogo.iniciaJogo = True