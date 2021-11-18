from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError, forms, fields
from django.utils.safestring import mark_safe

from .models import *


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NotebookAdminForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:14px";>Загружайте изображение
             с минимальным размером {}x{},
             но не больше {}x{}, если разрешение будет больше максимального,
             то изображение будет обрезано.</span>""".format(
                *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION
            )
        )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_heigth, min_width = Product.MIN_RESOLUTION
    #     max_heigth, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер загружаемого изображения не должен превышать 3мб')
    #     if img.width < min_width or img.height < min_heigth:
    #         raise ValidationError('Загруженное изображение меньше минимального')
    #     if img.width > max_width or img.height > max_heigth:
    #         raise ValidationError('Загруженное изображение больше максимального')
    #     return  image


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


class BaseAdminModel(admin.ModelAdmin):
    slug = ''

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category' and self.slug:
            queryset = Category.objects.filter(slug=self.slug)
            return ModelChoiceField(queryset, initial=queryset[0], widget=fields.Select(attrs={'disabled': 'disabled'}))
        return super(BaseAdminModel, self).formfield_for_foreignkey(db_field, request, **kwargs)


class NotebookAdmin(BaseAdminModel):
    form = NotebookAdminForm
    slug = 'Notebooks'


class SmartphoneAdmin(BaseAdminModel):
    change_form_template = 'admin.html'
    form = SmartphoneAdminForm
    slug = 'Smartphones'


class TilevisionAdmin(BaseAdminModel):
    slug = 'Televisions'


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Television, TilevisionAdmin)
admin.site.register(Order)
