FROM nginx:alpine
RUN apk add --no-cache openrc nginx-mod-http-image-filter nginx-mod-http-upstream-fair;

RUN rm /usr/share/nginx/html/index.html
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
COPY index.html /usr/share/nginx/html/
COPY queen.mp3 /usr/share/nginx/html/
COPY vader.jpg /usr/share/nginx/html/



EXPOSE 80