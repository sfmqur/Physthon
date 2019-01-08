'''     Library that contains functions useful for the creation of physics simulations to be run in Jupyter.
'''

import numpy as np
import pythreejs as three
from IPython.display import display

#create the scene object which all objects need to be added to
scene = three.Scene()


# int, int -> renderer
def renderer(viewWidth = 600, viewHeight = 400):
    """
    :param viewWidth: width of simulation window
    :param viewHeight: height of simulation window
    :return: threejs renderer object. can run simulation by executing the outputted renderer
    """
    camera = three.PerspectiveCamera(fov=75, aspect=viewWidth / viewHeight, position=[10, 6, 10])
    scene.add(camera)

    # sets up the mouse controls of the camera
    controller = three.OrbitControls(controlling=camera)

    renderer = three.Renderer(scene=scene, camera=camera, width=viewWidth, height=viewHeight,
                              controls=[controller])

    return renderer
