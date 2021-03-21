FROM node:15-alpine as build-stage

WORKDIR /app

COPY package.json ./
RUN yarn install

COPY . .
RUN yarn build

ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=3000

CMD ["yarn", "start"]
