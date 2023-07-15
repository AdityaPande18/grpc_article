from concurrent import futures
import grpc
from messages.user_info_pb2_grpc import add_UserServiceServicer_to_server
from service.user_service import RequestHandlerService


def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Register user service
    user_service = RequestHandlerService()
    add_UserServiceServicer_to_server(user_service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    grpc_server()
