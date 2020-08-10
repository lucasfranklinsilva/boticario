# HTTP STATUS
HTTP_SUCCESS = 200
HTTP_CREATED = 201
HTTP_SERVER_ERROR = 500
HTTP_BAD_REQUEST = 400

# MYSQL
DB_USER_NAME = 'root'
DB_PASSWORD = 'root123@'
DB_HOST = 'localhost:3306'
DATA_BASE = 'boticario'
DB_CONNECTION_STRING = 'mysql://' + DB_USER_NAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DATA_BASE

# TABLES
T_CASH_BACK = 'Cashback'
T_PURCHASE = 'Purchase'
T_PURCHASE_STATUS = 'Purchase_Status'
T_RESELLER = 'Reseller'

# CONTENTS
JSON_CONTENT = "application/json"

# MESSAGES
SUCCESS_MESSAGE = 'Success'

# PURCHASES
PURCHASE_DEFAULT_STATUS_ID = 1 # 'Em validação'
PURCHASE_APROVED_STATUS_ID = 2 # 'Aprovado'
PURCHASE_USER_EXCEPTION = '153.509.460-56'

# DB FIELDS NAMES
F_RESELLER_ID = 'reseller_id'
F_PURCHASE_STATUS_ID = 'purchase_status_id'
F_CASHBACK_PERCENT = 'cash_back'
F_SALT_PASSWORD = 'salt_password'
F_PASSWORD = 'hash_password'

# JSON
J_CPF = 'cpf'
J_PRODUCT_PRICE = 'product_price'
J_PASSWORD = 'password'
J_USER_EMAIL = 'email'

# EXTERNAL API
API_CASHBACK_URL = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf='
API_TOKEN = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'
API_HEADER = {'Content-type': 'application/json', 'token': API_TOKEN}
# GENERAL
ACTIVE_STATUS = 1

# JWT
CHAR_ENCODE = 'UTF-8'
JWT_ALGORITHM = 'HS256'
JWT_SECRET_KEY = '2jvxmFsY7w0mWEkPwuMXilt_7K7uCBFW5loBeIW6ldUh7c5VxWqFkVxIp0W_wjgZqALbxfg1BXIVbPUvysKHa54SVV8FzyyP2Mj424gKjUtyhVQL2GGkv2mL0Dt08kOBsxQZ78XqvkWTFbCkgPKHYb0Gw-hlyqsUEDGcJYlrozs'
PAYLOAD_USER = 'user'
PAYLOAD_PASSWORD = 'password'
PAYLOAD_EXPIRATION = 'exp'
JWT_EXP_MINUTES = 60

