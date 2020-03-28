# gRPC-python
This is a demo of client-server communication using gRPC.

Use below command to generate protocol files from .proto file.
e.g. python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. hello.proto
