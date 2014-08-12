from django.conf.urls import url, patterns 

from projectname import views

urlpatterns = patterns('',
        url(r'^$', views.ProjectnameListView.as_view(), name=r'projectname-list'),
        url(r'^(?P<pk>\d+)/$', views.ProjectnameDetailView.as_view(), name='projectname-detail'),
        url(r'^create/$', views.ProjectnameCreateView.as_view(), name='projectname-create'),
        url(r'^(?P<pk>\d+)/delete$', views.ProjectnameDeleteView.as_view(), name='projectname-delete'),
        url(r'^(?P<pk>\d+)/edit$', views.ProjectnameUpdateView.as_view(), name='projectname-edit'),
        )
