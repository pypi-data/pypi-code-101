from blendSupports.Nodes.emission_node import create_emission_node
import bpy


def make_mesh(object_name, object_colour=(0.25, 0.25, 0.25, 1.0), collection="Collection"):
    """
    Create a mesh then return the object reference and the mesh object

    :param object_name: Name of the object
    :type object_name: str

    :param object_colour: RGBA colour of the object, defaults to a shade of grey
    :type object_colour: (float, float, float, float)

    :param collection: Where you want the objected to be added, defaults to Collection
    :type collection: str

    :return: Object reference and mesh reference
    """
    # Make the block
    mesh = bpy.data.meshes.new(object_name)  # add the new mesh
    obj = bpy.data.objects.new(mesh.name, mesh)
    create_emission_node(obj, object_colour)
    col = bpy.data.collections.get(collection)
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj

    return obj, mesh
