from cbook.model import helper
from cbook.config import config
from cbook.controller.re_controller import ReController
from cbook.controller.rc_controller import RvController
from cbook.view import recipe_button as rb
from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QDialogButtonBox, QFileDialog, QMessageBox, QVBoxLayout
import os
from os.path import split



class MwController:
    label_filter = []
    categories = []
    nahrung = []
    kohlehydrate = []
    
    def __init__(self, model, window):
        self.model = model
        self.window = window
        self.rv_controller = RvController(model, window)
        self.re_controller = ReController(model, window)

        self.window.recipeList.layout().addStretch()

        self.window.backButton.clicked.connect(self.open_recipe_list)
        self.window.buttonCancel.clicked.connect(self.open_recipe_list)
        self.window.buttonNeuesRezept.clicked.connect(self.create_new_recipe)
        self.window.buttonSave.clicked.connect(self.save_recipe)
        self.window.editButton.clicked.connect(self.edit_recipe)
        self.window.toolButtonDelete.clicked.connect(self.open_confirmation_dialog)
        self.window.toolButtonFolder.clicked.connect(self.change_folder)

        recipes_path = config.get_recipe_path()
        while not config.get_recipe_path():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Noch kein Rezeptordner ausgewählt.")
            msg.setInformativeText("Bitte einen Rezeptordner wählen!")
            msg.setWindowTitle("Rezeptordner wählen")
            msg.setStandardButtons(QMessageBox.Open | QMessageBox.Cancel)

            ret = msg.exec_()
            if ret == QMessageBox.Cancel:
                exit()
            elif ret == QMessageBox.Open:
                # open file chooser
                fd = QFileDialog()
                options = QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
                text = "Wähle Rezeptordner"
                path = os.path.expanduser('~')
                dir = fd.getExistingDirectory(msg, text, path, options)
                if dir:
                    config.set_recipe_path(dir)

        self.load_recipes()


    def change_folder(self):
        fd = QFileDialog()
        options = QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        text = "Wähle Rezeptordner"
        path = os.path.expanduser('~')
        dir = fd.getExistingDirectory(self.window, text, path, options)
        if dir:
            config.set_recipe_path(dir)
        self.window.delete_recipe_buttons()
        self.load_recipes()


    def load_recipes(self):
        self.model.load_recipes()
        self.read_recipes()
        self.create_checkboxes()


    def create_recipe_button(self, recipe, recipe_dict):
        name = self.model.get_name(recipe_dict)
        image_path = self.get_image_path(recipe)
        recipe_button = rb.RecipeButton()
        recipe_button.set_name(name)
        recipe_button.set_image(image_path)
        recipe_button.recipe = recipe
        recipe_button.add_cb(self.open_recipe)
        return recipe_button


    def read_recipes(self):
        self.recipes = self.model.get_recipes()
        self.categories = []
        self.nahrung = []
        self.kohlehydrate = []
        for r in self.recipes:
            rd = self.model.get_recipe_dict(r)
            self.categories = self.categories + self.model.get_kategorien(rd)
            self.nahrung = self.nahrung + self.model.get_nahrung(rd)
            self.kohlehydrate = self.kohlehydrate + self.model.get_kohlehydrat(rd)
            self.window.add_recipe(self.create_recipe_button(r, rd))
        self.categories = sorted(set(self.categories))
        self.nahrung = sorted(set(self.nahrung))
        self.kohlehydrate = sorted(set(self.kohlehydrate))
        self.label_filter = self.categories + self.nahrung + self.kohlehydrate


    def show_button(self, recipe_dict):
        show = False
        for c in self.model.get_kategorien(recipe_dict):
            if c in self.label_filter:
                show = True
        if show:
            show = False
            for n in self.model.get_nahrung(recipe_dict):
                if n in self.label_filter:
                    show = True
        if show:
            show = False
            for kh in self.model.get_kohlehydrat(recipe_dict):
                if kh in self.label_filter:
                    show = True
        return show


    def filter_recipes(self):
        buttons = self.window.get_recipe_buttons()
        for b in buttons:
            rd = self.model.get_recipe_dict(b.recipe)
            b.setHidden(not self.show_button(rd))


    def filter_label(self, state, label):
        if QtCore.Qt.Checked == state:
            if label not in self.label_filter:
                self.label_filter.append(label)
        else:
            if label in self.label_filter:
                self.label_filter.remove(label)
        self.filter_recipes()


    def create_checkbox(self, label):
        cb = QCheckBox(label.split('_')[1])
        cb.categorie = label
        if label in self.label_filter:
            cb.setChecked(True)
        cb.stateChanged.connect(lambda s, l=label: self.filter_label(s, l))
        return cb


    def clear_checkboxes(self):
        helper.clear_layout(self.window.kategorieGroupBox.layout())
        helper.clear_layout(self.window.nahrungGroupBox.layout())
        helper.clear_layout(self.window.kohlehydrateGroupBox.layout())


    def create_checkboxes(self):
        self.clear_checkboxes()
        for c in self.categories:
            self.window.kategorieGroupBox.layout().addWidget(self.create_checkbox(c))
        for n in self.nahrung:
            self.window.nahrungGroupBox.layout().addWidget(self.create_checkbox(n))
        for k in self.kohlehydrate:
            self.window.kohlehydrateGroupBox.layout().addWidget(self.create_checkbox(k))


    def get_image_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/thumb.jpg"


    def open_recipe(self, recipe):
        self.recipe = recipe
        self.rv_controller.load_recipe(recipe)


    def open_confirmation_dialog(self):
        dlg = QMessageBox(self.window)
        dlg.setWindowTitle("Rezept löschen?")
        dlg.setText("Soll das Rezept wirklich gelöscht werden?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec_()

        if button == QMessageBox.Yes:
            self.delete_recipe()
        

    def delete_recipe(self):
        self.model.delete_recipe(self.recipe)
        self.window.delete_recipe_buttons()
        self.window.stackedWidget.setCurrentIndex(0)
        self.load_recipes()


    def edit_recipe(self):
        self.re_controller.prepare_edit(self.recipe, self.categories,
                self.nahrung, self.kohlehydrate)
        self.window.stackedWidget.setCurrentIndex(2)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)


    def create_new_recipe(self):
        self.re_controller.prepare_new(self.categories, self.nahrung, self.kohlehydrate)
        self.window.stackedWidget.setCurrentIndex(2)


    def save_recipe(self):
        if self.re_controller.save_recipe():
            self.window.delete_recipe_buttons()
            self.window.stackedWidget.setCurrentIndex(0)
            self.load_recipes()
