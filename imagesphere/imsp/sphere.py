import bpy
import sys
from os.path import isfile

# Take image path as the last command line argument
imgPath = sys.argv[-1]

o  = bpy.data.objects['Sphere'] # Replace with your actual object's name
t  = o.active_material.node_tree
im = t.nodes['Image Texture'].image

# If provided image exists set is as the image texture node's image
if isfile( imgPath ): im.filepath = imgPath
bpy.ops.render.render(animation=True)
