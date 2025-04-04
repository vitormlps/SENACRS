FROM node:lts-alpine

WORKDIR /home/api

COPY package*.json ./
RUN npm install -f
COPY . .

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]