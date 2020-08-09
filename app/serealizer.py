from flask_marshmallow import Marshmallow


ma = Marshmallow()


def configure(app):
    ma.init_app(app)

class Purchase_Schema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('product_code', 'product_price', 'date',
                  'cash_back', 'cash_back_amount', 'status', 'cpf')

class Cashback_Schema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id_cashback', 'purchase_amount', 'percentage')

class Purchase_Status_Schema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id_purchase_status', 'status', 'is_active')

class Reseller_Schema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id_reseller', 'email', 'create_date', 'first_name', 'last_name', 'cpf', 'street',
                  'city', 'state', 'country', 'zip_code', 'phone', 'is_active', 'last_updated')






