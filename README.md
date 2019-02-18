# django-presskit
A port of Rami Ismail's presskit()/dopresskit to Django.

[![Build Status](https://travis-ci.com/FutureProofGames/django_presskit.svg?branch=develop)](https://travis-ci.com/FutureProofGames/django_presskit)

## Installing

### Requirements:

* Django==1.11.x
* django-filer
* easy_thumbnails
* Markdown
* Pillow

Add "django_presskit" to your settings INSTALLED_APPS.

Add `DJANGO_PRESSKIT_DEFAULT_COMPANY_ID = 1` to your settings file.

In your main urls.py, add a line like: `url(r'^presskit/', include('django_presskit.urls', namespace='django_presskit')),`

All data can be set up in the Django admin.

## Converting from presskit()/dopresskit

If you are switching from Rami Ismail's presskit(), you'll want to make sure any old URLs that are floating around continue to work. Presskit() URLs look like `/presskit/sheet.php?p=exploit_zero_day`. You'll want to convert those into something like `/presskit/exploit-zero-day/`.

Make sure that the slugs for your django-presskit projects match those for your presskit() projects. Then, you can use URL rewriting to redirect users to the new URL.

If you have Apache with mod_rewrite enabled, add something like the following to your `.htaccess` file:

```
RewriteEngine  on
RewriteCond %{QUERY_STRING} ^p=(.*)$
RewriteRule "^/?presskit/sheet.php"  "/presskit/projects/%1" [N]
# Repeatedly remove underscores until only one is left.
RewriteRule "^(/?presskit/projects/.*)_(.*_.*)$"  "$1-$2" [N]
# Redirect with the last underscore rewrite.
RewriteRule "^(/?presskit/projects/.*)_(.*)$"  "$1-$2" [R=301]
RewriteRule "^/?presskit/sheet\.php$ "              "/presskit/" [R=301]
```

If you're using nginx for rewrites, this would look like:

```
location ~* /presskit/sheet.php {
    if ($args ~* "^p=(\d+)") {
        set $proj $1;
        set $args '';
        rewrite ^.*$ /presskit/projects/$proj permanent;
    }
}
# Remove up to 10 underscores until none are left.
rewrite ^(/?presskit/projects/.*?)_(.*)$  $1-$2 last
rewrite ^/?presskit/sheet\.php$           /presskit/ permanent
```
If you're using nginx and one of your slugs has more than ten underscores, add a rewrite above the first one to manually fix that one case. Nginx does not want to loop more than 10 times in a rewrite calculation.
