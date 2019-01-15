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
        # TODO: set up near and far
        self.camera = three.PerspectiveCamera(fov=75, aspect=viewWidth / viewHeight, position=[-10, -6, -10])
        self.scene.add(self.camera)

        self.lights = [three.AmbientLight(), three.DirectionalLight(position=[0, -10, -10])]
        for l in self.lights:
            self.scene.add(l)

        # sets up the mouse controls of the camera
        self.controller = three.OrbitControls(controlling=self.camera)

        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])

    def render(self):
        return self.renderer

# self.geo needs to be added to Renderer scene
class Sphere:
    def __init__(self, radius=5, position=[0, 0, 0], color='red', velocity=[0, 0, 0], acceleration=[0, 0, 0]):
        self.radius = radius
        self.geo = three.SphereBufferGeometry(radius=self.radius, widthSegments=10, heightSegments=10)
        self.color = color
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
