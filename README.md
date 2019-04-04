# Scrappy project

Tiene la funcionalidad de todos los ejecercicios que se propusieron en el pdf 

##Ejercicio 1

#####Tarea 1
```sql
SELECT count(*)
FROM empresa.empleados WHERE ciudad_dep='Lleida' and sueldo > 200000;
```
El resultado fue 0

#####Tarea 2

```sql
SELECT *
FROM empresa.empleados WHERE apellido like 'T%';
```
El resultado fue 

|codigo	       |nombre  |apellido |sueldo  |nombre_dep|ciudad_dep|codigo_proy
|--------------|:------:|:-------:|:------:|:------  :|:------  :|---------:|
|6	           |Laura	|Tort	  |21584   |PROGR	  |Tarragona |3

#####Tarea 3

```sql
INSERT INTO empresa.empleados VALUES(1, 'Pedro', 'Revenga', 24154, 'GESTR', 'Cádiz', NULL);

```

Devuelve un error porque no existe el Deparmento GESTR
 

#Ejercicico 2

Estan resueltos en el script exercices y se exponen bajo los endpoints /palindrome/{palabra} y /factorial/{numero} 



#Ejericio3

Para ejecutar el programa hacer ``` pip install -r requirements.txt```
Y despues ``` cd /src ``` y ```python main.py```

Existen dos endpoint uno es para indexar los datos en  http://127.0.0.1:5000/index y otro para recuperlos en http://127.0.0.1:5000/teams que devuelve los equipos en json
