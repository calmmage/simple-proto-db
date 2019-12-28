from google.protobuf.message import Message as ProtobufMessage


class ProtoItemMeta:
    pass


class ProtoItem(metaclass=ProtoItemMeta):
    proto_type: ProtobufMessage = None

    # init - accept proto record attributes. Proper docstring?
    # patch in meta.

    # dir - do i need to patch it

    #
