FROM cgr.dev/chainguard/redis:latest

COPY redis.conf /etc/redis/redis.conf

EXPOSE 6379

ENTRYPOINT [ "redis-server", "/etc/redis/redis.conf" ]