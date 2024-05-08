from kerykeion import Report, AstrologicalSubject

eunice = AstrologicalSubject("eunice", 2003, 2, 18, 13, 28, "Singapore")
report = Report(eunice)
report.print_report()

eunice.sun
eunice.first_house
eunice.moon.element

