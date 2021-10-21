import bpy
import random
import sys


def delete_all():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=True, confirm=False)


def run():
    for x in range(10):
        for y in range(10):
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x*2, y*2, 0))
            bpy.context.active_object.name = "c" + str(x) + str(y)

    material = bpy.data.materials.new(name="red")
    material.diffuse_color = (1, 0, 0, 1)

    for z in range(8):
        obj = random.choice((bpy.context.visible_objects))
        if obj.data.materials:
            # assign to 1st material slot
            obj.data.materials[0] = material
        else:
            # no slots
            obj.data.materials.append(material)


try:
    delete_all()
    run()
except Exception as e:
    print("ERROR: ")
    print(e)
    sys.exit(1)
