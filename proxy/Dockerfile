FROM nginx:1.18-alpine

ARG DOMAIN

COPY assets/etc/nginx/conf.d/*.conf /etc/nginx/conf.d/
COPY assets/etc/nginx/nginx.conf /etc/nginx/nginx.conf

RUN sed -i "s/_DOMAIN_/${DOMAIN}/g" /etc/nginx/conf.d/*.conf

RUN rm /etc/nginx/conf.d/default.conf
