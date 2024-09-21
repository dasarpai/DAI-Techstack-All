FROM node:12-alpine
# Adding build tools to make yarn install work on Apple silicon / arm64 machines
RUN apk add --no-cache python2 g++ make
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]

# FROM node:12.16.3
# WORKDIR  /code 
# ENV PORT 80 
# COPY package.json /code/package.json  
# RUN npm install 
# COPY . /code 
# CMD ["node", "src/server.js"]
