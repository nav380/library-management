from django.shortcuts import render,redirect

def home(request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, 'home/adminhome.html')
            elif request.user.is_customer:
                return render(request, 'home/home.html')
        else:
            return redirect('login')
            
   



def dashboard(request):
    return render(request, 'main/dashboard.html')


def member_list(request):
    return render(request, 'main/member_list.html')

def borrow_book(request):
    return render(request, 'main/borrow.html')

def borrow_records(request):
    return render(request, 'main/borrow_records.html')

def returns(request):
    return render(request, 'main/returns.html')

def categories(request):
    return render(request, 'main/categories.html')


