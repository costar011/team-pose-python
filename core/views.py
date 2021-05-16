from django.shortcuts import render
from members.models import MemberModel as Mem


def renderHome(request):

    all_members = Mem.objects.all()

    return render(request, "screens/home.html", context={"members": all_members})
