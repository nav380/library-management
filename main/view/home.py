from django.shortcuts import render,redirect

def home(request):
    try:
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, 'home/adminhome.html')
            elif request.user.is_customer:
                return render(request, 'home/home.html')
        else:
            return render(request, 'error.html', {'error': 'User is not authenticated'})
    except Exception as e:
        print(f"Error: {e}")
        
        return redirect('login')
