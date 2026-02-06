# ubuntu base image
FROM ubuntu:latest

# cleaning up apt cache to keep image small
RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# copy config, certificates and content
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html
COPY ssl/nginx.crt /etc/nginx/ssl/nginx.crt
COPY ssl/nginx.key /etc/nginx/ssl/nginx.key


# xpose the ports
EXPOSE 8080 8081 443

# start nginx in the background so the container do not exit
CMD ["nginx", "-g", "daemon off;"]