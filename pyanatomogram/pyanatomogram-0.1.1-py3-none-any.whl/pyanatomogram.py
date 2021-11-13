import os
import pathlib
import xml.dom.minidom

import lxml.etree
import matplotlib.cm
import matplotlib.collections
import matplotlib.colors
import matplotlib.pyplot
import matplotlib.transforms
import pandas
import pandas.core.common
import pylustrator.parse_svg

SVG_PATH = pathlib.Path(__file__).parent.joinpath("anatomogram", "src", "svg")


class CurrentAxes:
    """
    Context Manager for setting the matplotlib current axes.
    """

    def __init__(self, ax):
        self.ax = ax
        self.old_ax = None

    def __enter__(self):
        self.old_ax = matplotlib.pyplot.gca()
        matplotlib.pyplot.sca(self.ax)

    def __exit__(self, exc_type, exc_val, exc_tb):
        matplotlib.pyplot.sca(self.old_ax)


class Anatomogram:
    """Class to generate anatomograms."""

    def __init__(self, name):
        self.name = name
        self.filename = os.path.join(SVG_PATH, "{}.svg".format(self.name))
        self.tree = lxml.etree.parse(self.filename)
        self.nsmap = {"svg": "http://www.w3.org/2000/svg"}
        self.efo_layer = self.tree.find(
            '/svg:g[@id="LAYER_EFO"]', namespaces=self.nsmap
        )

    def to_svg(self):
        return lxml.etree.tostring(self.tree, encoding="unicode")

    def save_svg(self, file):
        self.tree.write(file)

    def add_patch_collection(self, ax, ids, label):
        # The ids datastructure may also contain style and may have multiple layers of lists, so flatten to find the
        # artists.
        artists = [
            x
            for x in pandas.core.common.flatten(ids)
            if isinstance(x, matplotlib.pyplot.Artist)
        ]
        collection = matplotlib.collections.PatchCollection(
            artists, match_original=True
        )
        collection.set_label(label)
        ax.add_collection(collection)
        return collection

    def to_matplotlib(self, ax=None):
        """
        Export to matplotlib.
        :param ax: matplotlib axes to draw into or None to draw in the current axes.
        :return: dictionary mapping tissue names to pathcollections.
        """
        if ax is None:
            ax = matplotlib.pyplot.gca()
        x0, y0, x1, y1 = [
            pylustrator.parse_svg.svgUnitToMpl(s)
            for s in self.tree.getroot().get("viewBox").split()
        ]
        ax.set_xlim(x0, x1)
        ax.set_ylim(y1, y0)
        ax.set_aspect(1)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ["left", "right", "top", "bottom"]:
            ax.spines[spine].set_visible(False)

        minidoc = xml.dom.minidom.parseString(self.to_svg())
        ids = {"css": []}
        with CurrentAxes(ax):
            pylustrator.parse_svg.parseGroup(
                minidoc.getElementsByTagName("svg")[0],
                ax.transData.inverted(),
                {},
                ids,
                no_draw=True,
            )
        # Group matplotlib artists into collections:
        collections = {}
        for element in self.efo_layer.xpath(
            'svg:*[local-name()!="use"]', namespaces=self.nsmap
        ):
            uberon_id = element.get("id")
            organ, = element.xpath("svg:title[1]/text()", namespaces=self.nsmap)
            collections[organ] = self.add_patch_collection(ax, ids[uberon_id], organ)
        collections["outline"] = self.add_patch_collection(
            ax, ids["LAYER_OUTLINE"], "outline"
        )

        return collections

    def get_tissue_names(self):
        # Exclude "use"-nodes, as titles overlap with titles of referenced objects.
        return self.efo_layer.xpath(
            'svg:*[local-name()!="use"]/svg:title/text()', namespaces=self.nsmap
        )

    def set_tissue_style(self, tissue, **kwargs):
        """
        Set styling for tissue.
        :param tissue: string, tissue to style. Must be one of the names from get_tissue_names();
        :param kwargs: dict mapping CSS style attributes (fill, stroke, ...) to values;
        """
        elements = self.efo_layer.xpath(
            'svg:*[local-name()!="use" and svg:title[text()="{}"]]'.format(tissue),
            namespaces=self.nsmap,
        )
        if len(elements) != 1:
            raise Exception("Tissue {} not found".format(tissue))
        element, = elements
        style = dict(x.split(":", 1) for x in element.get("style").split(";"))
        style.update(kwargs)
        element.set(
            "style",
            ";".join(["{}:{}".format(key, value) for (key, value) in style.items()]),
        )

    def highlight_tissues(self, tissues, cmap=None, norm=None, style_kwargs=None):
        """
        Highlight multiple tissue with a common colormap.
        :param tissues: dict mapping tissue names to values to color by.
        :param cmap: instance of matplotlib.colors.Colormap, a colormap name, or None (for default colormap).
        :param norm: instance of matplotlib.colors.Normalize or None for default normalization
        :param style_kwargs: dictionary of CSS style attributes to apply to all highlighted tissues.
        """
        cmap = matplotlib.cm.get_cmap(cmap)
        sm = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
        default_style_kwargs = {
            "stroke": "black",
            "stroke-width": 0.2,
            "fill-opacity": 0.8,
        }
        if style_kwargs is None:
            style_kwargs = default_style_kwargs
        else:
            style_kwargs = default_style_kwargs.update(style_kwargs)

        colors = sm.to_rgba(list(tissues.values()))
        for tissue, color in zip(tissues, colors):
            self.set_tissue_style(
                tissue, fill=matplotlib.colors.to_hex(color), **style_kwargs
            )


def facetgrid_helper(organs, values, color, name="homo_sapiens.male", **kwargs):
    """
    Convenience function to use Anatomogram with FacetGrid.
    Use:
    g = seaborn.FacetGrid(...)
    g.map(facetgrid_helper, 'organ-column-name', 'values-column-name')
    :param organs: pandas Series with the organs to highlight in the facet
    :param values: pandas Series with the values corresponding to organs
    :param color: unused, needed for FacetGrid compatibility
    :param name: string, name to pass to Anatomogram. Defaults to homo_sapiens.male
    :param kwargs: dict, keyword arguments passed to Anatomogram.highlight_tissues
    """
    a = Anatomogram(name)
    assert organs.index.equals(values.index)
    a.highlight_tissues(dict(zip(organs, values)), **kwargs)
    a.to_matplotlib()
