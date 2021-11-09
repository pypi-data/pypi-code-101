from cbook.config import config
from cbook.model import recipe_parser as rp


class CbModel:
    recipes = []
    label_no_c = "k_Keine Kategorie"
    label_no_n = "n_Kein Nahrungstyp"
    label_no_kh = "kh_Keine Kohlenhydrate"


    def load_recipes(self):
        self.recipes = rp.get_recipes(config.get_recipe_path())


    def get_recipes(self):
        return self.recipes


    def get_recipe_dict(self, recipe):
        return rp.read_recipe(recipe)


    def get_name(self, recipe):
        return rp.get_name(recipe)


    def get_instructions(self, recipe):
        return rp.get_instructions(recipe)
    

    def get_servings(self, recipe):
        return rp.get_servings(recipe)


    def get_label_list(self, recipe, label):
        keywords = rp.get_keywords(recipe).split(',')
        ret = []
        for k in keywords:
            if len(k) > len(label) and k[0:len(label)] == label:
                ret.append(k)
        return ret


    def get_kategorien(self, recipe):
        ret = self.get_label_list(recipe, 'k_')
        if len(ret) <= 0:
            ret.append(self.label_no_c)
        return ret


    def get_nahrung(self, recipe):
        ret = self.get_label_list(recipe, 'n_')
        if len(ret) <= 0:
            ret.append(self.label_no_n)
        return ret


    def get_kohlehydrat(self, recipe):
        ret = self.get_label_list(recipe, 'kh_')
        if len(ret) <= 0:
            ret.append(self.label_no_kh)
        return ret


    def get_ingredients(self, recipe):
        return rp.get_ingredients(recipe)


    def get_description(self, recipe):
        return rp.get_description(recipe)


    def check_name(self, name):
        for r in self.get_recipes():
            rd = self.get_recipe_dict(r)
            if name == rp.get_name(rd):
                return False
        return True


    def save_recipe(self, name, image, ingredients, servings, description,
            instructions, categories, nahrung, kohlenhydrate):
        print("Todo")
        rd = rp.create_recipe_dict(name, ingredients, servings, description,
                instructions, categories, nahrung, kohlenhydrate)
        rp.write_recipe(config.get_recipe_path(), rd, image)


    def delete_recipe(self, recipe):
        rp.delete_recipe(recipe)
