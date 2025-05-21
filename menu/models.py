from django.db import models
from django.contrib.auth.models import User


######################################
# pain alie
######################################
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name

        # class Order(models.Model):
        # STATUS_CHOICES = [
        # ('pending', 'در انتظار'),
        # ('preparing', 'در حال آماده‌سازی'),
        # ('delivered', 'تحویل داده شده'),
        # ('cancelled', 'لغو شده'),
        # ]

        # customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
        # created_at = models.DateTimeField(auto_now_add=True)
        # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
        # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

        # def __str__(self):
        # return f"Order #{self.id} by {self.customer.username}"

# class OrderItem(models.Model):
# order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
# menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
# quantity = models.PositiveIntegerField(default=1)
# price = models.DecimalField(max_digits=8, decimal_places=2)

# def get_total_price(self):
# return self.quantity * self.price


# class Payment(models.Model):
# order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
# amount = models.DecimalField(max_digits=10, decimal_places=2)
# paid_at = models.DateTimeField(auto_now_add=True)
# is_successful = models.BooleanField(default=False)
# payment_method = models.CharField(max_length=50, choices=[
# ('cash', 'نقدی'),
# ('card', 'کارت بانکی'),
# ('online', 'آنلاین'),
# ])

# def __str__(self):
# return f"payment for Order #{self.order.id}"

######################################
# pain Mr U va Abol
######################################
