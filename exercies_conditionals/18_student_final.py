def final_grade(grade_exam, num_projects):
    if grade_exam > 90 or num_projects > 10:
        return f"{grade_exam}, {num_projects} --> {100}"
    elif grade_exam > 75 and num_projects >= 5:
        return f"{grade_exam}, {num_projects} --> {90}"
    elif grade_exam > 50 and num_projects >= 2:
        return f"{grade_exam}, {num_projects} --> {75}"
    else:
        return f"{grade_exam}, {num_projects} --> {0}"
