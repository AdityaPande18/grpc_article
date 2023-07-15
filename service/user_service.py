import logging
from messages.user_info_pb2_grpc import UserServiceServicer
import messages.user_info_pb2 as user_info_pb2

USER_MOCK_DB = {
    "John": "924 W Main St Tipp City, Ohio, 45371, United States",
    "Shawn": "200 W Peace St Raleigh, Nebraska, 27603, United States",
}


class RequestHandlerService(UserServiceServicer):
    def getUserAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        try:
            user_name = request.name
            user_address = USER_MOCK_DB[user_name]
            return user_info_pb2.UserResponse(address=user_address, error="No Errors")
        except Exception as ex:
            logging.error(f"Something went wrong: {str(ex)}", exc_info=True)
            return user_info_pb2.UserResponse(error=f'Something went wrong: {str(ex)}', address="-")
