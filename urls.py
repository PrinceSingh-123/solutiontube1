from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from courses.views import CourseListView
from django.conf.urls import url

# applications
from home import views
# autocomplete url
from ebook.views import ebook_autocomplete

urlpatterns = [
    
    # Home page URLS
    path('',views.home),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('subscrption/',views.subscrption,name='subscrption'),
    path('khalti/',views.khalti,name='khalti'),
    path('covid/',views.covid,name='covid'),
    path('googlepay/',views.googlepay,name='googlepay'),
    path('legal/',views.legal,name='legal'),
    path('setting/',views.setting,name='setting'),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('course_list/', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),

    # Ebook URL
    path('ebook/', include('ebook.urls')),
    # Ebook URL forwarding
    url(r'^api/ebook-autocomplete/', ebook_autocomplete, name='ebook-autocomplete'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
