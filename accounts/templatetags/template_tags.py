from django import template

register = template.Library()

@register.inclusion_tag("registration/templatetags/link_base_profile_view.html")
def link_base_profile(request,content_name,url_name):
    return {
        "request": request,
        "content_name": content_name,
        "url_name": f"account:{url_name}"
    }