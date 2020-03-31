# gRPC-python
This is a demo of client-server communication using gRPC.

Use below command to generate protocol files from .proto file.
e.g. python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. hello.proto

To run this demo, start grpc server using this command from terminal 'python server.py'. 
Now keep the server started and run grpc client from another terminal by using command 'python client.py'.
