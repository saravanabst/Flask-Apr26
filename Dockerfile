FROM python:3.12.10-slim-bullseye
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code
COPY ./ ./
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["python", "-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0"]
