from rest_framework import routers
from .api import UserDataViewSet

router = routers.DefaultRouter()
router.register('api', UserDataViewSet, 'UserData')

urlpatterns = router.urls