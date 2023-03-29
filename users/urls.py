from django.urls import path, include
from django.contrib.auth.views import LoginView

from users.views import registration
from users.views import personal_account
from users.views import profile_form


urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', view=registration, name="registration"),
    path('personal-account/', view=personal_account, name="personal_account"),
    path('profile/', view=profile_form, name="profile_form"),
]
