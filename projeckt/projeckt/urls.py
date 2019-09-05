"""projeckt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from plab.views import ProfileList, ProfileCreate, ProfileView, ProfileUpdate, ProfileDelete, HomePageView, RegisterPageView, FormPageView, registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProfileList.as_view(), name='profile_list'),
    path('new', ProfileCreate.as_view(), name='profile_new'),
    path('view/<int:pk>', ProfileView.as_view(), name='profile_view'),
    path('edit/<int:pk>', ProfileUpdate.as_view(), name='profile_edit'),
    path('delete/<int:pk>', ProfileDelete.as_view(), name='profile_delete'),
    path('home', HomePageView.as_view(), name='index'),
    url(r'^register/$', RegisterPageView.as_view(), name='register'),
    url(r'^form/$', FormPageView.as_view(), name='form'),
    url(r'^registration1/$', registration, name='register'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
