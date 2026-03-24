# This is how I did it
#def format_name(f_name,l_name):
    #print(f_name.capitalize())
    #print(l_name.capitalize())

# This is a way with .title()
def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_str = (format_name("ANGELA", "yU"))
print(formated_str)

