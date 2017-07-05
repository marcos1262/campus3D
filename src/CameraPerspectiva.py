from OpenGL.GL import *

from OpenGL.GLU import *


class CameraPerspectiva:
    def __init__(self, fov=90, ar=16.0/9.0, near=1, far=1000):
        self.fov = fov
        self.ar = ar
        self.near = near
        self.far = far
        self.atualiza()

    def atualiza(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(self.fov, self.ar, self.near, self.far)

        gluLookAt(0, -1, 2,
                  0, 0, 2,
                  0, 0, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()