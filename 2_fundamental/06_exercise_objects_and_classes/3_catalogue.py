class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_list = list(filter(lambda item: item[0] == first_letter, self.products))
        return filtered_list

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted(self.products))


# Test Code:

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
