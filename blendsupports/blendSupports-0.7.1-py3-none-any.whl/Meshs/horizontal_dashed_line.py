from blendSupports.Meshs.mesh_ref import make_mesh

from miscSupports import chunk_list
import bpy


def make_horizontal_dashed_line(name, colour, total_width, width_min, height, line_density=80, line_width=0.1,
                                collection="Collection"):
    """
    Make a dashed line horizontally for things line significance thresholds

    :param name: Name of the mesh
    :type name: str

    :param colour: RGBA colour of the line
    :type colour: (float, float, float, float)

    :param total_width: maximum x
    :type total_width: float

    :param width_min: minimum x
    :type width_min: float

    :param height: y dimension you want the line to follow
    :type height: float

    :param line_density: Number of segments in the line, defaults to 80
    :type line_density: int

    :param line_width: width of the segments, defaults to 0.1
    :type line_width: float

    :param collection: Collection
    :type collection: str

    :return: Nothing, make mesh then finished
    :rtype: None
    """

    # Create the object reference
    obj, mesh = make_mesh(name, colour, collection)

    # Determine the width of the line segments based on how many segments we need
    width_iter = total_width / line_density
    total = width_min

    # Isolate the vertexes on even index intervals
    verts = []
    for i in range(line_density):

        if i % 2 == 0:
            verts.append((total + width_iter, height + (line_width / 2), 1))
            verts.append((total + width_iter, height - (line_width / 2), 1))
            verts.append((total, height - (line_width / 2), 1))
            verts.append((total, height + (line_width / 2), 1))
            total += width_iter

        else:
            total += width_iter

    # Create an index reference for the verts, then chunk them into fours representing the four corners of each segment
    vert_indexes = [i for i in range(len(verts))]
    faces = chunk_list(vert_indexes, 4)

    # Create the mesh
    edges = []
    mesh.from_pydata(verts, edges, faces)
    bpy.ops.object.select_all(action='DESELECT')