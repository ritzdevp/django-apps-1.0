from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Hit me up at, ', 'rtjsingh30@gmail.com','rituraj_bt2k16@dtu.ac.in']})
