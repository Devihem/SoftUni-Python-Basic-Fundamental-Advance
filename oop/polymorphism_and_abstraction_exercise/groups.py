class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return __class__(self.name, other.surname)

    def __repr__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return __class__(f'{self.name} {other.name}', self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(people) for people in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"
