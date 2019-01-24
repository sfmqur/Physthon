'''     Library that contains functions useful for the creation of physics simulations to be run in Jupyter.
'''

import pythreejs as three
from random import getrandbits

# TODO: make sure this outputs valid html colors
# void -> string
def random_hex_color():
    '''
        Returns a random 6 digit hex number for use with colors
    :return: hex string of the format #ffffff
    '''

    return '#' + '%0x' % getrandbits(6 * 4)


class Renderer:
    def __init__(self, view_width=600, view_height=400, camera_position=[10, 6, 10], view_range=[0.1, 1000], fov=75,
                 light_position=[0, 10, 10]):
        self.scene = three.Scene()
        self.width = view_width
        self.height = view_height

        # sets up the camera for this renderer
        self.camera = three.PerspectiveCamera(fov=fov, aspect=self.width / self.height, position=camera_position,
                                              near=view_range[0], far=view_range[1])
        # scene takes in a list of things to add
        self.scene.add([self.camera])

        self.lights = [three.AmbientLight(), three.DirectionalLight(position=light_position)]
        self.scene.add(self.lights)

        # sets up the mouse controls of the camera
        self.controller = three.OrbitControls(controlling=self.camera)
        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])

    def render(self):
        self.renderer = three.Renderer(scene=self.scene, camera=self.camera, width=self.width, height=self.height,
                                       controls=[self.controller])
        return self.renderer


class PositionAnimator:
    # .mesh of the moving object, double[], double[] -> void
    def __init__(self, object_mesh, time_list, position_list):
        self.position_track = three.VectorKeyframeTrack(name='.position', times=time_list, values=position_list)
        self.clip = three.AnimationClip(tracks=[self.position_track])
        self.action = three.AnimationAction(three.AnimationMixer(object_mesh), self.clip, object_mesh)

    def animate(self):
        return self.action.play()


# self.mesh needs to be added to Renderer scene to be visible
class Box:
    # color can be in hex format #ffffff
    def __init__(self, width=1, height=1, depth=1, color='red', mass=1, position=[0, 0, 0], velocity=[0, 0, 0],
                 acceleration=[0, 0, 0]):
        self.width = width
        self.height = height
        self.depth = depth
        self.geo = three.BoxBufferGeometry(width=self.width, height=self.height, depth=self.depth, widthSegments=1,
                                           heightSegments=1, depthSegments=1)
        self.mat = three.MeshPhysicalMaterial(color=color)
        # TODO: fix it so that calling self (ie scene.add(box))returns the self.mesh
        self.mesh = three.Mesh(geometry=self.geo, material=self.mat, position=position)

        self.mass = mass
        # WARNING: position is in the form of [x,z,y]
        self.pos = position
        self.vel = velocity
        self.acc = acceleration


# self.geo needs to be added to Renderer scene
class Sphere:
    # color can be in hex format #ffffff
    def __init__(self, radius=1, color='orange', mass=1, position=[0, 0, 0], velocity=[0, 0, 0],
                 acceleration=[0, 0, 0]):
        self.radius = radius
        self.geo = three.SphereBufferGeometry(radius=self.radius, widthSegments=32, heightSegments=16)
        self.mat = three.MeshPhysicalMaterial(color=color)
        # TODO: fix it so that calling self (ie scene.add(sphere))returns the self.mesh
        self.mesh = three.Mesh(geometry=self.geo, material=self.mat, position=position)

        self.mass = mass
        # WARNING: position is in the form of [x,z,y]
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
