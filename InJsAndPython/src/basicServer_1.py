from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import time
import logging
import constants

logger = logging.getLogger(__name__)

class BasicServer_1(BaseHTTPRequestHandler):
    serverType = "BasicServer_1"
    html_body = '''
<html>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
'''

    # Automatoically resolved when GET request is sumbitted.
    def do_GET(self):
        logger.info("[%s]:: GET Request,\nPath: %s\nHeaders:\n%s\n", self.serverType, str(self.path), str(self.headers))
        self.send_response(constants.HTTP_SUCCESS)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(self.html_body, "utf-8"))

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



def startBasicServer(host_name, server_port):
    logger.info("Server Type = %s. Starting server!", BasicServer_1.serverType)
    localServer = HTTPServer((host_name, server_port), BasicServer_1)
    logger.info("Server 'http://%s:%d' is up and running...", host_name, server_port)

    try:
        localServer.serve_forever()
    except KeyboardInterrupt:
        pass

    localServer.server_close()
    logger.info("Server Type = %s. Server is stopped!", BasicServer_1.serverType)