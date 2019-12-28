# simple-proto-db
Simple lib that stores protobuf items in a database of your choice.

1) Create one or several proto files describing items you want to store in the database
2) Compile them
3) declare corresponding item classes
    ```python
    from proto_database import ProtoItem
    from animal_pb2 import Animal
    class ProtoAnimal(ProtoItem):
        proto_type = Animal
    ```  
4) declare your proto_database class
    ```python
    from proto_database import ProtoDatabase
    class MyProtoDatabase(ProtoDatabase):
        types = [ProtoAnimal]
    ```

