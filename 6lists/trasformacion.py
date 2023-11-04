variable = "12/31/20"
date = variable.split("/")
date_day_month_year = [date[1], date[0], date[-1]]
print("-".join(date_day_month_year))

