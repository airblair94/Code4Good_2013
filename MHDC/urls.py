from django.conf.urls import patterns, include, url

from views import *
from views_blair import *
from views_stephen import *
from views_brandon import *
from views_casey import *
from views_josh import *
from views_james import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     (r'^$', homepage),
     (r'^home/?$', homepage),
     (r'^home_repair_app/?$', home_repair_application),    
     (r'^register_user/?$', register_user),
     (r'^new_app/?$', new_application),
     (r'^self_help_app/?$', self_help_application),
     (r'^user_login/?$', user_login),
     (r'^user_logout/?$', user_logout),
     (r'^user_app/?$', view_my_applications),
     (r'^self_help_app/(?P<app_id>\d+)/?$', self_help_view),
     (r'^home_repair_app/(?P<app_id>\d+)/?$', home_repair_view),
     (r'^welcome/?$', general_welcome),
     (r'^stats/?$', analysis),
     (r'^self_help_client_check/?$', get_document_checklist),
     (r'^self_help_staff_check/?$', get_self_help_staff_checklist),
     (r'^repair_client_check/?$', get_repair_checklist),
     (r'^repair_staff_check/?$', get_repair_internal_checklist),
     (r'^comp_app/?$', view_completed_applications),
     (r'^search/?$', search),
     (r'^account_info/?$', account_info_view),

   # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
