from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from pathlib import Path
import constants
import os
import time
import logging
import json

logger = logging.getLogger(__name__)

class BasicServer_2(BaseHTTPRequestHandler):
    serverType = "BasicServer_2"
    htmlFilesDir = "htmlsWebPages"
    jsonFileDir = "res"


    def __init__(self, request, client_address, server):
        parent_dir = Path(__file__).parent.parent
        self.htmlFilesLocation = Path.joinpath(parent_dir, self.htmlFilesDir)
        self.jsonFileLocation = Path.joinpath(parent_dir, self.jsonFileDir)
        self.jsFilesLocation = parent_dir
        super().__init__(request, client_address, server)


    # Automatoically resolved when GET request is sumbitted.
    def do_GET(self):
        logger.info("[%s]::GET Request,\nPath: %s\nHeaders:\n%s\n", self.serverType, str(self.path), str(self.headers))

        if self.path == '/':
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.__get_html('index.html').encode())

        elif self.path.startswith('/getAll/'):
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.__get_json(self.path.removeprefix('/getAll/') + '.json' ).encode())

        elif self.path.startswith('/get/'):
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Our path is like: /get/user/<user_id>
            # we need to create correct filepath from it and extract the id.
            tokens = self.path.split('/')

            assert len(tokens) == 4, 'Tokens count is not 4 as expected!'

            self.wfile.write(self.__get_jsonEntity(filename=tokens[2] + 's.json', targetId=tokens[3]).encode())

        elif self.path == '/about':
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.__get_html('about.html').encode())

        elif self.path == '/contact':
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.__get_html('contact.html').encode())

        elif self.path.startswith('/js/'):
            self.send_response(constants.HTTP_SUCCESS)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            self.wfile.write(self.__get_js(self.path[1:]).encode())

        else:
            self.send_response(constants.HTTP_NOT_FOUND)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'404 - Not Found')


    # Automatoically resolved when POST request is sumbitted.
    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_payload = self.rfile.read(content_len)

        logger.info("[%s]::POST Request,\nPath: %s\nHeaders:\n%s\n\n", self.serverType, str(self.path), str(self.headers))
        logger.info("Body:\n%s\n", post_payload.decode('utf-8'))

        self.send_response(constants.HTTP_SUCCESS)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


    # Return full content of Json file as string.
    def __get_json(self, filename) -> str:
        logger.info("[%s]::Getting full content of JSON File = '%s' @ '%s'", self.serverType, filename, self.jsonFileLocation)
        try:
            with open(os.path.join(self.jsonFileLocation, filename), 'r') as file:
                return json.dumps(json.load(file))
        except FileNotFoundError:
            logger.info("[%s]::File = '%s' not found @ '%s'", self.serverType, filename, self.htmlFilesLocation)
            return self.__get_HtmlErrorAsHeader1(constants.HTTP_NOT_FOUND)


    # Return single entity from Json file as string
    def __get_jsonEntity(self, filename, targetId) -> str:
        logger.info("[%s]::Getting single target entity id = '%s' of JSON File = '%s' @ '%s'", self.serverType, targetId, filename, self.jsonFileLocation)
        try:
            jsonContent = json.loads(self.__get_json(filename=filename))    # As __get__json returns string and not Json object.
            result = None
            for dataEntity in jsonContent:
                if 'id' in dataEntity and str(dataEntity['id']) == targetId:
                    result = dataEntity
                    break

            if result == None:
                raise KeyError("[%s]::File = '%s' @ '%s' key = '%s' not found.", self.serverType, filename, self.jsFilesLocation, targetId)
            return json.dumps(result)

        except FileNotFoundError:
            logger.info("[%s]::File = '%s' not found @ '%s'", self.serverType, filename, self.htmlFilesLocation)
            return self.__get_HtmlErrorAsHeader1(constants.HTTP_NOT_FOUND)
        except KeyError as e:
            logger.info("Error: {e}")
            return self.__get_HtmlErrorAsHeader1(constants.HTTP_NOT_FOUND)

    # Return content of Html file as string.
    def __get_html(self, filename) -> str:
        logger.info("[%s]::Getting content of HTML File = '%s' @ '%s'", self.serverType, filename, self.htmlFilesLocation)
        try:
            with open(os.path.join(self.htmlFilesLocation, filename), 'r') as file:
                return file.read()
        except FileNotFoundError:
            logger.info("[%s]::File = '%s' not found @ '%s'.", self.serverType, filename, self.htmlFilesLocation)
            return self.__get_HtmlErrorAsHeader1(constants.HTTP_NOT_FOUND)


    # Return content of Javascript file as string.
    def __get_js(self, filename) -> str:
        logger.info("[%s]::Getting content of Js File = '%s' @ '%s'", self.serverType, filename, self.jsFilesLocation)
        try:
            with open(os.path.join(self.jsFilesLocation, filename), 'r') as file:
                return file.read()
        except FileNotFoundError:
            logger.info("[%s]::File = '%s' not found @ '%s'", self.serverType, filename, self.jsFilesLocation)
            return ""


    # Return Html errors as string.
    def __get_HtmlErrorAsHeader1(self, errorCode) -> str:
        if errorCode == constants.HTTP_NOT_FOUND:
            return "<h1>404 Not Found</h1>"
        
        return "<h1>500 Internal</h1>"



def startBasicServer(host_name, server_port):
    logger.info("Server Type = %s. Starting server!", BasicServer_2.serverType)
    localServer = HTTPServer((host_name, server_port), BasicServer_2)
    logger.info("Server 'http://%s:%d' is up and running...", host_name, server_port)

    try:
        localServer.serve_forever()
    except KeyboardInterrupt:
        pass

    localServer.server_close()
    logger.info("Server Type = %s. Server is stopped!", BasicServer_2.serverType)