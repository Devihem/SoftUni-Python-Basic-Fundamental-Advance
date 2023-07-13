
class Cat:
    def __init__(self, name):

        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):

        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTest(TestCase):
    def test_cat_size_increase_after_eating(self):
        # Arrange
        cat = Cat("Nekomamushi")

        # Base_Asset
        self.assertEqual(0, cat.size)

        # Act
        cat.eat()

        # Asset
        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        # Arrange
        cat = Cat("Nekomamushi")
        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_cat_is_fed_after_eating_raise_error(self):
        # Arrange
        cat = Cat("Nekomamushi")
        cat.eat()
        self.assertEqual(True, cat.fed)

        with self.assertRaises(Exception) as excp:
            cat.eat()
        self.assertEqual('Already fed.', str(excp.exception))

    def test_cat_cannot_go_to_sleep_without_food_raise_error(self):
        # Arrange
        cat = Cat("Nekomamushi")

        with self.assertRaises(Exception) as excp:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(excp.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        cat = Cat("Nekomamushi")
        cat.eat()
        cat.sleep()

        self.assertEqual(False, cat.sleepy)


if __name__ == "__main__":
    main()
