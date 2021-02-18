from django.shortcuts import redirect


def admin_access(get_response):
    def middleware(request):
        user = request.user
        path = request.path

        if 'admin' in path:
            if user.is_authenticated:
                if not user.is_superuser:
                    return redirect('public_index')
            elif 'login' not in path:
                return redirect('admin_login')
        return get_response(request)
    return middleware