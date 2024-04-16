import datetime


def year(request):
    dt = datetime.date.today()
    return {'year': dt.year, }
