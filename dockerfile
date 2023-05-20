FROM python:3.7
RUN pip install apache-airflow==2.1.4 
ENV AIRFLOW_HOME=C:\Users\USUARIO\airflow\


ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True \
    AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.api.auth.backend.default \
    AIRFLOW__WEBSERVER__RBAC=True \
    AIRFLOW__WEBSERVER__USERNAME=juan \
    AIRFLOW__WEBSERVER__PASSWORD=juan



EXPOSE 8080
CMD ["bash", "-c", "sleep 10 && airflow webserver -p 8080 & airflow scheduler"]

RUN sleep 10

RUN airflow db init

RUN airflow users create \
    --username $AIRFLOW__WEBSERVER__USERNAME \
    --password $AIRFLOW__WEBSERVER__PASSWORD \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email juandedioscamacho@hotmail.com
