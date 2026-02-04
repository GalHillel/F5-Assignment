# base image must be ubuntu
FROM ubuntu:latest

# update packages and install nginx
RUN apt-get update && apt-get install -y nginx

# copy configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# copy html file to the directory we defined in the config
COPY index.html /var/www/html/index.html

# xpose the ports
EXPOSE 8080 8081

# start nginx in the foreground so the container doesn't exit
CMD ["nginx", "-g", "daemon off;"]