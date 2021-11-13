import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Toolbar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(500, -1)
        self.connect("destroy", Gtk.main_quit)

        toolbar = Gtk.Toolbar()
        self.add(toolbar)

        openbtn = Gtk.ToolButton()
        openbtn.set_label("Open")
        openbtn.set_is_important(True)
        openbtn.set_icon_name("gtk-open")
        openbtn.connect('clicked', self.on_item_activated)
        toolbar.add(openbtn)

        savebtn = Gtk.ToolButton()
        savebtn.set_label("Save")
        savebtn.set_is_important(True)
        savebtn.set_icon_name("gtk-save")
        savebtn.connect('clicked', self.on_item_activated)
        toolbar.add(savebtn)

    def on_item_activated(self, recentchoosermenu):
        item = recentchoosermenu.get_current_item()

        if item:
            print("Item selected:")
            print("Name:\t %s" % (item.get_display_name()))
            print("URI:\t %s" % (item.get_uri()))

window = Toolbar()
window.show_all()

Gtk.main()