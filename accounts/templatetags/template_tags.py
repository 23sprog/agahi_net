from django import template

register = template.Library()

@register.inclusion_tag("registration/templatetags/link_base_profile_view.html")
def link_base_profile(request, content_name, url_name):
    return {
        "request": request,
        "content_name": content_name,
        "route_page": url_name,
        "url_name": f"account:{url_name}"
    }

@register.inclusion_tag("registration/templatetags/link_navbar.html")
def link_navbar(request, content_name, url_name, route_name=None):
    if route_name is None:
        return {
            "request": request,
            "content_name": content_name,
            "url_name": url_name,
            "url_link": None
        }
    else:
        return {
            "request": request,
            "content_name": content_name,
            "url_name": url_name,
            "url_link": f"{route_name}:{url_name}"
        }