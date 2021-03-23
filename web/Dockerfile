FROM node:15-alpine as build

WORKDIR /app

COPY package.json ./
RUN yarn install

COPY . .
RUN yarn generate


FROM nginx:1.19.6-alpine
COPY --from=build /app/dist /app/web

ARG DOMAIN

COPY docker/conf.d/*.conf /etc/nginx/conf.d/
COPY docker/nginx.conf /etc/nginx/nginx.conf

RUN sed -i "s/_DOMAIN_/${DOMAIN}/g" /etc/nginx/conf.d/*.conf

RUN rm /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
