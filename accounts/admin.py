from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', "username", 'date_joined',
                    'last_login', 'is_staff', 'is_sig_head', 'is_admin', 'is_superuser')
    search_fields = ('email', "username", "membership_no")
    readonly_fields = ('date_joined', 'last_login')
    # just required
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
