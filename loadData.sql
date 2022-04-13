\c enunciados;


/* Carreras */
INSERT INTO public."Enunciados_carreras"(nombre_carrera)
	VALUES
	('IngenieríaCivilInformática'),
	('IngenieríadeEjecuciónenComputacióneInformática'),
	('IngenieríaCivilBiomédica'),
	('IngenieríaCivilenTelemática'),
    ('IngenieríaCivilMecatrónica');
	
/* Roles */
INSERT INTO public."Enunciados_roles"(nombre_rol)
	VALUES
	('Estudiante'),
    ('Profesor'),
    ('QA');

/* Usuarios */
INSERT INTO public."Enunciados_usuarios"(apellido1,apellido2,nombres,correo,password,carrera_id,rol_id,date_joined,email,first_name,is_active,is_staff,is_superuser,last_login,last_name)
	VALUES
	('Perez','Tapia','Hector Campos','hector.peta@gmail.com','asd',1,1, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Suarez','Ruiz','Edgar Ruiz','edsuru@live.cl','asd',1,1, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Ferrer','Gutierrez','Arturo Garrido','ferrerartu@smail.com','asd',1,2, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Pascual','Jiménez','Dorotea Morales','doropascual@hotmail.cl','asd',1,2, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Mora','Saez','Asunción Moreno','asumoreno@gmail.com','asd',1,3, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Hidalgo','Méndez','Reinaldo Mendez','reihidalgo@hotmail.cl','asd',2,3, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Juanes','Tapia','Alberto Esteban','albertoesteban@gmail.com','asd',3,3, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Suazo','Jara','Gerardo Juan','gejusuja@live.cl','asd',4,3, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Mendez','Román','Arturo Luis','arturoluis@smail.com','asd',5,3, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Labarca','Lara','Trinidad Kristina','trinikri@hotmail.cl','asd',1,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Cancino','Kri','Juan Pablo','jpcancino@gmail.com','asd',2,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Bielsa','Nilo','Fernando Lucas','ferbielsanilo@hotmail.cl','asd',3,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Rojas','Heller','Joaquin Cristobal','joacorojas@hotmail.cl','asd',4,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Linton','Cruz','Victoria Justa','vickylin@hotmail.cl','asd',5,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Lopez','Rodriguez','Sofía Javiera','sofilopez@gmail.com','asd',1,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Bravo','Caro','Gastón Bastián','bravogaston@hotmail.cl','asd',2,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Truman','Linetti','Julieta Francisca','julitruman@hotmail.cl','asd',3,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Catrileo','Yanka','Karla Constanza','karlacatrileo@gmail.com','asd',4,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd'),
	('Gonzales','Rubilar','Linda Flor','lindaflor@hotmail.cl','asd',5,4, '2020/10/10', 'asd', 'asd', False, False, False, '2020/10/10', 'asd');

/* Enunciados */
INSERT INTO public."Enunciados_enunciados" (titulo,enunciado,tipo)
	VALUES
	('Pares','Llevar a cabo un programa en Python que compare 2 listas de números, revisando si la suma de cada número de la lista 1 con el de la lista 2 dan como resultado un número par. Lista 1: [1,2,3,4]. Lista 2: [1,2,2,1]','Orden'),
	('Sumatoria','Crear un programa en Python que lleva a cabo una sumatoria de 1 desde el 1 al 10','Ciclos'),
	('Encuentra palabra','Llevar a cabo un programa en Python que busque una palabra específica en un texto, y retorne si la palabra existe en el mismo y la cantidad de veces que aparece','Búsqueda'),
	('Buscador de Aes','Construya un programa en Python que recibiendo como entrada una secuencia aleatoria de letras, identifique la
secuencia mas larga de aes.
Ejemplo:
Entrada: nvfanivnauoyvbfearbueafgaapmlibtgsaaaaarfubueyrarghsog
Salida: aaaaa','Búsqueda'),
	('Busca vocal','Dada una lista de palabras, implemente un programa en lenguaje Python que entregue como salida una lista con todas
las palabras que contengan una vocal en su posici ́on central.
Ejemplo:
Entrada: [’Canta’, ’oh’, ’diosa’, ’la’, ’colera’, ’del’, ’Pelida’, ’Aquileo’, ’colera’, ’funesta’, ’que’, ’causo’, ’infinitos’, ’males’,
’a’, ’los’, ’aqueos’, ’y’, ’precipito’, ’al’, ’Hades’, ’muchas’, ’almas’, ’valerosas’]
Salida: [’diosa’, ’del’, ’Aquileo’, ’funesta’, ’que’, ’causo’, ’a’, ’los’, ’precipito’]','Búsqueda'),
	('Sumas','Para una secuencia de números separados por espacios, construya un programa que entregue como resultado una lista,
donde cada elemento sea la suma de los dígitos de cada uno de los números de la lista de entrada.
Ejemplo:
Entrada: 36 5 0 56 987 23
Salida: [9, 5, 0, 11, 24, 5]
Tip: El m ́etodo split(str) retorna una lista con substrings de un String como elementos, utilizando str como separador. Si
no se especifica el separador, se utiliza por defecto el espacio en blanco.','Lógica'),
	('Registros','Considere el registro de las calificaciones de un curso en el siguiente formato: [[Nombre(String), Calificaci ́on(Float)]]
Construya un programa en Python que entregue las siguientes salidas:
Lista con los nombres de los alumnos aprobados.
Lista con los nombres de los alumnos que deben rendir examen (3.0≤ calificaci ́on ≤3.9).
Lista con los nombre de los alumnos reprobados.
Lista con nombre y nota del o los alumnos con mejor calificaci ́on.
Lista con nombre y nota del o los alumnos con peor calificaci ́on.
Calificaci ́on promedio del curso.
Ejemplo:
Entrada: [[’Felipe Echeverría’, 2.2],[’María Pérez’, 5.6],[’Rosa Navarro’, 3.6],[’Francisco Chavez’, 5.0]]
Salida:
La lista de alumnos reprobados es: [’Felipe Echeverría’]
La lista de alumnos que rinden examen es: [’Rosa Navarro’]
La lista de alumnos aprobados es: [’María Pérez’, ’Francisco Chavez’]
La peor calificación es: [[’Felipe Echeverría’, 2.2]]
La mejor calificación es: [[’María Pérez’, 5.6]]
El promedio de las calificaciones es: 4.1
Nota: Considere que todas las calificaciones se encuentran en el rango 0.0 hasta 7.0.','Estructuras'),
	('Histograma','Construya un programa en Python que recibiendo como entrada una lista de números enteros, dibuje un histograma
utilizando un caracter.
Ejemplo.
Entrada: [2,4,3,5]
Salida:

*
* *
* * *
* * * *
* * * *

Recomendación: max(iterable) retorna el mayor elemento de un objeto iterable.','Lógica'),
	('Traducción','El análisis de frecuencias, estudia estadísticamente la aparición de letras o símbolos en un idioma. Construya un progra-
ma en Python que comprima un texto mediante el reemplazo por símbolos, de las secuencias de dos letras más frecuentes

del idioma español.

Secuencia es en el de la os ar ue ra re
Simbolo # $ & % ( / * + ? !

Ejemplo.
Entrada: en un lugar de la mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de
los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor.
Salida: $ un lug* % ( mancha, % cuyo nomb! no quiero acord*me, no ha mucho tiempo q+ vivia un hidalgo % l/ % (nza $
astillero, ad*ga antigua, rocin f(co y galgo cor!dor.
Considere: El texto de ingreso en minúsculas y sin tildes.
Restricción: No utilice el método replace().

Recomendación: string.find(str) determina si str se encuentra en string, en caso de encontrarse, retorna el  índice de comienzo de str en string en caso contrario retorna -1.','Búsqueda'),
	('Factorial','Construya un programa que entregue como salida el factorial de un número n.
Ejemplo.
Entrada: 6
Salida: 720
Considere: 0!=1','Lógica'),
	('A hexadecimal','Construya un programa que reciba como entrada por pantalla un n ́umero en base 10 y que muestre su equivalente en
hexadecimal.
Ejemplo.
Entrada: 20266
Salida: 4f2a','Lógica'),
	('Encuentra palabra','Llevar a cabo un programa en Python que busque una palabra específica en un texto, y retorne si la palabra existe en el mismo y la cantidad de veces que aparece','Búsqueda'),
	('Signos','Llevar a cabo un programa en Python que a partir de el día y mes de una persona, pueda entregar el signo zodiacal al cual pertenece esa persona','Lógica');



/* Datos */
INSERT INTO public."Enunciados_datos"(fecha_inicio,fecha_termino,errores,id_enunciado_id,id_estudiante_id)
	VALUES
	(CURRENT_TIMESTAMP(0),CURRENT_TIMESTAMP(0),2,1,1);


END;

$$ LANGUAGE 'plpgsql';