from django.db import models


def recalc_cart(cart):
    cart_data = cart.product.aggregate(models.Sum('final_price'), models.Count('id'))
    if cart_data.get('final_price__sum'):
        cart.final_price = cart_data['final_price__sum']
    else:
        cart.final_price = 0
    cart.total_product = cart_data['id__count']
    cart.save()














    # # Если карзина не сохранена то получим ошибку, т.к обращаемся к несуществующему полю ManyToManyField
    # if not self._state.adding:
    #     cart_data = self.product.aggregate(models.Sum('final_price'), models.Count('id'))
    #     if cart_data.get('final_price__sum'):
    #         self.final_price = cart_data['final_price__sum']
    #     else:
    #         self.final_price = 0
    #     self.total_product = cart_data['id__count']
    # super().save(*args, **kwargs)