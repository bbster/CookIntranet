#Base Imange
FROM postgres:latest

#Copy init script
COPY docker-compose/db/create.sql /docker-entrypoint-initdb.d/

# Port
EXPOSE 5432

# Run
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]