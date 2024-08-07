from django.urls import path
from .views import (
    home,
    login_view,
    logout_view,
    register,
    admin_dashboard,
    add_lawyer,
    lawyer_dashboard,
    client_dashboard,
    book_appointment,
    lawyer_appointments,
    client_appointments,
    lawyer_list,
    client_list,
    appointment_list,
    delete_appointment,
    contact,
    about,
    complete_appointment,
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
     path('add-lawyer/', add_lawyer, name='add_lawyer'),
    path('lawyer/dashboard/', lawyer_dashboard, name='lawyer_dashboard'),
    path('client/dashboard/', client_dashboard, name='client_dashboard'),
    path('appointments/book/', book_appointment, name='book_appointment'),
#    path('lawyer/<int:lawyer_id>/appointments/', lawyer_appointments, name='lawyer_appointments'),
     path('lawyer/appointments/',lawyer_appointments, name='lawyer_appointments'),

    path('client/appointments/', client_appointments, name='client_appointments'),
    path('lawyers/', lawyer_list, name='lawyer_list'),
    path('clients/', client_list, name='client_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('appointments/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('appointments/delete/<int:id>/', delete_appointment, name='delete_appointment'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('complete_appointment/<int:appointment_id>/', complete_appointment, name='complete_appointment'),

]






