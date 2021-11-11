from __future__ import print_function

import re


class MarkDownFormat(object):

    def escape_entities(self, txt):
        """
        Escapes markdown symbols for underscores, ampersands, less-than and
        greater-than symbols.
        """
        out = ""
        quotpat = re.compile(r'([^`]*)(`[^`]*`)(.*$)')
        while txt:
            m = quotpat.match(txt)
            unquot  = m.group(1) if m else txt
            literal = m.group(2) if m else ""
            txt     = m.group(3) if m else ""
            unquot = unquot.replace(r'_', r'\_')
            unquot = unquot.replace(r'&',r'&amp;')
            unquot = unquot.replace(r'<', r'&lt;')
            unquot = unquot.replace(r'>',r'&gt;')
            out += unquot + literal
        return out

    def header_link(self, name):
        refpat = re.compile("[^a-z0-9_ -]")
        return refpat.sub("", name.lower()).replace(" ", "-")

    def get_link(self, label, anchor, targfile=None, literalize=True):
        if literalize:
            label = "`{0}`".format(label)
        else:
            label = self.escape_entities(label)
        return "[{0}]({1}#{2})".format(
            label,
            targfile if targfile != None else "",
            self.header_link(anchor)
        )

    def horizontal_rule(self):
        return [ "---", "" ]

    def file_header(self, title, subtitle=""):
        return [
            "# {}: {}".format(
                self.escape_entities(self.title),
                self.escape_entities(sub)
            ),
            ""
        ]

    def section_header(self, title, subtitle=""):
        return [
            "## {}: {}".format(
                self.escape_entities(self.title),
                self.escape_entities(sub)
            ),
            ""
        ]

    def item_header(self, title, subtitle=""):
        return [
            "### {}: {}".format(
                self.escape_entities(self.title),
                self.escape_entities(sub)
            ),
            ""
        ]

    def block_header(self, title, subtitle=""):
        return [
            "**{}:** {}".format(
                self.escape_entities(self.title),
                self.escape_entities(sub)
            )
        ]

    def image(self, title, subtitle="", rel_url=""):
        return [
            '![{0} {1}]({2} "{0} {1}")'.format(
                mkdn_esc(self.parent.subtitle),
                mkdn_esc(self.title),
                rel_url
            )
            "",
        ]

    def code_block(self, code):
        out = [ "``` {.C linenos=True}" ]
        for line in code:
            out.append(line)
        out.append("```")
        out.append("")
        return out

    def bullet_list(self, items):
        return [ "- {}".format(item) for item in items ]

    def numbered_list(self, items):
        return [
            "{:d}. {}".format(num, item)
            for num, item in enumerate(items)
        ]

    def table(self, headers, rows):
        pass



# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap
