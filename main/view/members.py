# views.py

from django.shortcuts import render,redirect, get_object_or_404
from django.core.exceptions import ValidationError
from main.models import  Recharge  # assuming custom User model
from accounts.models import User  # assuming custom User model

def member_list(request):
    members = User.objects.filter(is_customer=True)
    member_data = []

    for user in members:
        recharge = Recharge.objects.filter(user=user).order_by('-recharge_time').first()
        member_data.append({
            'user': user,
            'recharge_time': recharge.recharge_time if recharge else None,
            'valid_till': recharge.valid_till if recharge else None
        })

    return render(request, 'members/member_list.html', {'members': member_data})

def add_recharge(request, user_id):
    user = get_object_or_404(User, id=user_id, is_customer=True)

    if request.method == 'POST':
        validity_days = request.POST.get('validity_days', 30)  # default to 30 days
        recharge = Recharge(user=user, validity_days=validity_days)
        
        try:
            recharge.full_clean()  # run model validations
            recharge.save()
            return redirect('customer_list')
        except ValidationError as e:
            return render(request, 'members/recharge_form.html', {
                'user': user,
                'errors': e.message_dict,
                'title': '➕ Add Recharge'
            })

    return render(request, 'members/recharge_form.html', {'user': user, 'title': '➕ Add Recharge'})


# views.py



def add_member(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(
            username=username,
            email=email,
            is_customer=True,
            is_staff=False,
            is_superuser=False,
        )
        if password:
            user.set_password(password)

        try:
            user.full_clean()  # run model validations
            user.save()
            
            return redirect('customer_list')
        except ValidationError as e:
            return render(request, 'members/customer_form.html', {
                'errors': e.message_dict,
                'title': '➕ Add Member'
            })

    return render(request, 'members/admin.html', {'title': '➕ Add Member'})



def edit_member(request, user_id):
    user = get_object_or_404(User, id=user_id, is_customer=True)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        password = request.POST.get('password')

        if password:
            user.set_password(password)

        try:
            user.full_clean()
            user.save()
            return redirect('customer_list')
        except ValidationError as e:
            return render(request, 'members/customer_form.html', {
                'user': user,
                'errors': e.message_dict,
                'title': '✏️ Edit Member'
            })

    return render(request, 'members/admin.html', {
        'user': user,
        'title': '✏️ Edit Member'
    })
