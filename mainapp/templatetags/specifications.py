from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone

register = template.Library()

TABLE_HEAD = """
            <table class="table">
                <tbody>
        """

TABLE_TAIL = """
                </tbody>
            </table>    

"""

TABLE_CONTENT = """
         <tr>
                <td>{name}</td>
                <td>{value}</td>
            </tr>

"""

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип матрицы': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видео карта': 'video',
        'Автономность': 'time_without_charge'

    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип матрицы': 'display_type',
        'Разрешение экрана': 'resolution',
        'Оперативная память': 'ram',
        'Слот для SD карты': 'sd',
        'Максимальный объем встраиваемой памяти': 'sd_volume_max',
        'Главная камера': 'main_cam_mp',
        'Фронтальная камера': 'frontal_cam_mp',
        'Емкость батареи': 'acum_volume'
    },
    'television': {
        'Диагональ': 'diagonal',
        'Тип матрицы': 'display_type',
        'Частота дисплея': 'display_freq',
        'Разрешение экрана': 'resolution',
        'Оперативная память': 'ram',
        'Наличие функции смарт': 'smart_fync',
        'Наличие функции 3D': 'display_3d_fync',
        'Мощность динамиков': 'speaker_power',
        'Количество USB портов': 'usb_qty',
        'Количество HDMI портов': 'hdmi_qty'
        }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объем встраиваемой памяти')
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объем встраиваемой памяти'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
