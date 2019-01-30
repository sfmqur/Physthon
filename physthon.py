'''     Library that contains functions useful for the creation of physics simulations to be run in Jupyter.
'''

import pythreejs as three
from random import getrandbits
import numpy as np


# double, double[3], double[3], double[3] -> double[3]
def euler_method(dt, pos_vec, vel_vec, acc_vec):
    """
    a simple function that will output a new position vector after a timestep of dt given a  velocity and acceleration
        vector
    :param dt:
    :param pos_vec:
    :param vel_vec:
    :param acc_vec:
    :return: replaces the old position vector
    """
    for i in range(3):
        vel_vec[i] += acc_vec[i] * dt
        pos_vec[i] += vel_vec[i] * dt
    return pos_vec


# TODO: make sure this outputs valid html colors
#  void -> string
def random_hex_color():
    """
        Returns a random 6 digit hex number for use with colors
    :return: hex string of the format #ffffff
    """
    return '#' + '%0x' % getrandbits(6 * 4)


# double, double, double, double, -> double[3]
def vector_components(magnitude, pos_x, pos_y, pos_z):
    """
        outputs a vector in component form when given the magnitude of the vector in question and a parallel vector's
            components. Useful when converting from central forces
    :param magnitude:
    :param pos_x:
    :param pos_y:
    :param pos_z:
    :return: 3 component vector
    """
    r = np.sqrt(pos_x ** 2 + pos_y ** 2 + pos_z ** 2)
    r_xz = r * np.cos(np.arcsin(pos_y / r))
    r_xy = r * np.cos(np.arcsin(pos_z / r))
    vec_xz = magnitude * np.cos(np.arcsin(pos_y / r))
    vec_xy = magnitude * np.cos(np.arcsin(pos_z / r))
    vec = [vec_xz * pos_x / r_xz, vec_xy * pos_y / r_xy, vec_xz * pos_z / r_xz]
    return vec


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
