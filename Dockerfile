FROM python:3.10-slim
RUN apt-get update && apt-get install -y sqlite3 nano
WORKDIR /lab
COPY setup_db.py .
COPY validator.py .
COPY oppgave.txt .
RUN python3 setup_db.py
CMD ["/bin/bash"]