from django.utils.timezone import now
from django.contrib import admin
from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','cpf','created_at',"subscribed_today","paid")
    date_hierarchy = 'created_at'
    search_fields = ("name","email","phone","cpf")
    list_filter = ('paid','created_at')
    
    actions = ["mark_as_paid","mark_as_not_paid"]
    
    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True
    
    def mark_as_paid(self,request,queryset):
        count = queryset.update(paid =True)
        if(count == 1):
            msg = '{} inscrição foi marcada como paga.'
        else:   
            msg = '{} incrições foram marcadas como pagas.'
        
        self.message_user(request,msg.format(count))
        
    def mark_as_not_paid(self,request,queryset):
        
        count = queryset.update(paid =False)
        if(count == 1):
            msg = '{} inscrição foi marcada como não paga.'
        else:   
            msg = '{} incrições foram marcadas como não pagas.'
        
        self.message_user(request,msg.format(count))
    
    mark_as_paid.short_description = 'Marcar como pago'
    mark_as_not_paid.short_description = 'Marcar como não pago'
    
    
admin.site.register(Subscription,SubscriptionModelAdmin)
