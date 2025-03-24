from django.contrib import admin
from .models import Ticket,TicketAdmin
admin.site.register(Ticket,TicketAdmin)