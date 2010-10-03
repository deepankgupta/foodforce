#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/06/2008 
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
upgrade_text_house = ["Cabañas sería actualizado a ladrillo y mortero de barro y chozas con techo de paja." "Cada cabaña contara con un baño letrina.", "Conexión eléctrica se han proporcionado a cada cabaña."]
upgrade_text_hospital = ["Los hospitales se han actualizado a ladrillo y mortero de barro y techo de paja hospitales.", "Los hospitales han sido reformadas y rellena con equipos de investigación.", "Los hospitales han sido siempre con la electricidad y se han proporcionado con techo ondulado . "]
upgrade_text_school = ["Las escuelas se han actualizado a ladrillo y mortero de barro y de la escuela con techo de paja.", "capacidad de la Escuela para el número de niños que pueden ser educados en la escuela se ha incrementado con Upgradation de muebles.", "Las escuelas han sido siempre con la electricidad "]
upgrade_text_workshop = ["Los talleres se han actualizado a ladrillo y mortero de barro y techo de paja del taller.", "Instalación de la chimenea y las herramientas de mecanizado han hecho.", "talleres de trabajo se proporcionan letrina para los trabajadores al descanso y también se han electrificado sido . "]
upgrade_text_farm = ["Las granjas se va a actualizarse a fin de que sería el aumento de la producción.", "Los habitantes del pueblo se va a enseñar acerca de la agricultura de cultivos varios, para que puedan crecer los cultivos de muchos en la misma granja.", "El aldeanos van a ser enseñados acerca de cómo utilizar los fertilizantes de las granjas para aumentar su productividad. "]
upgrade_text_well = ["La actualización de un bien aumenta la producción de agua", "Actualización de un bien aumenta la producción de agua", "Actualización de un bien aumenta la producción de agua"]

upgrade_text = {'HOUSE':upgrade_text_house, 'HOSPITAL':upgrade_text_hospital, 'WORKSHOP':upgrade_text_workshop, 'SCHOOL':upgrade_text_school,'FOUNTAIN':upgrade_text_well, 'FARM':upgrade_text_farm}

trailer_text = ["LA POBREZA ES EL HAMBRE \n\nHUNGER ES LA POBREZA \n\nWFP y Food Force como objetivo romper este círculo vicioso CICLO",
                "EN CASO DE DESASTRES \n \nALIMENTOS PFNM TRAE AL HAMBRE \ n\nFOOD TRAE LA FUERZA Y EL ESPÍRITU DEL CONOCIMIENTO A LA remontada",
                "AIM-GESTIÓN DE CRISIS, reconstruir sus vidas y restablecer la paz, \n \nPROPSPERITY Y SOSTENIBILIDAD",
                "ÚNETE A LA FUERZA DE LOS ALIMENTOS",
                "AYUDAR A SU GENTE SE física, social, \n\nMENTALLY ESPIRITUALMENTE Y SALUDABLE",
                "Cultivar alimentos \n\nTRADE ALIMENTOS \n\nNMAKE SU PUEBLO AUTOSUFICIENTE \n\nGIVE SU COMUNIDAD una dieta equilibrada",
                "Tú decides \n\npara crecer? \n\nPARA VENDER? \n\n COMPRAR? \n\nWHERE PARA INVERTIR?",
                "EI DECISIONES DE CRECIMIENTO SOSTENIBLE \n\nBREAKING EL CIRCULO VICIOSO DEL HAMBRE Y LA POBREZA"]




instruction_text = ["Bienvenido a la aldea de Gokul. \n\nJoin la Fuerza y la Alimentación que su comunidad sea saludable y el pueblo auto-suficiente. \n\nNo se puede \n\nde alimentos a crecer. \n\nBuy alimentos. \n\nproductos de Comercio. \n\nayudar a satisfacer las necesidades básicas de su comunidad:.. \n\nde alimentos, \n agua \n y vivienda \n-Invertir en salud y educación ",
                    "Casa Vida \n\nHouse \ninguno por familia-Ayude a construir vivienda para vivir seguro y saludable. \n\n actualización nSanitation \nAyúdanos a un retrete inodoro por casa. \nFincas n \ Nsetup nFarm \ y ayudar a proporcionar una dieta equilibrada para su comunidad. \n\nWELL \nWater es la clave para la supervivencia y sustainence. \nUpgrade su pozo para obtener más agua. "
                    "Comunidad \n\nmateriales nBuild nWorkshop \n y herramientas para la construcción de las instalaciones. \n\nSchool \nInvest en la educación, invertir en el crecimiento. Construya las escuelas. Utilice barras de progreso para medir el desempeño. \nHospitales \n\nHospital \nBuild para la prevención y cura de las enfermedades, ofrecer la vacunación a los niños \ny organizar eventos para la higiene de la comunidad. "
                    "Recursos \n\n Agua Alimentos \n\n Medicina \n Libros \nHerramientas \n\n Materiales de Construcción",
                    "Dieta equilibrada Alimentos \n\nProvide a tu pueblo por una comunidad saludable, activo y fuerte. \nEn Gokul, a crecer, comprar y comer \n\nRice \ nRice es el alimento básico y fuente importante de hidratos de carbono en Sheylan. \n\nFruit y hortalizas \nSource de vitaminas y minerales. Alrededor de un tercio de la dieta de todos los aldeanos en Gokul se compone de frutas y verduras. \nGrow en explotación, consumo y comercio de los mismos (en kilogramos) en el mercado. "
                    "Los frijoles \nSource de proteínas en Sheylan. Cultivarlas en granjas, consumo y comercio de los mismos (en kilogramos) en el mercado. \n\nSugar, Sal y Aceite \nEllos se añaden a los elementos de su comida. Comprarlos en el mercado para su de la familia. \nSugar y aceite de ayudarle a proporcionar los hidratos de carbono y grasas. Sal le proporciona minerales. \nKeep sus cantidades equilibradas. "
                    "El agua \nWater es la clave para la supervivencia y sustainence. \nUtilizado para beber, lavar y el aumento de los cultivos. \nMaintain y mejorar los pozos de un suministro constante de agua limpia. \n\nMedicine \nMedicine para el tratamiento y cura de enfermedades. \n\nVaccination para los niños \nEnsure un suministro constante de medicamentos para la caja fuerte y saludable Sheylan. "
                    "Los libros \nBooks están destinados a jóvenes y viejos, mantenerlos bien mi amigo, su peso es de oro. \nMaintain los libros existentes en las bibliotecas escolares, y el orden más necesaria cada vez. Libros sobre la nutrición, la higiene y la agricultura ayudará a la comunidad para adaptarse las mejores prácticas en Sheylan. \nTools \n\nmake o comprar herramientas para el mantenimiento de campos y cultivos, y para \nconstruction de las instalaciones. \n\nBricks. \nProduce ellos en el taller, o comprarlos en el mercado de la construcción de las instalaciones . "]

credits_text = "Desarrolladores: \n      Mohit Taneja\n         Grivan Thapar\n          Rupinder Singh\n\n         Administrador \n  Deepank Gupta \n\n Pruebas de crédito: \n Chakkilam Infotech limitada \n\n ilustraciones y el logotipo de: \n Silke Buhr y Graham Bell del PMA "


about_us_text = 'Somos un grupo de programadores interesados para que las plataformas digitales como los portátiles de servir como plataformas para proporcionar educación y formación al tiempo que el alumno se sienten comprometidos y entretenido durante toda la experiencia. Foodforce2 es uno de esos intentos de hacer que se conscientes de hambre en el mundo y la pobreza, dándole la oportunidad de crear comunidades auto-sostenible y en el proceso que tiene una aplicación de otras habilidades básicas de matemáticas y conocimientos teóricos. \n\nPor favor escríbanos a foodforce2@gmail.com de las opiniones, comentarios e ideas para \ndevelopment. \n\nSe adelante a oír de usted.'

# Área de visualización de texto

indicators_text = ["barras de progreso"]
ind_namelist = ('Vivienda', 'Nutrición', 'Salud', 'Educación', 'Training')
resources_text = ["Recursos"]
money_text = ["El dinero"]
time_text = ['Tiempo transcurrido','Nivel Sólo empezar ',' Años ',' meses ',' Días ']
mpwr_resources_text = ["Mano de Obra de distribución"]
mpwr_list_names = ('Población Total', 'Al abrigo de personas ',' gente educada ',' Gente Sana ',' La gente de la Fed', 'Las personas empleadas')
facilities_list = ("Chozas", "Escuela", "Hospitales", "Talleres", "las granjas", "Wells")
num_text = "Número"
level_text = "Nivel"

list_gen_res = ('agua', 'Ladrillo', 'Herramientas', 'Medicamentos', 'Libros')
list_food_res = ('arroz', 'Frutas y Hortalizas', 'Habichuelas', 'Sugar', 'Salt', 'aceite')

earthquake_hit_text = "Su pueblo ha sido golpeada por un terremoto"

# GUI texto butons

objective = ["actual Objetivo"]

setup_text = ["Configurar una instalación para su pueblo", "¿Qué le gustaría crear?", "Por favor, seleccione una instalación para ver su estado y necesidades", "Por favor, seleccione un Fondo de Apoyo para la construcción", "Fondo ha sido construir "," Configuración de la Granja "," Balance de la gráfica de barras para seleccionar los porcentajes de los diferentes alimentos que desea crecer en la granja "," Set Up "]

setup_fac_exceptions = {'no_exception':"",'stopped': "No se puede construir una instalación cuando se ha detenido temporalmente, intente edificio cuando se reanude", 'low_manpower':" Usted no tiene suficiente mano de obra para construir las instalaciones , por favor, intente más tarde ",'max_limit': "No se puede configurar más edificios de este servicio, intentar la creación de otro establecimiento", 'low_resource':" Usted no tiene suficientes% (de recursos) s para construir la instalación, por favor, intente más tarde "}

setup_format_text = ['Hay %(number)s %(facility)s\'s en el pueblo.\nNeeds %(costbuild)s y %(manbuild)s las personas para construir.\n Requires %(costrun)s y %(manrun)s las personas a ejecutar.\n\n %(resafter)s']

upgrade_fac_text = ["Actualizar Fondo", "Por favor, seleccione un Fondo de Apoyo a la actualización", "Por favor, seleccione una instalación para ver la próxima actualización", "Por favor, seleccione un Fondo de Apoyo para la modernización", "Fondo se ha actualizado"]

upgrade_fac_exceptions = {'no_exception':"",'stopped': "No se puede actualizar una instalación cuando se ha detenido temporalmente, intente actualizar cuando se reanude", 'none_setup':" Debe configurar una instalación de primera actualización que ",'low_res': "Usted no tiene suficientes% (de recursos) s para actualizar la instalación, por favor, intente más tarde", 'max_level':" Fondo ha alcanzado su nivel máximo no puedo actualizar ahora "}

upgrade_format_text = ['%(text)s\nHay %(number)s %(facility)s\'s en el pueblo.\nNeeds %(costupgrade)s para actualizar.\n\n%(resafter)s']

buysell_text = ["Compra y venta de Recursos", "Comercio con los Pueblos de pares", "Bienvenido al mercado de Sheylan, donde puedes intercambiar recursos. Seleccione el elemento que desea comprar o vender en la columna de la izquierda, entrar en el cantidad, y luego elegir comprar o vender "," Por favor, seleccione un recurso para el Comercio "]

buysell_exceptions = {'no_exception': "El pueblo ha cambiado el recurso que exigía", 'zero_qty':" La cantidad debe ser mayor que cero ",'low_qty': "El pueblo no tiene la cantidad suficiente para vender este recurso a mercado ",'low_money': "Usted no tiene suficiente dinero para comprar este recurso por favor, cambia la cantidad o intente más tarde", 'low_mkt_qty':" El mercado no tiene la cantidad suficiente para vender este recurso a pueblo",'overflow' : "El pueblo no puede almacenar tanta cantidad de recursos que debe tratar de usar el dinero para comprar otros recursos"}

fac_running_exceptions ={'insufficient_res': "Facility %(facility)s se ha detenido temporalmente debido a insuficientes %(resource)s en el pueblo!",'resume': "Fondo %(facility)s se ha reanudado."}

fac_name = ['cabaña', 'Hospital', 'Taller', 'School', 'Granja', 'Bien']

food_ingredient_list = ['arroz', 'Frutas y \nVegetables', 'Habichuelas']

Upgrade_box_text = ['Actualizaciones']

buysell_window_text = ['Recursos', 'Pueblo', 'Cantidad', 'Precio', 'Mercado']

buysell_window_buttons = ['Comprar', 'Vender', 'Close']

panel_text = ['Build', 'Upgrade', 'Mercado']

exceptions_text = ['del pueblo no tiene suficiente dinero para comprar los recursos', 'No hay suficientes recursos en el pueblo para el comercio']



# El texto de Foodforce2.py

Language = ['Inglés','Español']

message_window_text = ['mensaje']

start_new_game = ['nuevo comienzo Juego']

resume_saved_game = ['Reanudar guardados Juego']

resume_game = ['Reanudar Juego']

start_game_again = ['Start Game Again ']

save_current_level = ['Guardar actual nivel']

control_button_text = ['controles']

exit_button_text = ['Exit']

instructions_window_text = ['Guía']

about_button_text = ['Nosotros']

language_window_text = ['Elegir idioma']

storyboard_window_text = ['Elige Storyboard']

skip_text = ['Skip']

play_text = ['Play']

instructions_next_text = ['Siguiente>']

instructions_pre_text = ['<Anterior']

close_window_text = ['Close']

# Texts from level_change

loading_text = ['Cargando ....']

# Texts from chat

proceed_text = ['PARTICIPAR : Para mostrar el conjunto de chat                  CES: Para saltar chat']