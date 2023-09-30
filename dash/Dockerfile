FROM python:3.9.2

RUN mkdir -p /home/project/sde_assign_2
WORKDIR /home/project/sde_assign_2
COPY requirements.txt /home/project/sde_assign_2
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/sde_assign_2