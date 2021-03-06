from django.contrib import admin
# from django.conf.urls import include,path,url
from django.urls import include,path
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),  
    
    path('accounts/register/',RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include ('user.urls')),
    

]
