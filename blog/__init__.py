"""
the blog app is an example of an app accessed using a subdomain 
the url for the blog app would be something like https://blog.example.com 
"""

import logging 
logger = logging.getLogger(__name__)

from flask import Flask 

subdomain = 'blog' 

def create_app(config=None):
    domain = None 
    if config:
        domain = config.get('domain')

    logger.info(f'creating app for {subdomain}.{domain}')
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def index():
        logger.info(f'in {subdomain}:index')
        return f'Hello from the {subdomain} application!  Blog on Wayne!!  Blog on Garth!!'

    return app 


## end of file 