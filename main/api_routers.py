from rest_framework import routers
from gate import view_sets as gate_vs
from crypto import view_sets as crypto_vs
from schedule import view_sets as calendar_vs

# Register api routes here
router = routers.DefaultRouter()
router.register(r'user', gate_vs.UserViewSet)
router.register(r'user_log', gate_vs.UserLogViewSet)
router.register(r'vechain', crypto_vs.VechainCandleViewSet)
router.register(r'calendar', calendar_vs.CalendarViewSet)