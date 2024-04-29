from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class TraderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
        
class StockMarketOrder(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    trader = models.ForeignKey(TraderProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-order_date']

    def get_absolute_url(self):
        return '/' + str(self.id) + '/'

    def __str__(self):
        return self.name + ' - ' + self.ticker + ' - ' + str(self.quantity) + '@$' + str(self.price)

# Create a custom save method that will update the order total each time an Order object is saved to the database
class MarketTransaction(StockMarketOrder):
    pass

class LimitOrder(MarketTransaction):
    pass

class StopLossOrder(MarketTransaction):
    pass

class TradingSection(models.Model):
    name = models.CharField(max_length=100)
    trader = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " ("+self.trader.username+")"

# @receiver(post_save, sender=MarketTransaction)
# def create_stockmarkettransaction(sender, instance, created, **kwargs):
#     if created:
#         instance.save()
#         tradingsection, _ = TradingSection.objects.get_or_create(name=instance.name, trader=instance.trader)
#         tradingsection.active = True
#         tradingsection.save()</script>

# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><style type="text/css"><style type="text/css">
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><style type="text/css"><style type="text/css"><style type="text/css"><style type="text/css">
# <h3>Add a new Stock Order</h3>
# {% load crispy_forms %}
# <form method="POST">
#   {% csrf_token %}
#   {{ form|crispy }}
#   <button type="submit" class="btn btn-primary">Submit</button>
# </form>
# <hr />
# <h4>Active Orders</h4>
# <table class="table table-striped">
#   <thead>
#       <tr>
#           <th scope="col">Type</th>
#           <th scope="col">Symbol</th>
#           <th scope="col">Quantity</th>
#           <th scope="col"></th>
#       </tr>
#   </thead>
#   <tbody>
#     {% for order in orders %}
#         <tr>
#             <td>{{order.type}}</td>
#             <td><a href="/symbol/{{order.ticker}}">{{order.ticker}}</a></td>
#             <td>{{order.quantity}}</td>
#             <td><a href="{% url 'delete_order' order.id %}">Delete</a></td>
#         </tr>
#     {% empty %}
#         <tr>
#             <td colspan="5">No Orders</td>
#         </tr>
#     {% endfor %}
#   </tbody>
# </table>

class TradeCommand(models.Model):
    section = models.ForeignKey(TradingSection, on_delete=models.CASCADE)
    command = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    trader = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

@login_required
def tradecommand(request):
    return render(request, 'moni/tradecommand.html')
