# user-demo
Simple application to demonstrate the differences in container user permissions between OpenShift and Kubernetes.

The application is a simple Flask REST API with two endpoints:
* `/` - Returns user and group information for the user the container runs as
* `/write` - Attempts to write a file to `/code` (randomly generated name between 1000-9999)

The two Dockerfiles demonstrate the different approaches to defining container users:
* `Dockerfile.root` - A simple Dockerfile without any special handling for users, resulting in the container running as root.
* `Dockerfile.user` - Takes extra steps to set user and application permissions to ensure the container does not run as root.

Images have been built with each of these Dockerfiles:
* `quay.io/jdob/user-demo-bad:latest` - built using Dockerfile.root
* `quay.io/jdob/user-demo-good:latest` - built using Dockerfile.user
