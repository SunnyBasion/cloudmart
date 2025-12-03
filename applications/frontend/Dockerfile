FROM nginx:alpine

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy frontend files
COPY index.html .
COPY app.js .

# Expose port 80 for Azure
EXPOSE 80

