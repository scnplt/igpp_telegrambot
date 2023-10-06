FROM python:3.9-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE $PORT
CMD ["python", "bot.py"]
