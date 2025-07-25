# REST API Example using : Python and already available website having REST API.

To demonstrate how to access REST APIs webserver using simple python (no lib like Flask etc).
</br></br>


## Reference Links
  1. https://www.datacamp.com/tutorial/making-http-requests-in-python  
  2. https://jiminbyun.medium.com/building-python-scripts-for-rest-api-calls-a-practical-guide-2-9-3ac9ca1d701a  
  3. https://pythongeeks.org/python-and-rest-api/  
  4. https://realpython.com/api-integration-in-python/  
  5. https://realpython.com/api-integration-in-python/  
  6. https://www.integrate.io/blog/an-introduction-to-rest-api-with-python/
  7. Will create project to hi REST API of https://openlibrary.org/ .
</br></br>


## Setup
  1. Follow [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

  2. Install Python Extension : https://marketplace.visualstudio.com/items?itemName=ms-python.python

  3. Open/Create any folder for python workspace/project and start VS Code in workspace/project folder.</br>
        `mkdir TestProject`</br>
        `cd TestProject`</br>
        `code .`

  4. Create a python `Virtual Environment`.</br>
        1. In Windows press `Ctrl+Shift+P`</br>
        2. Search `Python:Create Environment`</br>
        3. Select `Venv Creates a /`.venv/` virtual environment in the current workspace`</br>
        4. Choose the python interpreter path. Mostly the `Recommended` one.

  5. **NOTE**: Above steps will create a `.venv` folder in workspace.

  6. To activate the `Python Virtual Environment`
        Linux/Mac   - `source venv/bin/activate`
        Windows     - `.\venv\Scripts\activate`

  7. Create your code files parallel to the generated `.venv` folder.

  8. To generate the `requirements.txt` file.</br>
        `pip freeze > requirements.txt`

  9. To add dependencies via `requirements.txt` file.</br>
        `pip install -r requirements.txt`

  10. Instal packages in</br>
        Linux:
            `apt-get install python3-tk`
            `python3 -m pip install <package_name>`

        Mac:
            `python3 -m pip install <package_name>`
    
        Windows:
            `py -m pip install <package_name>`