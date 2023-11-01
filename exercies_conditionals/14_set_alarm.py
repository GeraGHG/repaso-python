def set_alarm(employed = True, vacation = True):
    if employed == False and vacation == True:
        return False
    if employed == False and vacation == False:
        return False
    return not(employed and vacation)

true_or_false = [(True, True), (True, False), (False, True), (False, False)]
title_emp = "employed |"
title_vac = "vacation "
str_true = "true"
str_false = "false"
print(title_emp, title_vac, sep=" ")
for tuple in true_or_false:
    elem1, elem2 = tuple
    resp = set_alarm(elem1, elem2)
    show_col1 = str_true if elem1 == True else str_false
    show_col2 = str_true if elem2 == True else str_false
    show_col3 = str_true if resp == True else str_false
    rest_col1 = len(title_emp) - (len(str_true) if elem1 == True else (len(str_false)))
    rest_col2 = len(title_vac) - ((len(str_true) if elem2 == True else (len(str_false))))

    print(show_col1 + (" " * rest_col1) + "| " + show_col2 + (" " * rest_col2) + "=> " + show_col3)

