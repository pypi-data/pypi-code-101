import bpy


def create_emission_node(obj, colour, strength=1.0, custom_name=None):
    """
    Create an emission node for this object

    Source: https://blender.stackexchange.com/questions/23436/control-cycles-material-nodes-and-material-
            properties-in-python


    :param obj: The current blender object
    :param colour: RGBA colour

    :param strength: Intensity of the emission node
    :type strength: float

    :param custom_name: An custom name to use instead of the object
    :type custom_name: str | None

    :return: Nothing, make the emission node then stop
    :rtype: None
    """

    # Set custom names to avoid override if required
    if custom_name:
        mat_name = custom_name
    else:
        mat_name = obj.name

    # Test if material exists, If it does not exist, create it:
    mat = (bpy.data.materials.get(mat_name) or
           bpy.data.materials.new(mat_name))

    # Enable 'Use nodes':
    mat.use_nodes = True

    # clear all nodes to start clean
    nodes = mat.node_tree.nodes
    nodes.clear()

    # create emission node
    node_emission = nodes.new(type='ShaderNodeEmission')
    node_emission.inputs[0].default_value = colour
    node_emission.inputs[1].default_value = strength
    node_emission.location = 0, 0

    # create output node
    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    node_output.location = 400, 0

    node = nodes.new('ShaderNodeBsdfDiffuse')
    node.location = (100, 100)

    # link nodes
    links = mat.node_tree.links
    links.new(node_emission.outputs[0], node_output.inputs[0])

    obj.data.materials.append(mat)