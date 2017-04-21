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

urlpatterns = [
    redirect(r'projects/$', 'mozorg.product'),
    redirect(r'^projects/seamonkey$', 'mozorg.product', locale_prefix=False),
    redirect(r'apps/$', 'https://marketplace.firefox.com'),
    redirect(r'firefox/$', 'firefox.new', name='firefox'),
    redirect(r'the/dude$', 'abides', query={'aggression': 'not_stand'}),
]
```

Or you can install the `redirect_urls.middleware.RedirectsMiddleware` middleware and create 
`redirects.py` files in your Django apps. This will allow you to define a lot of redirects
in their own files (which will be auto-discovered) and guarantee that they'll be tested before 
the rest of your URLs.

```python
# redirects.py

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
