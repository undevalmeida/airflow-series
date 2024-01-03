FROM quay.io/astronomer/astro-runtime:9.6.0


ENV AIRFLOW_VAR_ENV_VAR_TEST='abacate'
ENV AIRFLOW_VAR_ENV_JSON_VAR_TEST='{"key1":"value1", "key2":"value2"}'

ENV AIRFLOW_CONN_MY_PROD_DATABASE = '{\
    "conn_type":"my-conn-type", \
    description":"my-description",\
    "host":"my-host",\
    "login":"admin",\
    "port":0,\
    "schema":"default",\
    "extra":"teste",\
    "password":"admin"\
}'