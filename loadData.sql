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
	('Signos','Llevar a cabo un programa en Python que a partir de el día y mes de una persona, pueda entregar el signo zodiacal al cual pertenece esa persona','Lógica');



/* Datos */
INSERT INTO public."Enunciados_datos"(fecha_inicio,fecha_termino,errores,id_enunciado_id,id_estudiante_id)
	VALUES
	(CURRENT_TIMESTAMP(0),CURRENT_TIMESTAMP(0),2,1,1);


END;

$$ LANGUAGE 'plpgsql';