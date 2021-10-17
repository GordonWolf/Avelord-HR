from datetime import datetime

class Calendar():

    def __init__(self, id, user, datetime, month, year, check) -> None:
        self.id = id
        self.user = user
        self.datetime = datetime
        self.month = month
        self.year = year
        self.check = check