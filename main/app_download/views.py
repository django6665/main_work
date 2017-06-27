from django.shortcuts import render
from .models import File_model
import datetime
import os
from main.settings import MEDIA_ROOT
import sys
sys.path.append('/home/django6665/main/script_py')
import my_main
# Create your views here.
# def home(request):
#     content={
#         "request":request,
#         'dir_request':dir(request),
#         }
#     return render(request,"index.html",content)


from django.shortcuts import redirect

def create(request):
    if request.method == 'POST':
        a=[request.FILES,"\n",request.FILES.getlist("w",[])]
        for i in request.FILES.getlist("w",[]):
            save_models=File_model(
                xlsx=i,
                storage=i,
                now=datetime.datetime.now())
            save_models.save()
            return redirect('http://django6665.pythonanywhere.com/')
    else:
        a=None
    model_eighth=File_model.objects.filter(id=8)[0]
    content={
        "file":a,
        "model":File_model.objects.all(),
        "model_eighth":model_eighth,
        }
    return render(request,"create.html",content)

def home(request):
    #three act:
    #first: save file
    #second: del file
    #third: get file
    #
    #first:
    if request.method == 'POST':
        if request.POST.get('submit_file', default=None)!=None:
        # a=[request.FILES,"\n",request.FILES.getlist("w",[])]
            for i in request.FILES.getlist("w",[]):
                save_models=File_model(
                    xlsx=i,
                    storage=i,
                    now=datetime.datetime.now())
                save_models.save()
                # no redirect because request.FILES.getlist("w",[])
    #end first
    #main
    storage_dir=os.listdir(os.path.join(MEDIA_ROOT,'storage'))
    stragare_len=range(len(storage_dir))
    storage_zip_list=list(zip(storage_dir,stragare_len))
    storage_zip_dict=dict((zip(stragare_len,storage_dir)))#nomber:file_name -in storage_zip_list[n].1
    #end main
    #second
    if request.method=="POST" and request.POST.get('submit_file', default=None)==None:
            if request.POST.get("submit_del", default=None)=='Удалить выбранные?':
                file_path_del=[]
                if request.POST.get("delete_all",None)!=None:
                    for i in storage_zip_dict.values():
                        file_path_del.append(os.path.join(MEDIA_ROOT,'storage')+"/"+i) #!important list with /home/xxx/x/x/storage/x.png
                    for i in file_path_del:
                        os.system("rm {i}".format(i=i))
                    return redirect('http://django6665.pythonanywhere.com/')
                else:
                    for i in request.POST.getlist("delete",[]):
                        file_name=storage_zip_dict[int(i)]
                        file_path_del.append(os.path.join(MEDIA_ROOT,'storage')+"/"+file_name) #!important list with /home/xxx/x/x/storage/x.png
                        for i in file_path_del:
                            os.system("rm \"{i}\"".format(i=i))
                    return redirect('http://django6665.pythonanywhere.com/')
    #end second
    #third:
    def file_read():
        file_main_list=[]
        for i in storage_zip_dict.values():
            file_main_list.append(os.path.join(MEDIA_ROOT,'storage')+"/"+i)
        for i in file_main_list:
            if (i.endswith('.xlsx')
            and not i.endswith("main.xlsx")
            ):
                try:
                    my_main.main(i,path=os.path.join(MEDIA_ROOT,'storage'),week=str(request.POST.get("week","25")))
                except:
                    return i
        return "OK all file"
    if request.method=="POST" and request.POST.get('go', default=None)=="start":
        status_file=file_read()
        return redirect('http://django6665.pythonanywhere.com/?status='+status_file+"&"+str(request.POST.get("week","25")))
    #end third
    content={
        "status_file":request.GET.get("status","Status None"),
        'storage_zip_list':storage_zip_list,
        "file_save":request.FILES.getlist("w",[]),
        }
    return render(request,"home.html",content)