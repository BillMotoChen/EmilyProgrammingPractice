# already used functions with outputs
length = len(formatted_name)

# returns as an early exit
def format_name(f_name, l_name):
    """Take a first and last name. Format it to return the title case version of tyhe name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"