from miscSupports import tuple_convert
from pathlib import Path
import bpy


class EngineInvalidError(Exception):
    """Invalid engine"""
    def __init__(self, engine):
        super().__init__(f"Engine takes the value of 'CYCLES' or 'BLENDER_EEVEE' yet found {engine}")


class CameraTypeError(Exception):
    """Invalid Camera"""
    def __init__(self, camera_type):
        super().__init__(f"Camera Type takes the value of 'PANO', 'ORTHO', or 'PERSP' yet found {camera_type}")


def setup_camera(camera_name, camera_position, camera_scale, camera_type, film_transparent, x_resolution, y_resolution):
    # Set the output resolution and camera scale
    bpy.context.scene.render.resolution_x = int(x_resolution)
    bpy.context.scene.render.resolution_y = int(y_resolution)

    # Set the camera position and scale
    if camera_type.upper() not in ['PANO', "ORTHO", "PERSP"]:
        raise CameraTypeError(camera_type.upper())

    # Find Camera, set camera type
    camera = bpy.data.objects[camera_name]
    camera.data.type = camera_type.upper()

    # Set the cameras location, and if camera type is orthographic set orthographic scale
    camera.location = tuple_convert(camera_position)
    if camera_type == "ORTHO":
        camera.data.ortho_scale = float(camera_scale)

    # Set transparency
    bpy.context.scene.render.film_transparent = film_transparent


def render_scene(camera_position, write_directory, write_name, engine="CYCLES", x_resolution=1080,
                 y_resolution=1080, camera_type="ORTHO", camera_scale=5, save_file=True, film_transparent=True,
                 file_type="png", camera_name="Camera"):

    if engine.upper() not in ["CYCLES", "BLENDER_EEVEE"]:
        raise EngineInvalidError(engine.upper())
    bpy.context.scene.render.engine = engine

    # Setup the camera
    setup_camera(camera_name, camera_position, camera_scale, camera_type, film_transparent, x_resolution, y_resolution)

    # Render the scene
    bpy.context.scene.render.filepath = str(Path(write_directory, f"{write_name}.{file_type}").absolute())
    bpy.context.scene.eevee.use_gtao = True
    bpy.ops.render.render(write_still=True)

    # Save the blend file for manual manipulation if requested
    if save_file:
        bpy.ops.wm.save_as_mainfile(filepath=f"{write_directory}/{write_name}.blend")


def open_gl_render(camera_position, write_directory, write_name, x_resolution=1080, y_resolution=1080,
                   camera_type="ORTHO", camera_scale=5, save_file=True, film_transparent=True, file_type="png",
                   camera_name="Camera"):

    # Turn off all viewport options
    remove_viewport_3d()

    # Setup the camera
    setup_camera(camera_name, camera_position, camera_scale, camera_type, film_transparent, x_resolution, y_resolution)

    # Open GL render the scene
    bpy.context.scene.render.filepath = str(Path(write_directory, f"{write_name}.{file_type}").absolute())
    bpy.ops.render.opengl(write_still=True, view_context=True)

    # Save the blend file for manual manipulation if requested
    if save_file:
        bpy.ops.wm.save_as_mainfile(filepath=f"{write_directory}/{write_name}.blend")


def context_type_dict(context_bpy):
    """Create a dict from a given context object within blender"""
    return {context.type: context for context in context_bpy}


def remove_viewport_3d():
    """Open GL renders will render all the elements in the viewport, so unless we disable them they will be visible"""
    # Isolate the VIEW_3D screen area and then context overlay space
    area = context_type_dict(bpy.context.screen.areas)["VIEW_3D"]
    space = context_type_dict(area.spaces)["VIEW_3D"].overlay

    # For set all attributes of this layer to False
    attributes = ["show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_object_origins"]
    [setattr(space, attr, False) for attr in attributes]
