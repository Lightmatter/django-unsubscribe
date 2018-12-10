# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .compat import url
from .views import unsubscribe

urlpatterns = [
    url(
        r"^(?P<user_id>\d*)-(?P<token>.*)/$",
        unsubscribe,
        name="unsubscribe_unsubscribe",
    )
]
