'''     Library that contains functions useful for the creation of physics simulations to be run in Jupyter.
'''

import numpy as np
import pythreejs as three
from IPython.display import display


class Renderer:
    def __init__(self, viewWidth=600, viewHeight=400):
        self.width = viewWidth
        self.height = viewHeight
        self.scene = three.Scene()

        # sets up the camera for this renderer
        self.camera = three.PerspectiveCamera(fov=75, aspect=viewWidth / viewHeight, position=[-10, -6, -10])
        self.scene.add(self.camera)

        # sets up the mouse controls of the camera
        self.controller = three.OrbitControls(controlling=self.camera)

        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])

    def render(self):
        return self.renderer


class Sphere:
    def __init__(self, size=5, position=[0, 0, 0], color='red', velocity=[0, 0, 0]):
        self.size = size
        self.color = color
        self.pos = position
        self.vel = velocity
