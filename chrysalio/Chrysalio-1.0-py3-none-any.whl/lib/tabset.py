"""Widget to create tabs."""

from webhelpers2.html import literal


# =============================================================================
class Tabset(object):
    """A class to manage tabs.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str tabset_id:
        ID of the tab set.
    :param list labels:
        A list of translation strings.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request, tabset_id, labels):
        """Constructor method."""
        self.request = request
        self.tabset_id = tabset_id
        self.tabs = [Tab(self, i, k) for i, k in enumerate(labels)]

    # -------------------------------------------------------------------------
    def begin(self):
        """Output the opening tag of the ``TabSet`` and its table of content as
        an ``<ul>`` structure.

        :rtype: webhelpers2.html.literal
        """
        translate = self.request.localizer.translate
        html = '<div id="{0}" class="cioTabset">\n'\
            '<ul class="cioTabsetToc">\n'.format(self.tabset_id)
        for tab in self.tabs:
            html += '  <li id="{tabset_id}{index}">'\
                '<a class="cioTab" href="#{tabset_id}{index}_">'\
                '<span>{label}</span></a></li>\n'.format(
                    tabset_id=self.tabset_id, index=tab.index,
                    label=translate(tab.label))
        html += '</ul>\n<div class="cioClear"></div>\n'
        return literal(html)

    # -------------------------------------------------------------------------
    @classmethod
    def end(cls):
        """End a tab set.

        :rtype: webhelpers2.html.literal
        """
        return literal('</div>\n')


# =============================================================================
class Tab(object):
    """A class to manage one tab.

    :type  tabset: Tabset
    :param tabset:
        Parent tab set.
    :param int index:
        Index of the tab.
    :param str label:
        Label of the tab.
    """

    # -------------------------------------------------------------------------
    def __init__(self, tabset, index, label):
        """Constructor method."""
        self._tabset = tabset
        self.index = index
        self.label = label

    # -------------------------------------------------------------------------
    def begin(self):
        """Open a tab zone.

        :rtype: webhelpers2.html.literal
        :return:
            Opening ``fieldset`` structure with legend.
        """
        return literal(
            '<fieldset class="cioTabContent" id="{tabset_id}{index}_">\n'
            '  <legend><span>{label}</span></legend>\n'.format(
                tabset_id=self._tabset.tabset_id,
                index=self.index,
                label=self._tabset.request.localizer.translate(self.label)))

    # -------------------------------------------------------------------------
    @classmethod
    def end(cls):
        """Close a tab zone.

        :rtype: webhelpers2.html.literal
        :return:
            Closing ``fieldset`` structure.
        """
        return literal('</fieldset>\n')
