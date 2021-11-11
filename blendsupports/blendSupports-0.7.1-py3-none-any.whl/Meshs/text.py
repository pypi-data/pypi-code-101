from blendSupports.Nodes.emission_node import create_emission_node
import bpy


def make_text(object_name, bound, y_mean_val, text, height_iterator, object_colour, align="LEFT"):
    """
    Creates a text object starting at x 'bound' and at y 'y_mean_val' displaying 'text'. It is scaled to be equal to the
    objects via the 'height_iter'

    :param object_name: The name of the object
    :type object_name: str

    :param bound: Starting x position
    :type bound: float

    :param y_mean_val: Y position
    :type y_mean_val: float

    :param text: Text to display
    :type text: str

    :param height_iterator: Scaling about to make text relative to all other components
    :type height_iterator: float

    :param object_colour: RGBA colour of the object

    :param align: Aligns the text, Takes LEFT, RIGHT, and CENTER
    :type align: str

    :return: Nothing, make the text object then stop
    """

    # Create the text object
    bpy.ops.object.text_add(location=(bound, y_mean_val, 0))

    # Set its name
    obj = bpy.context.object
    obj.data.body = text
    create_emission_node(obj, object_colour)
    bpy.context.object.name = object_name
    bpy.context.object.data.align_x = align

    # Scale it relative to all other elements
    bpy.ops.transform.resize(value=(height_iterator, height_iterator, height_iterator))
    bpy.ops.object.select_all(action='DESELECT')

    return obj
