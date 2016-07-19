from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import polls.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', polls.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls'))
]
