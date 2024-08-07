from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, LoginForm, AppointmentForm, AdminLawyerCreationForm
from .models import CustomUser, Appointment, Client, Lawyer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import AdminLawyerCreationForm  # Ensure this form is defined correctly
from .models import Lawyer  # Import your Lawyer model
from django.contrib.auth.decorators import login_required  # Make sure to import this
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm




def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def add_lawyer(request):
    return render(request, 'add_lawyer.html')

def appointment_list(request):
    return render(request, 'appointment_list.html')

@login_required
def admin_dashboard(request):
    # Only allow access if the user is a superuser
    if not request.user.is_superuser:
        return redirect('login')  # Redirect to login if not superuser
    return render(request, 'admin_dashboard.html')

@login_required
def lawyer_dashboard(request):
    if request.user.is_authenticated:
        lawyer = Lawyer.objects.get(user=request.user)
        appointments = Appointment.objects.filter(lawyer=lawyer)  # Filter by the lawyer
        return render(request, 'lawyer_dashboard.html', {'appointments': appointments})
    else:
        return redirect('lawyer_login')  # Redirect if not logged in

@login_required
def client_dashboard(request):
    return render(request, 'client_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'client'  # Set user type to 'client' by default
            user.save()
            login(request, user)
            return redirect('login')  # Redirect to client dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                if user.is_superuser:
                    return redirect('admin_dashboard')
                elif user.user_type == 'lawyer':
                    return redirect('lawyer_dashboard')
                elif user.user_type == 'client':
                    return redirect('client_dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('home')


#new code 

@login_required
def add_lawyer(request):
    if request.user.is_superuser:  # Ensure the user is an admin
        if request.method == 'POST':
            form = AdminLawyerCreationForm(request.POST)
            if form.is_valid():
                # Create the user
                user = form.save(commit=False)
                user.user_type = 'lawyer'  # Set the user type to 'lawyer'
                user.set_password(form.cleaned_data['password'])  # Hash the password
                user.save()  # Save the user to the database

                # Create the Lawyer profile
                Lawyer.objects.create(
                    user=user,  # Associate the user with the lawyer
                    name=form.cleaned_data['name'],  # Ensure you get the name from the form
                    specialization=form.cleaned_data['specialization'],  # Get specialization
                )

                messages.success(request, 'Lawyer added successfully.')
                return redirect('admin_dashboard')  # Redirect to the admin dashboard
        else:
            form = AdminLawyerCreationForm()
        return render(request, 'add_lawyer.html', {'form': form})
    else:
        return redirect('home')  # Redirect non-admins

#ends here
# @login_required
# def book_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.client = Client.objects.get(user=request.user)  # Get the logged-in client
#             appointment.save()
#             messages.success(request, 'Appointment booked successfully.')
#             return redirect('client_dashboard')  # Redirect to a success page
#     else:
#         form = AppointmentForm()
#     return render(request, 'book_appointment.html', {'form': form})

@login_required  # Ensure this decorator is placed directly above the function
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user.client  # Ensure user has a related Client model
            appointment.save()
            return redirect('client_dashboard')  # Redirect to a success page
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})


#new code
from django.shortcuts import render, get_object_or_404
from .models import Lawyer, Appointment  # Make sure these imports are correct

@login_required
def lawyer_appointments(request):
    # Use get_object_or_404 to handle the case where the lawyer does not exist
    lawyer = get_object_or_404(Lawyer, user=request.user)

    # If you reach this point, the lawyer exists
    appointments = Appointment.objects.filter(lawyer=lawyer)

    return render(request, 'lawyer_appointments.html', {'appointments': appointments, 'lawyer': lawyer})
#ends here

@login_required
def client_appointments(request):
    client = get_object_or_404(Client, user=request.user)
    appointments = Appointment.objects.filter(client=client)
    return render(request, 'client_appointments.html', {'appointments': appointments})

def lawyer_list(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'lawyer_list.html', {'lawyers': lawyers})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})



from django.shortcuts import get_object_or_404, redirect
from .models import Appointment

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return redirect('lawyer_appointments')  # Redirect to the appointments page after deletion


from django.shortcuts import get_object_or_404, redirect
from .models import Appointment

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return redirect('client_appointments')  # Redirect to the appointments page after deletion
    




# views.py

from django.shortcuts import get_object_or_404, redirect
from .models import Appointment

def complete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Mark the appointment as completed
    appointment.completed = True  # Make sure you have a field named 'completed'
    appointment.save()

    return redirect('lawyer_dashboard')  # Redirect to the lawyer dashboard or appointments page




# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment

def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return redirect('appointment_list')  # Redirect to the appointments page after deletion
    



