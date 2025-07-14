from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def staff_required(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'role') and request.user.role == 'staff':
            return view_func(request, *args, **kwargs)
        return redirect('no_permission')
    return wrapper
