# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy ONLY the necessary scripts into the container
COPY batch_modernize.py .
COPY generate_test_data.py .
COPY run_migration.sh .

# Give execution permission to the bash script
RUN chmod +x run_migration.sh

# Execute the script when the container starts
CMD ["./run_migration.sh"]
