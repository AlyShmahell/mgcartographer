# mgcartographer

- Pushes a JSON file based database to MongoDB Atlas.   
- Provides both a python interface and a script.   
- uses SRV links  

## Installation 
```sh
pip3 install git+http://github.com/Deprecode/mgcartographer
```
## Usage
  - ### as a script
    ```sh
    mgcartographer --link <atlas_srv_link> --database <local_database_path>
    ```  
  - ### as a library
    ```python
    from mgcartographer import MongoCartographer
    cartographer = MongoCartographer(<atlas_srv_link>)
    cartographer.push(os.path.join(<local_database_path>))
    ```