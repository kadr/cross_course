proto-gen:
	python -m grpc_tools.protoc -I pkg/grpc/protos --python_out=pkg/grpc/src --pyi_out=pkg/grpc/src  pkg/grpc/protos/*/*.proto
grpc-gen: proto-gen
	python -m grpc_tools.protoc -I pkg/grpc/protos  --grpc_python_out=pkg/grpc/src pkg/grpc/protos/*/*.proto