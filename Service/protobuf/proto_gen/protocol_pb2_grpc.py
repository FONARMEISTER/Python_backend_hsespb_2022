# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobuf.proto_gen.protocol_pb2 as protocol__pb2


class OfferSearcherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindOffer = channel.unary_unary(
                '/OfferSearcher/FindOffer',
                request_serializer=protocol__pb2.OfferFilter.SerializeToString,
                response_deserializer=protocol__pb2.Response.FromString,
                )


class OfferSearcherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindOffer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OfferSearcherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindOffer': grpc.unary_unary_rpc_method_handler(
                    servicer.FindOffer,
                    request_deserializer=protocol__pb2.OfferFilter.FromString,
                    response_serializer=protocol__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OfferSearcher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OfferSearcher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindOffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OfferSearcher/FindOffer',
            protocol__pb2.OfferFilter.SerializeToString,
            protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
