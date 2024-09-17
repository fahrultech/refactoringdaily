FROM nginx:alpine

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the default server block configuration for Certbot
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf

# Create directory for certbot challenges
RUN mkdir -p /var/www/certbot

# Copy the Diffie-Hellman parameter
COPY ssl/dhparam.pem /etc/ssl/certs/dhparam.pem