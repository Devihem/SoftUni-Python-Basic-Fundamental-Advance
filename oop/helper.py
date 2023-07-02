# @staticmethod
def find_object(item: str, attribute: str, collection: list):
    for obj in collection:
        if getattr(obj, attribute) == item:
            return obj
