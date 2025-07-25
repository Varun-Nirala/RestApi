from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import constants
import basicServer_1
import basicServer_2
import logging

logger = logging.getLogger(__name__);
logging.basicConfig(level=logging.DEBUG);


def startApp(serverType):
    if serverType == "BasicServer_1":
        basicServer_1.startBasicServer(host_name=constants.SERVER_IP, server_port=constants.SERVER_PORT);
    elif serverType == "BasicServer_2":
        basicServer_2.startBasicServer(host_name=constants.SERVER_IP, server_port=constants.SERVER_PORT);



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