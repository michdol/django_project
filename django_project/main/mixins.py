from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RedirectUnauthenticatedMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)