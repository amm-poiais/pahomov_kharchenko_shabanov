from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateDictionaryView,  UserDetail, CreateUserView
from .views import DetailsDictionaryView


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^words/$', CreateDictionaryView.as_view(), name="create"),
    url(r'^word/(?P<pk>[0-9]+)/$', DetailsDictionaryView.as_view(), name="details"),
#    url(r'^user/$', UserCreateView.as_view(), name="create"),
#    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="details"),
    url(r'^user/words/$', UserDetail.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token),
    url(r'^register/$', CreateUserView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)
