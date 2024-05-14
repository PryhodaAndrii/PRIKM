FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./Site/. /usr/share/nginx/html/
# зміни