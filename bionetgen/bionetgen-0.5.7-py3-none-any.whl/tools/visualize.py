import os, bionetgen, glob, xmltodict, copy
from tempfile import TemporaryDirectory


class VisResult:
    def __init__(self, input_folder, name=None, vtype=None) -> None:
        self.input_folder = input_folder
        self.name = name
        self.vtype = vtype
        self.rc = None
        self.out = None
        self.files = []
        self.file_strs = {}
        self.file_graphs = {}
        self._load_files()

    def _load_files(self) -> None:
        # we need to assume some sort of GML output
        # at least for now
        # use the name, if given, search for GMLs if not
        gmls = glob.glob("*.gml")
        graphmls = glob.glob("*.graphml")
        graphfiles = gmls + graphmls
        for gfile in graphfiles:
            if self.name is None:
                self.files.append(gfile)
                # now load into string
                with open(gfile, "r") as f:
                    l = f.read()
                self.file_strs[gfile] = l
            else:
                # pull GMLs that contain the name
                if self.name in gfile:
                    self.files.append(gfile)
                    # now load into string
                    with open(gfile, "r") as f:
                        l = f.read()
                    self.file_strs[gfile] = l

    def _dump_files(self, folder) -> None:
        os.chdir(folder)
        for gfile in self.files:
            g_name = os.path.split(gfile)[-1]
            with open(g_name, "w") as f:
                f.write(self.file_strs[gfile])


class BNGVisualize:
    def __init__(
        self, input_file, output=None, vtype=None, bngpath=None, suppress=None
    ) -> None:
        # set input, required
        self.input = input_file
        # set valid types
        self.valid_types = [
            "contactmap",
            "ruleviz_pattern",
            "ruleviz_operation",
            "regulatory",
        ]
        self.accept_types = [
            "contactmap",
            "ruleviz_pattern",
            "ruleviz_operation",
            "regulatory",
            "all",
        ]
        # set visualization type, default yo contactmap
        if vtype is None or len(vtype) == 0:
            vtype = "contactmap"
        if vtype not in self.accept_types:
            raise ValueError(f"{vtype} is not a valid visualization type")
        self.vtype = vtype
        # set output
        self.output = output
        self.suppress = suppress
        self.bngpath = bngpath
        self.mode = "normal"
        self.input2 = None

    def run(self) -> VisResult:
        if self.mode == "normal":
            self._normal_mode()
        elif self.mode == "diff":
            self._diff_mode()
        else:
            raise RuntimeError(f"Mode {self.mode} is not recognized")

    def _diff_mode(self):
        # first, check the input types, if we have bngl files we need
        # to first make the visualization types and then do diff
        # Temporarily we assume both are already graphmls so we can

        # work on the diff algorithm
        graph_file_1 = self.input
        graph_file_2 = self.input2
        with open(graph_file_1, "r") as f:
            graph_dict_1 = xmltodict.parse(f.read())
        with open(graph_file_2, "r") as f:
            graph_dict_2 = xmltodict.parse(f.read())
        # Now we have the graphml files, now we do diff
        diff_dict = self.diff_graphs(graph_dict_1, graph_dict_2)

    def diff_graphs(
        self, g1, g2, colors={"g1": "#3CB043", "g2": "#D0312D", "intersect": "#3944BC"}
    ):
        """
        Given two XML dictionaries (using xmltodict) of two graphml
        graphs, do the diff and return the difference graphml xml in
        dictionary format

        The result is g1-g2. By default g1 only stuff are colored green
        g2 only nodes are colored red and common elements are colored blue.
        These can be changed by the colors kwarg which is a dictionary with
        keys g1, g2 and intersect and colors are given as hexcode strings.

        input
            g1: dict
            g2: dict
            colors (opt): dict

        output
            diff_g1_g2: dict
        """
        # first do a deepcopy so we don't have to
        # manually do add boilerpate
        diff_gml = copy.deepcopy(g1)
        self._find_diff(g1, g2, diff_gml, colors)
        # now write gml as graphml
        with open("test.graphml", "w") as f:
            f.write(xmltodict.unparse(diff_gml))

    def _find_diff(self, g1, g2, dg, colors):
        # first find differences in nodes
        # FIXME: Check for single nodes before looping
        node_stack = [(["graphml"], g1["graphml"])]
        dnode_stack = [(["graphml"], dg["graphml"])]
        while len(node_stack) > 0:
            curr_keys, curr_node = node_stack.pop(-1)
            curr_dkeys, curr_dnode = dnode_stack.pop(-1)
            # let's take a look at the difference
            if self._get_node_from_keylist(g2, curr_keys):
                # we have the node in g2, we color it appropriately
                self._color_node(curr_dnode, colors["intersect"])
            else:
                # we don't have the node in g2, we color it appropriately
                self._color_node(curr_dnode, colors["g1"])
            # if we have graphs in there, add the nodes to the stack
            if "graph" in curr_node.keys():
                # there is a graph in the node, add the nodes to stack
                if isinstance(curr_node["graph"]["node"], list):
                    for inode, node in enumerate(curr_node["graph"]["node"]):
                        ckey = curr_keys + [node["@id"]]
                        node_stack.append((ckey, node))
                        dnode_stack.append(
                            (
                                curr_dkeys + [node["@id"]],
                                curr_dnode["graph"]["node"][inode],
                            )
                        )
                else:
                    ckey = curr_keys + [curr_node["graph"]["node"]["@id"]]
                    node_stack.append((ckey, curr_node["graph"]["node"]))
                    dnode_stack.append((ckey, curr_dnode["graph"]["node"]))

    def _get_node_from_keylist(self, g, keylist):
        copy_keylist = copy.copy(keylist)
        gkey = copy_keylist.pop(0)
        if len(copy_keylist) == 0:
            # we only have "graphml" as key
            return g[gkey]
        # we are out of group nodes
        if "graph" not in g[gkey].keys():
            return False
        # everything up to here is good,
        # loop over to find the node
        import ipdb

        ipdb.set_trace()
        nodes = g[gkey]["graph"]["node"]
        while len(copy_keylist) > 0:
            key = copy_keylist.pop(0)
            found = False
            for cnode in nodes:
                if cnode["@id"] == key:
                    found = True
                    node = cnode
                    nodes = node["graph"]["node"]
            if not found:
                return False
        return node

    def _color_node(self, node, color):
        if "data" in node.keys():
            node_key = None
            for key in node["data"]:
                if "y:" in key:
                    node_key = key
                    break
            if node_key is None:
                return False
            ynode = node["data"][node_key]
            node_key = None
            for key in ynode.keys():
                if "y:" in key:
                    node_key = key
                    break
            if node_key is None:
                return False
            ynode = ynode[node_key]
            node_key = None
            for key in ynode.keys():
                if "y:" in key:
                    node_key = key
                    break
            if node_key is None:
                return False
            ynode = ynode[node_key]
            ynode["y:Fill"]["@color"] = color
            return True
        return False

    def _get_node_text(self, node):
        noded = node["data"]["y:ProxyAutoBoundsNode"]["y:Realizers"]
        for key in noded.keys():
            if "y:" in key:
                return noded[key]["y:NodeLabel"]["#text"]
        return None

    def _normal_mode(self):
        model = bionetgen.modelapi.bngmodel(self.input)
        model.actions.clear_actions()
        if self.vtype == "all":
            for valid_type in self.valid_types:
                model.add_action("visualize", action_args={"type": f"'{valid_type}'"})
        else:
            model.add_action("visualize", action_args={"type": f"'{self.vtype}'"})
        # TODO: Work in temp folder
        cur_dir = os.getcwd()
        from bionetgen.core.main import BNGCLI

        if self.output is None:
            with TemporaryDirectory() as out:
                # instantiate a CLI object with the info
                cli = BNGCLI(model, out, self.bngpath, suppress=self.suppress)
                try:
                    cli.run()
                    # load vis
                    vis_res = VisResult(
                        os.path.abspath(os.getcwd()),
                        name=model.model_name,
                        vtype=self.vtype,
                    )
                    # go back
                    os.chdir(cur_dir)
                    # dump files
                    vis_res._dump_files(cur_dir)
                    return vis_res
                except Exception as e:
                    os.chdir(cur_dir)
                    # TODO: Better error reporting, improve consistency of reporting
                    print("Couldn't run the simulation")
                    print(e)
                    raise
        else:
            # instantiate a CLI object with the info
            cli = BNGCLI(model, self.output, self.bngpath, suppress=self.suppress)
            try:
                cli.run()
                # load vis
                vis_res = VisResult(
                    os.path.abspath(os.getcwd()),
                    name=model.model_name,
                    vtype=self.vtype,
                )
                # go back
                os.chdir(cur_dir)
                return vis_res
            except Exception as e:
                os.chdir(cur_dir)
                # TODO: Better error reporting, improve consistency of reporting
                print("Couldn't run the simulation")
                print(e)
                raise
