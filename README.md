# REST API Intro and Implementation in different languages.
To demonstrate how to use or implement REST APIs webserver in different programming languages.

## Reference Links
  1. https://www.restapitutorial.com/  
  2. HTTP Web Linking Specification (RFC5988)  
  3. APIs Example:
     1. Twitter: https://developer.twitter.com/en/docs/api-reference-index
     2. Facebook: https://developers.facebook.com/docs/reference/api/
     3. LinkedIn: https://developer.linkedin.com/apis
</br></br>

## Introduction to REpresentation State Transfer (REST).
1. **REST**: An architecture style originally written by Roy Fielding in his [doctoral dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).  
      Mostly, `REST service`, `REST API` or `RESTful API` mean an `HTTP` or web-based server which
    accepts requests over `HTTP` and responds in human-readable `JSON`.  
      The `six constrainst` provided in Roy's dissertation MUST be met in order for a service to be 
    rechnically RESTful, they don't specify any protocal.  

    Basic flow, the caller/client:  
      1. Makes an HTTP request to a URL  
        * using one of the standard HTTP methods (GET, PUT, POST, PATCH, DELETE, etc.)  
        * with some content(usually JSON) in the body  
      2. And waits for a response, which:  
        * indicates status via an HTTP response code  
        * and usually has more JSON in the body.  
</br>

2. **Rest is resource based**: Not action based like in `SOAP`.  
      1. Resources are identified by URIs.  
      2. Multiple URI can point to same resource.  
      3. Separate from their representation.  
            Representation?  
              * How resources get manipulated.  
              * Part of the resource state. Transfered between server-client.  
        4. Resource can be in different format like: JSON, XML.  
    Ex: Person resource, Phone resource, address resource.  
</br>

2. **Six Constraints**:  
      1. Uniform interface  
      2. Stateless  
      3. Client-server  
      4. Cacheable  
      5. Layered system  
      6. Code on demand  
</br>
    Compliance with them allows:  
      * Scalability,  
      * Simplicity,  
      * Modifiability,  
      * Visibility,  
      * Portability, and  
      * Reliability  
</br>

3. **Uniform interface**:  
      1. Define interface between client-server.  
      2. Simplifies and decouples the architecture.  
      3. Fundamental to RESTful design.  

    Four guiding principles of the `Uniform interface` are:  
      1. `Resource-based`.  
      2. Manipulation of Reosurces through `representations`.  
      3. `Self-descriptive` messages.  
      4. Hypermedia as the Engine of `Application State (HATEOAS)`.  

    Ex: Please note it is not mandatory to use HTTP,  
          * HTTP verbs (GET, PUT, POST, DELETE)
          * URIs
          * HTTP response (status, body)
</br>   

4. **Stateless**:
      1. Server does not maintain/stores client state.
      2. For above reason, each message should be self-descriptive, and should contain enough context 
        required for processing it.
</br>

5. **Client-Server**:
      1. Separation of concern.
      2. Uniform interface is the communication link between them.
</br>

6. **Cacheable**:
      1. Server responses should be cacheable, as mentioned below:
        * implicitly    (default)
        * explicitly    (explicitly stated by server)
        * negotiable    (negatiation between clients and server, like duration of validity of cached data.)
</br>

7. **Layered System**:
      1. Client can't assume direct connection(there can be h/w or s/w intermediaries) to server.
      2. It improves scalability.
</br>

8. **Code on demand**: (this one is optional constraint)
      1. Server can temporarily extend client. Which means, client can work as server by simple transfer of
        core server logic as representation.
</br>

9. **HTTP Methods**:  
      1. GET    - Read a specific resource or collection of resources (by an identifier).  
      2. PUT    - Create/Replace a specific resource or collection of resources (by an identifier).  
      3. PATCH  - Update a specific resource or collection of resources (by an identifier). Partial update compared to `PUT`.  
      4. DELETE - Remove/delete a specific resource (by an identifier).  
      5. POST   - Create a new resource. Also, a catch-all verb for operations that don't fit into the other categories.  
</br>

10. **HTTP Codes**: Common `HTTP` codes.  
      1. 200 OK           - Success.  
      2. 201 Created      - Successful creation (via `POST`/`PUT`). Response body may be present.  
      3. 204 No Content   - Success with no response in body. Often used for `DELETE` and `PUT`.  
      4. 400 Bad Request  - Invalid state general error. Ex: Domain validation errors, missing data, etc.  
      5. 401 Unauthorized - Missing or Invalid auth token.  
      6. 403 Forbidden    - User is unauthorized to access the resource.  
      7. 404 Not Found    - Requested Resource not found. Whether it doesn't exist or ir there was `401/403` that, for security reason, the service wants to mask.  
      8. 405 Method not allowed     - Request URL exists, but the HTTP method is not applicable.  
      9. 409 Conflict               - Request will lead to a resource conflict. Like some update will cause duplicated entry.  
      10. 500 Internal Server Error - General catch-all-error server side error. Should note be returned intentionally.  
</br>

**IDEMPOTENT** - *Performing same operation multiple times yields the same results as if it were executed only once.*  

11. **POST**: Post verb is mostly used for `creating` new resources(subordinate resources).  

    SAFE        - NO  
    IDEMPOTENT  - NO  

    Returns     - HTTP response code  

    HTTP Return code  
      - 201 Created  
      - 404 Not Found  
      - 409 Conflict  

    Ex:  
      `POST http://www.example.com/customers`  
      `POST http://www.example.com/customers/2025`  
      `POST http://www.example.com/customers/2025/orders`  
</br>

12. **GET**: Used to `read/retrieve` a representation of a resource.  

    SAFE        - YES (When used along with HEAD to only read the data)  
    IDEMPOTENT  - YES  

    Returns     - Data (XML or JSON) + HTTP response code  

    HTTP Return code  
      - 200 Ok  
      - 400 Bad Request  
      - 404 Not Found  

    Ex:  
      `GET http://www.example.com/customers/2025`  
      `GET http://www.example.com/customers/2025/orders`  
</br>

13. **PUT**: Used to `update` a representation of a resource. Request body contains the updated representation. The representation  
        should be of the whole resource and not only modifications. Can be used for creation too, where `resource ID` is choosen  
        by client instead of server.  

    SAFE        - No  
    IDEMPOTENT  - YES  

    Returns     - Data (XML or JSON) + HTTP response code  

    HTTP Return code  
      - 200 Ok  
      - 201 Created  
      - 204 No Content  
      - 400 Bad Request  
      - 404 Not Found  

    Ex:  
      `PUT http://www.example.com/customers/2025`  
      `PUT http://www.example.com/customers/2025/orders`  
</br>

14. **PATCH**: Used to `modify/update` a representation of a resource. It only requires the changed part of the Resource's  
        representation, and instructions describing `how to use the new DATA to modify the existing resource`. Can be used  
        for creation too, where `resource ID` is choosen by client instead of server.  

    SAFE        - NO  
    IDEMPOTENT  - NO (Can be made idempotent)  

    Returns     - Data (XML or JSON) + HTTP response code  

    HTTP Return code  
      - 200 Ok  
      - 204 No Content  
      - 404 Not Found  
      - 405 Method Not Allowed  

    Ex:  
      `PATCH http://www.example.com/customers/2025`  
      `PATCH http://www.example.com/customers/2025/orders`  
</br>

15. **DELETE**: Used to `remove` a representation of a resource identified by `resource URI`.  

    SAFE        - NO  
    IDEMPOTENT  - YES  

    Returns     - Data (XML or JSON) + HTTP response code   

    HTTP Return code  
      - 200 Ok  
      - 204 No Content  
      - 404 Not Found  

    Ex:  
      `DELETE http://www.example.com/customers/2025`  
      `DELETE http://www.example.com/customers/2025/orders`  
</br>