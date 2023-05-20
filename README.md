# proyectopython

Desafío Técnico: Construir un Pipeline de Datos con Docker y Apache Airflow:

# 1. Configurar Apache Airflow con Docker:
# a. Instalar Docker en tu máquina local.
Se realiza la instalaciòn de Docker version 23.0.5, build bc4487a

# b. Crear un Dockerfile que incluya las dependencias requeridas y la configuración para
Apache Airflow.

Se crea un archivo llamado dockerfile sin extensiòn alguna con la siguiente consiguraciòn


#para este archivo se Utilizo la imagen  de Python v3.7)
FROM python:3.7
RUN pip install apache-airflow==2.1.4 
ENV AIRFLOW_HOME=C:\Users\USUARIO\airflow\

# configuraciòn del usuario para ingresar a la interface web de airflow
ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True \
    AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.api.auth.backend.default \
    AIRFLOW__WEBSERVER__RBAC=True \
    AIRFLOW__WEBSERVER__USERNAME=juan \
    AIRFLOW__WEBSERVER__PASSWORD=juan


#puerto 8080
EXPOSE 8080

# se realiza la configuraciòn para que despues de la instalaciòn del dockerfile inicie inmediatamente el webserver
# y el panificador (scheduler) Esto evita que aparezca el error al momento de ingresar a la interface web y se puedan subir los archivos dags
CMD ["bash", "-c", "sleep 10 && airflow webserver -p 8080 & airflow scheduler"]


#espera de 10 segundos para la ejecuciòn, 
RUN sleep 10

# inicializaciòn de la base de datos
RUN airflow db init

# creaciòn del perfil y el rol.
RUN airflow users create \
    --username $AIRFLOW__WEBSERVER__USERNAME \
    --password $AIRFLOW__WEBSERVER__PASSWORD \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email juandedioscamacho@hotmail.com


# c. Construir y ejecutar el contenedor de Airflow utilizando el Dockerfile.

En el powerSherll de windows ingreso a la carpeta cd C:\Juan donde  se encuentra el archivo dockerfile
y ejecuto el siguiente comando para la instalaciòn de la imagen:

- docker build -t airflow-image .

Una vez que la imagen se haya construido correctamente, se ejecuta el siguiente comando para iniciar un contenedor a partir de la imagen

-  docker run -d -p 8888:8080 --name airflow -v C:\Juan\dags:/usr/local/airflow/dags dockerfile 

NOTA: se escogio el puerto 8888

Esto iniciará el contenedor de Docker y mapeará el puerto 8888 de la máquina host al puerto 8080 del contenedor,
lo que te permitirá acceder a la interfaz web de Airflow en [[http://localhost:8080]](http://localhost:8888/home)

en el navegador se accede a la interface web [http://localhost:8888/hom](http://localhost:8888/home) con el nombre de usuario y contraseña
juan/juan para iniciar sesión. 

Vista del contenedor en Docker: https://github.com/juancamacho11/proyectopython/blob/main/CreaciondelCONTENEDOR.PNG

Para subir el DAGs se usa el siguiente comando (se especifica el nombre del contenedor y la ruta donde se instala):
docker cp Dags.py airflow:/usr/local/lib/python3.7/site-packages/airflow/example_dags/

en este caso se subieron las 3 tareas de PythonOperator que se encuentran en los archivos Extraer, cargar y Transformar llamadas:
-	Extraer_data_dag
-	Transformar_data_dag
- Cargar_data_dag

Ademas se crea el archivo Dags.py donde se especifican mediante el BashOperator la ejecuciòn de las tareas anteriormente estipuladas.
- Dag_Tareas

Vista de la creaciòn delas tareas en AIRFLOW: https://github.com/juancamacho11/proyectopython/blob/main/TareasDAGS.PNG
