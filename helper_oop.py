

# CHECKING FOR WHITESPACES

@property
def SOMETHING(self):
    return self.__SOMETHING


@manufacturer.setter
def SOMETHING(self, value):
    if not value.strip():
        raise ValueError("SOMETHING name cannot be empty.")
    self.__SOMETHING = value