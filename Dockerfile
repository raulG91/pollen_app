FROM python:3.12

#Create work directory and copy content
WORKDIR /app
COPY . .

#Create virtual environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV VIRTUAL_ENV=/app/.venv_docker
RUN python3.12 -m venv $VIRTUAL_ENV

#Install app requirements 
RUN pip install -r requirements.txt

#Run docker app 
CMD reflex run --env prod


