FROM nginx:latest

# Copy static frontend files
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Copy nginx reverse proxy configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

