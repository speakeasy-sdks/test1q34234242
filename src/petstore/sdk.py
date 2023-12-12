"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .pet import Pet
from .sdkconfiguration import SDKConfiguration
from .store import Store
from .user import User
from petstore import utils
from petstore.models import shared
from typing import Dict, Optional

class Petstore:
    r"""Swagger Petstore - OpenAPI 3.0: This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
    Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
    You can now help us improve the API whether it's by making changes to the definition itself or to the code.
    That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

    Some useful links:
    - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
    - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
    http://swagger.io - Find out more about Swagger
    """
    pet: Pet
    r"""Everything about your Pets
    http://swagger.io - Find out more
    """
    store: Store
    r"""Access to Petstore orders
    http://swagger.io - Find out more about our store
    """
    user: User
    r"""Operations about user"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 petstore_auth: Optional[str]  = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param petstore_auth: The petstore_auth required for authentication
        :type petstore_auth: Union[str,Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security = shared.Security(petstore_auth = petstore_auth)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.pet = Pet(self.sdk_configuration)
        self.store = Store(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
    