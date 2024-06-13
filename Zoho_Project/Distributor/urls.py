from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('Distributor_Dashboard',views.distributor_dashboard,name='distributor_dashboard'),
    path('Dist_clients',views.dist_clients,name='dist_clients'),
    path('Dist_Client_Requests',views.dist_client_requests,name='dist_client_requests'),
    path('Dist_Client_Accept/<int:id>',views.dist_client_accept,name='dist_client_accept'),
    path('Dist_Client_Reject/<int:id>',views.dist_client_reject,name='dist_client_reject'),
    path('Dist_Client_Request_Overview/<int:id>',views.dist_client_request_overview,name='dist_client_request_overview'),
    path('Dist_All_Clients',views.dist_all_clients,name='dist_all_clients'),
    path('Dist_Client_Details/<int:id>',views.dist_client_details,name='dist_client_details'),
    path('Distributor_Profile',views.distributor_profile,name='distributor_profile'),
    path('Dist_Edit_ProfilePage/<int:id>',views.dist_edit_profilePage,name='dist_edit_profilePage'),
    path('Update_Distributor_Profile/<int:id>',views.update_distributor_profile,name='update_distributor_profile'),
    path('Distributor/Password_Change',views.distributor_password_change,name='distributor_password_change'),

    # notifications------------------------------------

    path('Distributor_Notification',views.distributor_notification,name='distributor_notification'),
    path('Dist_Module_Updation_Details/<int:mid>',views.dist_module_updation_details,name='dist_module_updation_details'),
    path('Dist_Module_Updation_Ok/<int:mid>',views.dist_module_updation_ok,name='dist_module_updation_ok'),
    path('Paymentterms/Updation_Details/<int:pk>',views.paymentterm_updation_details,name='paymentterm_updation_details'),
    path('Paymentterm/Updation_Ok/<int:pk>',views.paymentterm_updation_ok,name='paymentterm_updation_ok'),
    path('Dist_Term_Update_Request',views.dist_term_update_request,name='dist_term_update_request'),
    path('Client/Trial_Period/Details',views.trial_periodclients,name='trial_periodclients'),
    path('Distributor/messages/read/<int:pk>',views.distributor_message_read,name='distributor_message_read'),
    path('Distributor/Payment_history',views.distributor_payment_history,name='distributor_payment_history'),


   
  
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)