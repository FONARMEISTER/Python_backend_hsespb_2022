import grpc 
from protobuf.proto_gen.protocol_pb2_grpc import OfferSearcherStub
from protobuf.proto_gen.protocol_pb2 import OfferFilter

def search_offers(tag : str, lower_price : int, upper_price: int) -> int:
    """connects to localhost:50051 server and search for offers"""
    with grpc.insecure_channel('localhost:50051') as channel:
        client = OfferSearcherStub(channel)
        response = client.FindOffer(request = OfferFilter(tag, lower_price, upper_price))
        return response.in_stock