FROM node:lts-alpine

WORKDIR /home/spa

COPY package*.json ./
RUN npm install -f
COPY . .

EXPOSE 3000

ENTRYPOINT [ "./entrypoint.sh" ]