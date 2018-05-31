from django.core.urlresolvers import Resolver404
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
    is_compatible_with_new_style = False
else:
    is_compatible_with_new_style = True

from redirect_urls.utils import get_resolver


class RedirectsMiddleware(MiddlewareMixin):

    @classmethod
    def for_test(cls, get_response=None, resolver=None):
        middleware = cls(get_response or (lambda req: None), resolver)
        if not is_compatible_with_new_style:
            return middleware.process_request
        return middleware

    def __init__(self, get_response=None, resolver=None):
        self.resolver = resolver or get_resolver()
        if is_compatible_with_new_style:
            super(RedirectsMiddleware, self).__init__(get_response)
        else:
            super(RedirectsMiddleware, self).__init__()

    def process_request(self, request):
        try:
            resolver_match = self.resolver.resolve(request.path_info)
        except Resolver404:
            return None
        callback, callback_args, callback_kwargs = resolver_match
        request.resolver_match = resolver_match
        return callback(request, *callback_args, **callback_kwargs)
