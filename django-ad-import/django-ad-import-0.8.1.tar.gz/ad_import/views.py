from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from ad_import.models import User


@permission_required('ad_import.view_user', raise_exception=True)
def view_user(request):
    user_id = request.GET.get('id')
    user = User.objects.get(id=user_id)
    return render(request, 'ad_import/user.html', {'user': user})
