# clean_old_items.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from orders.models import Cart, CartItem, OrderInformation


class Command(BaseCommand):
    help = 'Clean up old items and carts older than 3 days'

    def handle(self, *args, **kwargs):
        three_days_ago = timezone.now() - timezone.timedelta(days=3)

        # Delete old carts without associated orders
        old_carts = Cart.objects.filter(date_generation__lt=three_days_ago)

        # Exclude carts that have associated OrderInformation records
        carts_with_orders = OrderInformation.objects.values_list('cart_data', flat=True)
        old_carts = old_carts.exclude(pk__in=carts_with_orders)

        # Delete old cart items
        old_cart_items = CartItem.objects.filter(cart_items__in=old_carts, date_generation__lt=three_days_ago)
        old_cart_items.delete()

        # Delete old carts
        old_carts.delete()

        self.stdout.write(self.style.SUCCESS('Successfully cleaned up old items and carts.'))


