import bpy_types
import bpy


def collection_cleanup(collection_name, save_camera=True):
    """
    Cleanup a collection of objects no longer required

    Source: https://blender.stackexchange.com/questions/153713/removing-all-meshes-from-a-collection-with-python
          : https://blender.stackexchange.com/questions/32349/python-scripting-remove-curve-object

    :param collection_name: Name of the collection iterate through

    :param save_camera: If True then this process will exclude cameras in this collection, defaults to True.

    :return: Nothing, delete the objects requested then stop
    """
    # Cleanup the collection
    collection = bpy.data.collections[collection_name]

    meshes = set()
    for obj in collection.objects:
        meshes.add(obj.data)

        if save_camera:
            if not isinstance(obj.data, bpy.types.Camera):
                bpy.data.objects.remove(obj)
        else:
            bpy.data.objects.remove(obj)

    # Look at meshes that are orphaned after objects removal
    for mesh in [m for m in meshes if m.users == 0]:

        # Delete meshes
        if isinstance(mesh, bpy_types.Mesh):
            bpy.data.meshes.remove(mesh)

        # Delete Curves
        elif isinstance(mesh, bpy.types.TextCurve):
            bpy.data.curves.remove(mesh)

        # Delete Camera
        elif isinstance(mesh, bpy.types.Camera):
            bpy.data.cameras.remove(mesh)

        # Warn users if we find mesh type we have not handled
        else:
            print(f"Unknown mesh type of {type(mesh)}: cannot delete")
