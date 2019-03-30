from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from onlinemechaniclocator.messager.consumers import MessagerConsumer
from onlinemechaniclocator.notifications.consumers import NotificationsConsumer
# from onlinemechaniclocator.notifications.routing import notifications_urlpatterns
# from onlinemechaniclocator.messager.routing import messager_urlpatterns

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r'^notifications/$', NotificationsConsumer),
                url(r'^(?P<username>[^/]+)/$', MessagerConsumer),
            ])
        ),
    ),
})
