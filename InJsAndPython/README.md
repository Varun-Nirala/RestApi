# Create a simple REST WebServer and Client using Python JavaScript
To demonstrat:</br>
  1. How to create simple web-client in Javascript.</br>
  2. How to create REST web-server in Python.</br>
</br></br>

## Reference Links
  1. Reference Video: https://www.youtube.com/watch?v=DeFST8tvtuI 
  2. https://pythonbasics.org/webserver/
  3. https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
  4. https://docs.python.org/3/library/http.server.html
  5. https://www.brandonrohrer.com/http_server
  6. https://www.programming-books.io/essential/python/basic-handling-of-get-post-put-using-basehttprequesthandler-cefff4e0b9664dd189d38a76f47ab410
  7. https://anshu-dev.medium.com/creating-a-python-web-server-from-basic-to-advanced-449fcb38e93b
</br>
  8. Flask: https://flask.palletsprojects.com/en/stable/
  9. Flask Example: https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/ 
  10. Free fake and reliable REST API webserver powered by JSON Server + LowDB for testing and prototyping: https://jsonplaceholder.typicode.com/
</br></br>

## About project.
  1. Three json data files namely `users`, `products`, and `orders`.
  2. A independent Javascript web-client. Which can send REST request to a webserver.
  3. A python web-server which receives REST request and act accordingly.
  4. Client and server request and response are based upon json data files mentioned in point 1.
</br></br>

## General info.
  1. **NOTE**: To start a webserver run below commands.</br>
    a. command: `python3 -m http.server`
            Result : It will open a webserver on port 8080. Then, you can open browser at `http://127.0.0.1:8080/`
</br>
    b.  command: `python -m http.server <PORT> -b http://<HOST>`
                `-b` to bind the server to a specific IP.
</br></br>

## Webserver's Hostname, Port and URL.
  HOSTNAME : 127.0.0.1</br>
  PORT     : 8001</br>
  URL      : 127.0.0.1:8001 or http://localhost:8001</br>
</br></br>

## Available APIs
  1. GET:</br>

            /about
            /contact

            /getAll/users
            /getAll/products
            /getAll/orders

            /get/user/<user-id>
            /get/product/<product-id>
            /get/order/<order-id>
</br></br>

## How to run.
  1. On browser:
        * Run your code.
        * Opne browser.
        * visit: 
            http://<HOST>:<PORT>/ or localhost:<PORT>
            result: You should see some web page, whatever you have configured/created in respose, as per code.

  2. Via terminal:
        * Run your code.
        * Open Terminal.
        * run:
            1. command: 
                cmd/PS: `curl <HOST>:<PORT>`
                result:  your web page or whatever you have configured in response, as per          code.

            2. command: 
                cmd:    `curl <HOST>:<PORT> -X POST`
                PS:     `curl <HOST>:<PORT> -Method POST`
                result: Proper response and HTTP code, html content along with error response
                            like `501 Not implemented`.
</br></br>