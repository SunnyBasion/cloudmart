FROM nginx:latest

# Remove default nginx HTML
RUN rm -rf /usr/share/nginx/html/*

# Copy frontend static assets into nginx root
COPY src/ /usr/share/nginx/html/

# Copy nginx reverse proxy configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

