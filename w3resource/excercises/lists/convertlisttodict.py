color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
dict_con = {}

# 'color_name': 'Black', 'color_code': '#000000'


print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])