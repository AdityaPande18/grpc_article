import grpc
from messages.user_info_pb2_grpc import UserServiceStub
import messages.user_info_pb2 as user_info_pb2


user_name = "John"


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = UserServiceStub(channel)
        response = stub.getUserAddress(
            user_info_pb2.UserRequest(name=user_name))
        print(f"Address: {response.address}  |  Error: {response.error}")


if __name__ == "__main__":
    run()
