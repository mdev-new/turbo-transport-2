from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# todo handle post
def login(req):
    return render(req, 'personal/login.html')


def register(req):
    if req.method != "POST":
        return HttpResponse("Not a post request!", status_code=403)
    pass


def logout(req):
    # Todo logout logic
    return render(req, '_success.html')


def last_searches(req):
    context = {
        # Todo pull this from db
        'searches': enumerate([
            'Strossova - Namesti republiky',
            'Hlavni nadrazi - Nem.'
        ])
    }
    return render(req, 'personal/_last_searches.html', context)


def session_controls(req):
    context = {
        'user': 'mdev'
    }
    return render(req, 'personal/_session_controls.html', context)
