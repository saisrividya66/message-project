from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
# Create your views here.
def create(request):
    if request.method=="POST":
        n=request.POST['name']
        mail=request.POST['email']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)    
        m.save()
            #print(n,"-",mail,"-",mob,"-",msg,"-")
        #return HttpResponse("Data inerted SUCCESS")
        return redirect('/dashboard')
        pass 

          
    else: 
         #print("request is:",request.method)
         return render(request,'create.html')
         
   
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
      #return HttpResponse("success")  

def delete(request,rid):
    #print("id to be deleted:",rid)
    m=Msg.object.filter(id=rid)
    m.delete()
    return redirect('\dashboard')
    #return HttpResponse("id to be deleted"+rid)

def edit(request,rid):
    if request.method=='POST':
        n=request.POST['name']
        mail=request.POST['email']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        #print(n)
        #print(mail)
        m=Msg.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=mob,msg=msg)
        return redirect('/dashboard')

    #print("id to be deleted:",rid)
    else:
         m=Msg.objects.get(id=rid)
         context={}
         context['data']=m
         return render(request,'edit.html',context)

   
    #return HttpResponse("id to be deleted"+rid)