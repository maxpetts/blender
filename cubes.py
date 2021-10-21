import bpy
import random
import sys


def delete_all():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=True, confirm=False)
    bpy.ops.object.material_slot_remove_unused


def run():

    bpy.context.scene.frame_end = 200

    # Generate cubes
    for x in range(10):
        for y in range(10):
            bpy.ops.mesh.primitive_cube_add(size=2, location=(x*2, y*2, 0))
            bpy.context.active_object.data.materials.append(
                bpy.data.materials.new(name="gray"))
            bpy.context.active_object.data.materials[0].diffuse_color = (
                0.3, 0.3, 0.3, 1)

            # Select a random few to animate
            if (random.randint(0, 1) == 1):

                bpy.context.active_object.keyframe_insert(
                    data_path="location", frame=0.0
                )
                for i in range(21):

                    z_modifier = random.uniform(0, 2)

                    if ((i*10) % 20 == 0):
                        bpy.context.active_object.location.z = -z_modifier
                        bpy.context.active_object.keyframe_insert(
                            data_path="location", frame=i * 10)
                    else:
                        bpy.context.active_object.location.z = z_modifier
                        bpy.context.active_object.keyframe_insert(
                            data_path="location", frame=i * 10)

    materials = [bpy.data.materials.new(name="red"), bpy.data.materials.new(
        name="blue"), bpy.data.materials.new(name="green")]
    materials[0].diffuse_color = (1, 0, 0, 1)
    materials[1].diffuse_color = (0, 1, 0, 1)
    materials[2].diffuse_color = (0, 0, 1, 1)

    # Select some cubes & assign them the above materials. Has the chance to select same cube twice..
    for z in range(random.randint(45, 100)):
        obj = random.choice((bpy.context.visible_objects))
        if obj.data.materials:
            # assign to 1st material slot
            obj.data.materials[0] = materials[random.randint(0, 2)]
        else:
            # no slots
            obj.data.materials.append(materials[random.randint(0, 2)])


try:
    delete_all()
    run()
except Exception as e:
    print("ERROR: ")
    print(e)
    sys.exit(1)
