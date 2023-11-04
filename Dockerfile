FROM python:3.11

RUN apt update && apt install gcc -y
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

WORKDIR /pipyao_bot

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY bot.py ./

CMD ["python","-u", "./bot.py"]
