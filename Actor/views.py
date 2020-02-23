from django.shortcuts import render, redirect
from ticket_consert.CallBack import CallBack
# Create your views here.
from .forms import ActorForm
from .presenters.ActorPresenter import ActorPresenter


def get_all_actors(request):
    pass


def get_by_id_actor(request):
    pass


def delete_by_id_actor(request):
    cbClass = CallBack()
    if request.GET.get("id_actor"):
        id_actor = request.GET.get("id_actor")
        delete = ActorPresenter().delete_by_id_actor(id_actor)
        if delete:
            cbClass.message = "Delete Success"
            cbClass.status = 200
        return redirect("Actor:add_actor")


def edit_by_id_actor(request):
    cbClass = CallBack()
    if request.GET.get("id_edit"):
        id_edit = request.GET.get("id_edit")
        editInfo = ActorPresenter().find_actor_by_id_actor(id_edit)
        cbClass.forms = ActorForm(request.POST or None, instance=editInfo)
    if request.GET.get("id_edit") and request.method == "PUT":
        cbClass.forms.save()
    return render(request, "edit_actor.html", cbClass.get_dict())


def add_actor(request):
    try:
        forms = ActorForm(request.POST or None)
        cbClass = CallBack(forms=forms)
        cbClass.datas = ActorPresenter().find_actor_all()
        if request.method == "POST" and forms.is_valid():
            forms.save()
        return render(request, "actor.html", cbClass.get_dict())
    except Exception as e:
        return render(request, "err.html", CallBack(e, 500, []).get_dict())
