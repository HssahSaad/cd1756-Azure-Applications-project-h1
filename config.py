import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aMhgJy4SP9Pa1MedIeS1DZNZPd1gzV_E4xvT_dc00B0'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'flaskappstoragehssah'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'HiJMPdD6cnTpXr/6QR1ekAxJ9jdIc2i7Q6lENQuvicqjwUgVWMGaSXnQwLnImhaVx89iqVnE2Jsd+AStVdOl+A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'flaskimages'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'flaskappserver-hssah.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'flaskapp-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'HESSA*2020'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sqladmin:HE1234sh@flaskappserver-hssah.database.windows.net/flaskappdb?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "HQi8Q~MTl1oDcON-~H5MLNo44_b1YsWs9OGbTcav"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "fa52e912-e481-4fab-a749-4ca043c3c20b"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
