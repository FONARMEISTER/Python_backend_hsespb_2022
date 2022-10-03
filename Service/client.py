import grpc
import sys 
from protobuf.proto_gen.protocol_pb2_grpc import OfferSearcherStub
from protobuf.proto_gen.protocol_pb2 import OfferFilter


def search_offers(tag_: str, lower_price_: int, upper_price_: int) -> int:
    """connects to localhost:50051 server and search for offers"""
    with grpc.insecure_channel('localhost:50051') as channel:
        client = OfferSearcherStub(channel)
        response = client.FindOffer(OfferFilter(tag=tag_, lower_price=lower_price_, upper_price=upper_price_))
        return response.in_stock


def main():
    print(search_offers(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))

    
if __name__ == '__main__':
    main()