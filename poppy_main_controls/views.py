from django.shortcuts import render
from poppy_humanoid import PoppyHumanoid

import time

hasPoppy = True

if hasPoppy:
    try:
        poppy = PoppyHumanoid()
        time.sleep(0.1)
    except Exception,e:
            print "could not create poppy object"
            print e
    
def index(request):
    context = {}
    context['other'] = request.POST
    
    


    if 'compliant' in request.POST.keys():
        if hasPoppy:
            #poppy.compliant =True
            context['other'] = poppy.r_ankle_y.present_position
            time.sleep(0.1)

    if 'notCompliant' in request.POST.keys():
        if hasPoppy:
            poppy.compliant = False
            time.sleep(0.1)

    return render(request, 'poppy_main_controls/index.html',context )