from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import constants
import basicServer_1
import basicServer_2
import logging

logger = logging.getLogger(__name__);       # create a logger and associate name (__name__ = "__main__") with it.
logging.basicConfig(level=logging.DEBUG);   # Enable debug logging.


def startApp(serverType):
    if serverType == "BasicServer_1":
        # BasicServer_1: Simple html web page. Nothing fancy very basic server.
        basicServer_1.startBasicServer(host_name=constants.SERVER_IP, server_port=constants.SERVER_PORT)

    elif serverType == "BasicServer_2":
        # BasicServer_2: Html web page with dynamic content. REST method trigger with different arguments.
        basicServer_2.startBasicServer(host_name=constants.SERVER_IP, server_port=constants.SERVER_PORT)



def main():
    logger.info('Started')

    serverArray = [
        "BasicServer_1",
        "BasicServer_2",
    ]
    startApp(serverArray[1])

    logger.info('Finished')



if __name__ == '__main__':
    main()