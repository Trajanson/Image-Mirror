docker build -t image-mirror . &&
docker run --rm -it -p 5000:5000 image-mirror
