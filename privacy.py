import re

def remove_names(name, text):
    """
    Removes all names from a given text using regular expressions.
    """
    names = name.split(" ")
    if len(names) <= 0 or names[0] == "":
        return text
    for name1 in names:
        pattern = r"\b" + re.escape(name1) + r"\b"
        # Use the sub() method of the re module to replace all matches of the pattern with an empty string
        text = re.sub(pattern, "John", text)

    return text
