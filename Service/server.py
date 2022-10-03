import grpc
from concurrent import futures
import protobuf.proto_gen.protocol_pb2_grpc as protocol
from protobuf.proto_gen.protocol_pb2 import Response
from database import db_offers


class Service(protocol.OfferSearcherServicer):
    def FindOffer(self, request, context):
        """ finds number of offers fitting tag and price restrictions

        Args:
            request (OfferFilter): given price and tag filter for offers
            context (_type_): grpc necessary argument

        Returns:
            Response : count of offers fitting filter
        """
        print(len(db_offers))
        return Response(in_stock=len(list(filter(lambda x: x[0] == request.tag and 
        (request.lower_price <= x[1] and x[1] <= request.upper_price), db_offers))))


def main():
    """ creates and starts server on port 50051 """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protocol.add_OfferSearcherServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()