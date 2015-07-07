from django.shortcuts import render
from poppy_humanoid import PoppyHumanoid

import time, os

#~ hasPoppy = False

#~ if hasPoppy:
    #~ try:
        #~ poppy = PoppyHumanoid()
        #~ time.sleep(0.1)
    #~ except Exception,e:
            #~ print "could not create poppy object"
            #~ print e
    
#~ def index(request):
    #~ context = {}
    #~ context['other'] = request.POST
    
    


    #~ if 'compliant' in request.POST.keys():
        #~ if hasPoppy:
            #~ #poppy.compliant =True
            #~ context['other'] = poppy.r_ankle_y.present_position
            #~ time.sleep(0.1)

    #~ if 'notCompliant' in request.POST.keys():
        #~ if hasPoppy:
            #~ poppy.compliant = False
            #~ time.sleep(0.1)

    #~ if  'speak' in request.POST.keys():
        #~ os.system('picospeaker -l "fr-FR" "Bonjour je suis poppy"')

    #~ return render(request, 'poppy_main_controls/index.html',context )
    
class PoppyMainController:
    def __init__(self, hasPoppy=True):
        self.hasPoppy = hasPoppy
        self.snapStarted = False
        self.notebookStarted = False
        
        self.context = {}
        self.context['notebookButton'] = "Start"
        self.context['notebookText'] = ""
        
    def index(self, request):
        self.context['other'] = request.POST
        if  'speak' in request.POST.keys() :
            if len(request.POST["toSay"]) == 0:
                self.context["speakerror"] = "Enter some text first!"
            else:
                self.context["speakerror"] = request.POST["toSay"]
                try:
                    os.system('picospeaker -l "fr-FR" "'+request.POST["toSay"]+'"')
                except:
                    print "error: could not use TTS"
                    
        #~ if 'notebook' in request.POST.keys() :
            #~ try:
                #~ os.system('ipython notebook --ip 0.0.0.0 --no-mathjax --no-browser')
            #~ except:
                #~ print "error: could not start ipython server"       
            #~ self.context['notebookButton'] = "Stop"
            #~ self.context['notebookText'] = 'Now open <a href="http://poppy.local:8888/notebooks/dev/poppy-humanoid/software/notebooks/TTFX.ipynb">http://poppy.local:8888/notebooks/dev/poppy-humanoid/software/notebooks/TTFX.ipynb <\a>'
        return render(request, 'poppy_main_controls/index.html',self.context )
        
        
poppyMainController = PoppyMainController()
        
        