from rest_framework import routers
from gate import view_sets

# Register api routes here
router = routers.DefaultRouter()
router.register(r'user', view_sets.UserViewSet)
router.register(r'user_log', view_sets.UserLogViewSet)