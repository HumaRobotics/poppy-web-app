from django.shortcuts import render
from poppy_humanoid import PoppyHumanoid

hasPoppy = False


def index(request):
    context = {}
    context['other'] = request.POST
    
    
    if hasPoppy:
        poppy = PoppyHumanoid()
    
    if 'compliant' in request.POST.keys():
        if hasPoppy:
            poppy.compliant(True)
 
    if 'notCompliant' in request.POST.keys():
        if hasPoppy:
            poppy.compliant(False)

    return render(request, 'poppy_main_controls/index.html',context )