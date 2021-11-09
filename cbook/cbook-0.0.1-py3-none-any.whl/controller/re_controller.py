import os
from cbook.model import helper, recipe_parser
from os.path import split
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class ReController:
    image = ""
    edit = False


    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.window.buttonAddIngredient.clicked.connect(self.add_ingredient_row)
        self.window.buttonDeleteIngredient.clicked.connect(self.delete_ingredient_row)
        self.window.loadImageButton.clicked.connect(self.open_select_image)
        self.window.deleteImageButton.clicked.connect(self.delete_image)
        self.window.comboBoxKategorien.activated.connect(self.activated_kategorien)
        self.window.comboBoxNahrung.activated.connect(self.activated_nahrung)
        self.window.comboBoxKohlenhydrate.activated.connect(self.activated_kohlenhydrate)
        self.window.buttonClearKategorien.clicked.connect(self.clear_categories)
        self.window.buttonClearNahrung.clicked.connect(self.clear_nahrung)
        self.window.buttonClearKohlenhydrate.clicked.connect(self.clear_kohlenhydrate)
        self.window.buttonReload.clicked.connect(self.reload)


    def reload(self):
        self.fill_data(self.recipe)


    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.window.imageLabelEdit.setPixmap(pixmap)


    def remove_prefix(self, labels):
        ret = []
        for l in labels:
            ret.append(l.split('_')[1])
        return ret


    def prepare_labels(self, categories, nahrungs, kohlehydrate):
        categories = self.remove_prefix(categories)
        nahrungs = self.remove_prefix(nahrungs)
        kohlehydrate = self.remove_prefix(kohlehydrate)
        self.window.comboBoxKategorien.clear()
        self.window.comboBoxKategorien.addItems(categories)
        self.window.comboBoxNahrung.clear()
        self.window.comboBoxNahrung.addItems(nahrungs)
        self.window.comboBoxKohlenhydrate.clear()
        self.window.comboBoxKohlenhydrate.addItems(kohlehydrate)


    def prepare_new(self, categories, nahrungs, kohlehydrate):
        self.edit = False
        self.prepare_labels(categories, nahrungs, kohlehydrate)
        self.window.nameLineEdit.setText("")
        self.window.zutatenTableWidget.setRowCount(1)
        self.window.zutatenTableWidget.clearContents()
        self.set_image(self.window.get_default_meal_image_path())
        self.window.spinBoxPortionenEdit.setValue(4)
        self.window.buttonReload.setHidden(True)
        self.clear_categories()
        self.clear_kohlenhydrate()
        self.clear_nahrung()
        self.window.textEditAnleitung.setText("")
        self.window.textEditBeschreibung.setText("")


    def fill_ingredients_table(self, ingredients):
        tableWidget = self.window.zutatenTableWidget
        tableWidget.setRowCount(len(ingredients))
        index = 0
        for i in ingredients:
            if len(i.split(';')) >= 3:
                item = QtWidgets.QTableWidgetItem(i.split(';')[0])
                tableWidget.setItem(index, 0, item)
                item = QtWidgets.QTableWidgetItem(i.split(';')[1])
                tableWidget.setItem(index, 1, item)
                item = QtWidgets.QTableWidgetItem(i.split(';')[2])
                tableWidget.setItem(index, 2, item)
            elif len(i.split(' ')) >= 3:
                item = QtWidgets.QTableWidgetItem(i.split(' ')[0])
                tableWidget.setItem(index, 0, item)
                item = QtWidgets.QTableWidgetItem(i.split(' ')[1])
                tableWidget.setItem(index, 1, item)
                ing = ""
                for e in i.split(' ')[2:]:
                    ing = ing + e + " "
                item = QtWidgets.QTableWidgetItem(ing[:-1])
                tableWidget.setItem(index, 2, item)
            index = index + 1


    def fill_data(self, recipe):
        rd = self.model.get_recipe_dict(recipe)
        self.window.nameLineEdit.setText(self.model.get_name(rd))
        self.set_image(os.path.dirname(recipe) + "/full.jpg")
        self.window.spinBoxPortionenEdit.setValue(self.model.get_servings(rd))
        instructions = self.model.get_instructions(rd)
        text = ""
        for i in instructions:
            text = text + i + "\n\n"
        self.window.textEditAnleitung.setText(text)
        self.window.textEditBeschreibung.setText(self.model.get_description(rd))
        k = self.model.get_kategorien(rd)
        n = self.model.get_nahrung(rd)
        kh = self.model.get_kohlehydrat(rd)
        self.window.labelKategorienEdit.setText(helper.get_label_string(k))
        self.window.labelNahrungEdit.setText(helper.get_label_string(n))
        self.window.labelKohlenhydrateEdit.setText(helper.get_label_string(kh))
        self.fill_ingredients_table(self.model.get_ingredients(rd))


    def prepare_edit(self, recipe, categories, nahrungs, kohlehydrate):
        self.edit = True
        self.recipe = recipe
        self.prepare_labels(categories, nahrungs, kohlehydrate)
        self.fill_data(recipe)


    def add_ingredient_row(self):
        tableWidget = self.window.zutatenTableWidget
        tableWidget.insertRow(tableWidget.rowCount())


    def delete_ingredient_row(self):
        tableWidget = self.window.zutatenTableWidget
        tableWidget.removeRow(tableWidget.rowCount()-1)


    def open_select_image(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, 
                'Öffne Bild', 
                '',
                "Image files (*.jpg *.gif *.png *.jpeg *.svg)")
        if fname:
            self.image = fname
            self.set_image(fname)


    def delete_image(self):
        self.image = ""
        self.set_image(self.window.get_default_meal_image_path())


    def activated_kategorien(self):
        selected = self.window.comboBoxKategorien.currentText()
        # add to list
        text = self.window.labelKategorienEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelKategorienEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxKategorien.clearEditText()


    def activated_nahrung(self):
        selected = self.window.comboBoxNahrung.currentText()
        # add to list
        text = self.window.labelNahrungEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelNahrungEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxNahrung.clearEditText()


    def activated_kohlenhydrate(self):
        selected = self.window.comboBoxKohlenhydrate.currentText()
        # add to list
        text = self.window.labelKohlenhydrateEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelKohlenhydrateEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxKohlenhydrate.clearEditText()


    def clear_categories(self):
        self.window.labelKategorienEdit.setText("")


    def clear_nahrung(self):
        self.window.labelNahrungEdit.setText("")


    def clear_kohlenhydrate(self):
        self.window.labelKohlenhydrateEdit.setText("")


    def get_ingredients(self):
        ingredients = []
        model = self.window.zutatenTableWidget.model()
        for r in range(0,self.window.zutatenTableWidget.rowCount()):
            ingredient = []
            menge = model.data(model.index(r, 0))
            einheit = model.data(model.index(r, 1))
            zutat = model.data(model.index(r, 2))
            if menge or einheit or zutat:
                if menge:
                    try:
                        menge = helper.string_to_float(menge)
                    except:
                        QtWidgets.QMessageBox.critical(self.window, "Ungültige Mengenangabe",
                                "Ungültige Mengeneingabe '" + str(menge) + "'.\n" +
                                "Entweder als Dezimalzahl (z.B. '1.5')\n" +
                                "oder als Bruch (z.B. '1 1/2' oder '3/5') eingeben!")
                        return None
                else:
                    menge = ""
                if not einheit:
                    einheit = ""
                if not zutat:
                    QtWidgets.QMessageBox.critical(self.window, "Ungültige Zutatenangabe",
                            "Leeres Zutatenfeld!")
                    return None

                ingredients.append(str(menge) + " " + str(einheit) + " " + str(zutat))
            else:
                print("Skipped empty ingredient row")
        if not ingredients:
            QtWidgets.QMessageBox.critical(self.window, "Ungültige Zutaten",
                    "Keine Zutaten angegeben!")
        return ingredients


    def save_recipe(self):
        name = self.window.nameLineEdit.text()
        if self.edit or self.model.check_name(name):
            ingredients = self.get_ingredients()
            if ingredients:
                # read recipe data and save recipe
                portionen = self.window.spinBoxPortionenEdit.value()
                anleitung = self.window.textEditAnleitung.toPlainText()
                beschreibung = self.window.textEditBeschreibung.toPlainText()
                kategorien = self.window.labelKategorienEdit.text().split(', ')
                nahrung = self.window.labelNahrungEdit.text().split(', ')
                kohlenhydrate = self.window.labelKohlenhydrateEdit.text().split(', ')
                
                self.model.save_recipe(name, self.image, ingredients, portionen,
                        beschreibung, anleitung, kategorien, nahrung, kohlenhydrate)

                # prevent having two folders with the same recipe
                if self.edit:
                    rd = self.model.get_recipe_dict(self.recipe)
                    if name != self.model.get_name(rd):
                        self.model.delete_recipe(self.recipe)

            return True
        else:
            QtWidgets.QMessageBox.critical(self.window, "Ungültiger Rezeptname",
                    "Ein Rezept mit diesem Namen ist bereits vorhanden.\n" +
                    "Bitte wähle einen anderen Namen!")
            return False
