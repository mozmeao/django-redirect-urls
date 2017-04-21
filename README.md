# django-redirect-urls

Manage URL redirects and rewrites in Django like you do other URLs: in code.

This was extracted from [bedrock](https://github.com/mozilla/bedrock/) (the code behind www.mozilla.org).
We had a lot of redirects and rewrites we wanted to move out of Apache configs and into versioned code.
This library is the result of all of that. Because it started life on a Mozilla site it does have some
features for how we make sites (e.g. locale prefixing in URLs and the `is_firefox` helper). Now that it
is a separate thing however I'm very open to adding features and helpers for a more general audience.

## Install

```bash
$ pip install django-redirect-urls
```

## Examples

With this library you can do things like:

```python
# urls.py
from redirect_urls import redirect

urlpatterns = [
    redirect(r'projects/$', 'mozorg.product'),
    redirect(r'^projects/seamonkey$', 'mozorg.product', locale_prefix=False),
    redirect(r'apps/$', 'https://marketplace.firefox.com'),
    redirect(r'firefox/$', 'firefox.new', name='firefox'),
    redirect(r'the/dude$', 'abides', query={'aggression': 'not_stand'}),
]
```

There are a lot of options to the `redirect` helper. Here is the basic list:

* **pattern**: the regex against which to match the requested URL.
* **to**: either a url name that `reverse` will find, a url that will simply be returned,
    or a function that will be given the request and url captures, and return the
    destination.
* **permanent**: boolean whether to send a 301 or 302 response.
* **locale_prefix**: automatically prepend `pattern` with a regex for an optional locale
    in the url. This locale (or None) will show up in captured kwargs as 'locale'.
* **anchor**: if set it will be appended to the destination url after a '#'.
* **name**: if used in a `urls.py` the redirect URL will be available as the name
    for use in calls to `reverse()`. Does _NOT_ work if used in a `redirects.py` file.
* **query**: a dict of query params to add to the destination url.
* **vary**: if you used an HTTP header to decide where to send users you should include that
    header's name in the `vary` arg.
* **cache_timeout**: number of hours to cache this redirect. just sets the proper `cache-control`
    and `expires` headers.
* **decorators**: a callable (or list of callables) that will wrap the view used to redirect
    the user. equivalent to adding a decorator to any other view.
* **re_flags**: a string of any of the characters: "iLmsux". Will modify the `pattern` regex
    based on the documented meaning of the flags (see python re module docs).
* **to_args**: a tuple or list of args to pass to reverse if `to` is a url name.
* **to_kwargs**: a dict of keyword args to pass to reverse if `to` is a url name.
* **prepend_locale**: if true the redirect URL will be prepended with the locale from the
    requested URL.
* **merge_query**: merge the requested query params from the `query` arg with any query params
    from the request.

Or you can install the `redirect_urls.middleware.RedirectsMiddleware` middleware and create 
`redirects.py` files in your Django apps. This will allow you to define a lot of redirects
in their own files (which will be auto-discovered) and guarantee that they'll be tested before 
the rest of your URLs.

```python
# redirects.py
from redirect_urls import redirect

redirectpatterns = [
    redirect(r'projects/$', 'mozorg.product'),
    redirect(r'^projects/seamonkey$', 'mozorg.product', locale_prefix=False),
    redirect(r'apps/$', 'https://marketplace.firefox.com'),
    redirect(r'firefox/$', 'firefox.new', name='firefox'),
    redirect(r'the/dude$', 'abides', query={'aggression': 'not_stand'}),
]
```

## Run The Tests

```bash
$ pip install tox
$ tox
```
