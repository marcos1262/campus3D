from collections.__main__ import Point
from OpenGL.GL import *


class NavMesh():
    def __init__(self):
        self.quads = []

        self.quads.append([
            Point(35, 100),
            Point(-35, 100),
            Point(-35, -30),
            Point(35, -30)
        ])

    def desenha(self):
        for q in self.quads:
            glBegin(GL_QUADS)
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1, 0, 0])
            glVertex(list(q[0]) + [1])  # superior direito
            glVertex(list(q[1]) + [1])  # superior esquerdo
            glVertex(list(q[2]) + [1])  # inferior esquerdo
            glVertex(list(q[3]) + [1])  # inferior direito
            glEnd()
