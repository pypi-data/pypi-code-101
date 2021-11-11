from blendSupports.Meshs.mesh_ref import make_mesh
import bpy


def make_graph_axis(colour, x_end, y_end, width=0.3, bound=0.2, name="Axis", collection="Collection"):
    """
    Axis for a standard graph

    :param colour: RGBA colour of the axis
    :type colour: (float, float, float, float)

    :param x_end: X axis width
    :type x_end: float

    :param y_end: Y axis height
    :type y_end: float

    :param width: Width of the lines, defaults to 0.3
    :type width: float

    :param bound: Distance between axis and 0 for padding between elements in the graph and the axis, defaults to 0.2
    :type bound: float

    :param name: Name of the object, defaults to Axis
    :type name: str

    :param collection: Default collect of the mesh, defaults to Collection
    :type collection: str

    :return: Nothing, make mesh then stop
    :rtype: None
    """
    obj, mesh = make_mesh(name, colour, collection)

    verts = [
        (-bound, y_end, 0),
        (-bound, -(width + bound), 0),
        (-(width + bound), -(width + bound), 0),
        (-(width + bound), y_end, 0),

        (x_end, -bound, 0),
        (x_end, -(width + bound), 0),
        (-(width + bound), -(width + bound), 0),
        (-(width + bound), -bound, 0)

    ]

    edges = []
    faces = [[0, 1, 2, 3], [4, 5, 6, 7]]
    mesh.from_pydata(verts, edges, faces)
    bpy.ops.object.select_all(action='DESELECT')
