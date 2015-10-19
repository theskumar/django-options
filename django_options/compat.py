try:
    from django.contrib.admin.helpers import normalize_fieldsets
except ImportError:
    normalize_fieldsets = lambda x: x
