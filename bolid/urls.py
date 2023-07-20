from rest_framework import routers

from bolid import views

router = routers.DefaultRouter()

router.register(r'plist', views.PlistViewSet)
router.register(r'ppost', views.PpostViewSet)
router.register(r'plogdata', views.PlogdataViewSet)
router.register(r'events', views.EventsViewSet)
router.register(r'pdivizion', views.PdivisionViewSet)
router.register(r'pcompany', views.PcompanyViewSet)
# router.register(r'auth', views.AuthoritiesViewSet)
# router.register(r'querylog', views.QuerylogViewSet)
# router.register(r'logschangedb', views.LogsChangeBdViewSet)

urlpatterns = []
urlpatterns += router.urls
