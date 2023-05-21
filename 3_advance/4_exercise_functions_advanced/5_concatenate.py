def concatenate(*args, **kwargs):
    final_text = ''
    for string in args:
        final_text += string

    for key in kwargs.keys():
        if key in final_text:
            final_text = final_text.replace(key, kwargs[key])

    return final_text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
