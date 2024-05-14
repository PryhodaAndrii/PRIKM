FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./Site-main/. /usr/share/nginx/html/