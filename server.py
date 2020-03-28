import hello_pb2
import hello_pb2_grpc
from concurrent import futures
import time
import grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Hello(hello_pb2_grpc.HelloServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message = "Hello %s!" %request.name)

if __name__ == "__main__":
    print('Started gRPC Server..')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
    hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)