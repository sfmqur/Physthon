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
        self.camera = three.PerspectiveCamera(fov=75, aspect=viewWidth / viewHeight, position=[10, 6, 10], near=0.1,
                                              far=1000, )
        # scene takes in a list of things to add
        self.scene.add([self.camera])

        self.lights = [three.AmbientLight(), three.DirectionalLight(position=[0, 10, 10])]
        self.scene.add(self.lights)

        # sets up the mouse controls of the camera
        self.controller = three.OrbitControls(controlling=self.camera)
        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])

    def render(self):
        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])
        return self.renderer


# self.geo needs to be added to Renderer scene
class Sphere:
    # color can be in hex format #ffffff
    def __init__(self, radius=5, color='red', mass=1, position=[0, 0, 0], velocity=[0, 0, 0], acceleration=[0, 0, 0]):
        self.radius = radius
        self.geo = three.SphereBufferGeometry(radius=self.radius, widthSegments=10, heightSegments=10)
        self.mat = three.MeshPhysicalMaterial(color=color)
        # TODO: fix it so that calling self (ie scene.add(sphere))returns the self.mesh
        self.mesh = three.Mesh(geometry=self.geo, material=self.mat)

        self.mass = mass
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
