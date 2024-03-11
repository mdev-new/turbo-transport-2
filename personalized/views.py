from django.shortcuts import render


# Create your views here.

# todo handle post
def login(req):
    return render(req, 'personal/login.html')


def register(req):
    pass


def logout(req):
    # Todo logout logic
    return render(req, '_success.html')


def last_searches(req):
    context = {
        'searches': [
            'Strossova - Namesti republiky',
            'Hlavni nadrazi - Nem.'
        ]
    }
    return render(req, 'personal/_last_searches.html', context)


def session_controls(req):
    context = {
        'user': 'mdev'
    }
    return render(req, 'personal/_session_controls.html', context)
