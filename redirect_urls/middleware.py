from django.core.urlresolvers import Resolver404

from redirect_urls.utils import get_resolver


class RedirectsMiddleware(object):
    def __init__(self, get_response=None, resolver=None):
        self.get_response = get_response
        self.resolver = resolver or get_resolver()
        super(RedirectsMiddleware, self).__init__()

    def __call__(self, request):
        try:
            resolver_match = self.resolver.resolve(request.path_info)
        except Resolver404:
            if self.get_response is None:
                return None
            else:
                return self.get_response(request)

        callback, callback_args, callback_kwargs = resolver_match
        request.resolver_match = resolver_match
        return callback(request, *callback_args, **callback_kwargs)
