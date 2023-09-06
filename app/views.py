from django.shortcuts import render
from .models import visitermodel
from datetime import datetime
from rest_framework import viewsets
from .serializer import visiterserializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        query=request.POST.get("query")
        obj=visitermodel(name=name,email=email,phone=phone,query=query,date=datetime.now()) 
        obj.save()      
    return render(request,"self.html")

def visiter(request):
    data=visitermodel.objects.all()
    return render(request,"visiterdetail.html",{'data':data})


class visiterviewset(viewsets.ModelViewSet):
    queryset=visitermodel.objects.all()
    serializer_class=visiterserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
    


