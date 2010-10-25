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
upgrade_text_house = [u'Cabañas sería actualizado a ladrillo y mortero de barro y chozas con techo de paja.', 
                      u'Cada cabaña contara con un baño letrina.', 
                      u'Conexión eléctrica se han proporcionado a cada cabaña.']
upgrade_text_hospital = [u'Los hospitales se han actualizado a ladrillo y mortero de barro y techo de paja hospitales.', 
                         u'Los hospitales han sido reformadas y rellena con equipos de investigación.', 
                         u'Los hospitales han sido siempre con la electricidad y se han proporcionado con techo ondulado . ']
upgrade_text_school = [u'Las escuelas se han actualizado a ladrillo y mortero de barro y de la escuela con techo de paja.', 
                       u'capacidad de la Escuela para el número de niños que pueden ser educados en la escuela se ha incrementado con Upgradation de muebles.', 
                       u'Las escuelas han sido siempre con la electricidad ']
upgrade_text_workshop = [u'Los talleres se han actualizado a ladrillo y mortero de barro y techo de paja del taller.', 
                         u'Instalación de la chimenea y las herramientas de mecanizado han hecho.', 
                         u'talleres de trabajo se proporcionan letrina para los trabajadores al descanso y también se han electrificado sido . ']
upgrade_text_farm = [u'Las granjas se va a actualizarse a fin de que sería el aumento de la producción.', 
                     u'Los habitantes del pueblo se va a enseñar acerca de la agricultura de cultivos varios, para que puedan crecer los cultivos de muchos en la misma granja.', 
                     u'El aldeanos van a ser enseñados acerca de cómo utilizar los fertilizantes de las granjas para aumentar su productividad. ']
upgrade_text_well = [u'La actualización de un bien aumenta la producción de agua', 
                     u'Actualización de un bien aumenta la producción de agua', 
                     u'Actualización de un bien aumenta la producción de agua']

upgrade_text = {u'HOUSE':upgrade_text_house, 
                u'HOSPITAL':upgrade_text_hospital, 
                u'WORKSHOP':upgrade_text_workshop, 
                u'SCHOOL':upgrade_text_school,
                u'FOUNTAIN':upgrade_text_well, 
                u'FARM':upgrade_text_farm}

trailer_text = [u'LA POBREZA ES EL HAMBRE \n\nHUNGER ES LA POBREZA \n\nWFP y Food Force como objetivo romper este círculo vicioso CICLO',
                u'EN CASO DE DESASTRES \n \nALIMENTOS PFNM TRAE AL HAMBRE \ n\nFOOD TRAE LA FUERZA Y EL ESPÍRITU DEL CONOCIMIENTO A LA remontada',
                u'AIM-GESTIÓN DE CRISIS, reconstruir sus vidas y restablecer la paz, \n \nPROPSPERITY Y SOSTENIBILIDAD',
                u'ÚNETE A LA FUERZA DE LOS ALIMENTOS',
                u'AYUDAR A SU GENTE SE física, social, \n\nMENTALLY ESPIRITUALMENTE Y SALUDABLE',
                u'Cultivar alimentos \n\nTRADE ALIMENTOS \n\nNMAKE SU PUEBLO AUTOSUFICIENTE \n\nGIVE SU COMUNIDAD una dieta equilibrada',
                u'Tú decides \n\npara crecer? \n\nPARA VENDER? \n\n COMPRAR? \n\nWHERE PARA INVERTIR?',
                u'EI DECISIONES DE CRECIMIENTO SOSTENIBLE \n\nBREAKING EL CIRCULO VICIOSO DEL HAMBRE Y LA POBREZA']




instruction_text = [u'Bienvenido a la aldea de Gokul. \n\nJoin la Fuerza y la Alimentación que su comunidad sea saludable y el pueblo auto-suficiente. \n\nNo se puede \n\nde alimentos a crecer. \n\nBuy alimentos. \n\nproductos de Comercio. \n\nayudar a satisfacer las necesidades básicas de su comunidad:.. \n\nde alimentos, \n agua \n y vivienda \n-Invertir en salud y educación ',
                    u'Casa Vida \n\nHouse \ninguno por familia-Ayude a construir vivienda para vivir seguro y saludable. \n\n actualización nSanitation \nAyúdanos a un retrete inodoro por casa. \nFincas n \ Nsetup nFarm \ y ayudar a proporcionar una dieta equilibrada para su comunidad. \n\nWELL \nWater es la clave para la supervivencia y sustainence. \nUpgrade su pozo para obtener más agua. '
                    u'Comunidad \n\nmateriales nBuild nWorkshop \n y herramientas para la construcción de las instalaciones. \n\nSchool \nInvest en la educación, invertir en el crecimiento. Construya las escuelas. Utilice barras de progreso para medir el desempeño. \nHospitales \n\nHospital \nBuild para la prevención y cura de las enfermedades, ofrecer la vacunación a los niños \ny organizar eventos para la higiene de la comunidad. '
                    u'Recursos \n\n Agua Alimentos \n\n Medicina \n Libros \nHerramientas \n\n Materiales de Construcción',
                    u'Dieta equilibrada Alimentos \n\nProvide a tu pueblo por una comunidad saludable, activo y fuerte. \nEn Gokul, a crecer, comprar y comer \n\nRice \ nRice es el alimento básico y fuente importante de hidratos de carbono en Sheylan. \n\nFruit y hortalizas \nSource de vitaminas y minerales. Alrededor de un tercio de la dieta de todos los aldeanos en Gokul se compone de frutas y verduras. \nGrow en explotación, consumo y comercio de los mismos (en kilogramos) en el mercado. '
                    u'Los frijoles \nSource de proteínas en Sheylan. Cultivarlas en granjas, consumo y comercio de los mismos (en kilogramos) en el mercado. \n\nSugar, Sal y Aceite \nEllos se añaden a los elementos de su comida. Comprarlos en el mercado para su de la familia. \nSugar y aceite de ayudarle a proporcionar los hidratos de carbono y grasas. Sal le proporciona minerales. \nKeep sus cantidades equilibradas. '
                    u'El agua \nWater es la clave para la supervivencia y sustainence. \nUtilizado para beber, lavar y el aumento de los cultivos. \nMaintain y mejorar los pozos de un suministro constante de agua limpia. \n\nMedicine \nMedicine para el tratamiento y cura de enfermedades. \n\nVaccination para los niños \nEnsure un suministro constante de medicamentos para la caja fuerte y saludable Sheylan. '
                    u'Los libros \nBooks están destinados a jóvenes y viejos, mantenerlos bien mi amigo, su peso es de oro. \nMaintain los libros existentes en las bibliotecas escolares, y el orden más necesaria cada vez. Libros sobre la nutrición, la higiene y la agricultura ayudará a la comunidad para adaptarse las mejores prácticas en Sheylan. \nTools \n\nmake o comprar herramientas para el mantenimiento de campos y cultivos, y para \nconstruction de las instalaciones. \n\nBricks. \nProduce ellos en el taller, o comprarlos en el mercado de la construcción de las instalaciones . ']

credits_text = u'Desarrolladores: \n      Mohit Taneja\n         Grivan Thapar\n          Rajat Goel\n\n         Administrador \n  Deepank Gupta \n\n Pruebas de crédito: \n Chakkilam Infotech limitada \n\n ilustraciones y el logotipo de: \n Silke Buhr y Graham Bell del PMA '


about_us_text = u'Somos un grupo de programadores interesados para que las plataformas digitales como los portátiles de servir como plataformas para proporcionar educación y formación al tiempo que el alumno se sienten comprometidos y entretenido durante toda la experiencia. Foodforce2 es uno de esos intentos de hacer que se conscientes de hambre en el mundo y la pobreza, dándole la oportunidad de crear comunidades auto-sostenible y en el proceso que tiene una aplicación de otras habilidades básicas de matemáticas y conocimientos teóricos. \n\nPor favor escríbanos a foodforce2@gmail.com de las opiniones, comentarios e ideas para \ndevelopment. \n\nSe adelante a oír de usted.'

# Área de visualización de texto

indicators_text = [u'  Barras de progreso']
ind_namelist = (u'  Vivienda', 
                u'  Nutrición', 
                u'  Salud', 
                u'  Educación', 
                u'  Training')
resources_text = [u'Recursos','sin recursos']
money_text = [u'El dinero']
time_text = [u'Tiempo transcurrido', 
             u'Nivel Sólo empezar ', 
             u' Años ', 
             u' meses ', 
             u' Días ']
mpwr_resources_text = [u'Mano de Obra de distribución']
mpwr_list_names = (u' Población Total', 
                   u' Al abrigo de personas ', 
                   u' Gente educada ', 
                   u' Gente Sana ', 
                   u' La gente de la Fed', 
                   u' Las personas empleadas')
facilities_list = (u'Chozas', 
                   u'Escuela', 
                   u'Hospitales', 
                   u'Talleres', 
                   u'las granjas', 
                   u'Bueno')
num_text = [u'Número']
level_text = [u'Nivel']

list_gen_res = (u' Agua', 
                u' Ladrillo', 
                u' Herramientas', 
                u' Medicamentos', 
                u' Libros')
list_food_res = (u' Arroz', 
                 u' Frutas y Hortalizas', 
                 u' Habichuelas', 
                 u' Azúcar', 
                 u' Sal', 
                 u' Aceite')

earthquake_hit_text = u'Su pueblo ha sido golpeada por un terremoto'

# GUI texto butons

objective = [u'Actual Objetivo']

setup_text = [u'Configurar una instalación para su pueblo', 
              u'¿Qué le gustaría crear?', 
              u'Por favor, seleccione una instalación para ver su estado y necesidades', 
              u'Por favor, seleccione un Fondo de Apoyo para la construcción', 
              u'Fondo ha sido construir ',
              u' Configuración de la Granja ',
              u' Balance de la gráfica de barras para seleccionar los porcentajes de los diferentes alimentos que desea crecer en la granja ',
              u' Set Up ']

setup_fac_exceptions = {u'no_exception':u'',
                        u'stopped': u'No se puede construir una instalación cuando se ha detenido temporalmente, intente edificio cuando se reanude', 
                        u'low_manpower':u' Usted no tiene suficiente mano de obra para construir las instalaciones , por favor, intente más tarde ',
                        u'max_limit': u'No se puede configurar más edificios de este servicio, intentar la creación de otro establecimiento', 
                        u'low_resource':u' Usted no tiene suficientes %(resource)s para construir la instalación, por favor, intente más tarde '}

setup_format_text = [u'Hay %(number)s %(facility)s en el pueblo.\nNeeds %(costbuild)s y %(manbuild)s las personas para construir.\nRequires %(costrun)s y %(manrun)s las personas a ejecutar.\n\n%(resafter)s']

upgrade_fac_text = [u'Actualizar Fondo', 
                    u'Por favor, seleccione un Fondo de Apoyo a la actualización', 
                    u'Por favor, seleccione una instalación para ver la próxima actualización', 
                    u'Por favor, seleccione un Fondo de Apoyo para la modernización', 
                    u'Fondo se ha actualizado']

upgrade_fac_exceptions = {u'no_exception':u'',
                          u'stopped': u'No se puede actualizar una instalación cuando se ha detenido temporalmente, intente actualizar cuando se reanude', 
                          u'none_setup':u' Debe configurar una instalación de primera actualización que ',
                          u'low_res': u'Usted no tiene suficientes% (de recursos) s para actualizar la instalación, por favor, intente más tarde', 
                          u'max_level':u' Fondo ha alcanzado su nivel máximo no puedo actualizar ahora '}

upgrade_format_text = [u'%(text)s\nHay %(number)s %(facility)s en el pueblo.\nNeeds %(costupgrade)s para actualizar.\n\n%(resafter)s']

buysell_text = [u'Compra y venta de Recursos', 
                u'Comercio con los Pueblos de pares', 
                u'Bienvenido al mercado de Sheylan, donde puedes intercambiar recursos. Seleccione el elemento que desea comprar o vender en la columna de la izquierda, entrar en el cantidad, y luego elegir comprar o vender ',
                u' Por favor, seleccione un recurso para el Comercio ']

buysell_exceptions = {u'no_exception': u'El pueblo ha cambiado el recurso que exigía', 
                      u'zero_qty':u' La cantidad debe ser mayor que cero ',
                      u'low_qty': u'El pueblo no tiene la cantidad suficiente para vender este recurso a mercado ',
                      u'low_money': u'Usted no tiene suficiente dinero para comprar este recurso por favor, cambia la cantidad o intente más tarde', 
                      u'low_mkt_qty':u' El mercado no tiene la cantidad suficiente para vender este recurso a pueblo',
                      u'overflow' : u'El pueblo no puede almacenar tanta cantidad de recursos que debe tratar de usar el dinero para comprar otros recursos'}

fac_running_exceptions ={u'insufficient_res': u'Facility %(facility)s se ha detenido temporalmente debido a insuficientes %(resource)s en el pueblo!',
                         u'resume': 'Fondo %(facility)s se ha reanudado.'}

fac_name = [u'Cabaña', 
            u'Hospital', 
            u'Taller', 
            u'Escuela', 
            u'Granja', 
            u'Bien']

food_ingredient_list = [u' Arroz', 
                        u' Frutas y \nVegetables', 
                        u' Habichuelas']

Upgrade_box_text = [u'Actualizaciones']

buysell_window_text = [u'Recursos', 
                       u'Pueblo', 
                       u'Cantidad', 
                       u'Precio', 
                       u'Mercado']

buysell_window_buttons = [u'Comprar', 
                          u'Vender', 
                          u'Cerrar']

panel_text = [u'Construir', 
              u'Actualizar', 
              u'Mercado']

exceptions_text = [u'Del pueblo no tiene suficiente dinero para comprar los recursos', 
                   u'No hay suficientes recursos en el pueblo para el comercio']



# El texto de Foodforce2.py

Language = [u'Inglés',
            u'Español']

message_window_text = [u'Mensaje']

start_new_game = [u'Nuevo comienzo Juego']

resume_saved_game = [u'Reanudar guardados Juego']

resume_game = [u'Reanudar Juego']

start_game_again = [u'Inicio del juego nuevo']

save_current_level = [u'Guardar actual nivel']

control_button_text = [u'Controles']

exit_button_text = [u'Salir']

instructions_window_text = [u'Guía']

about_button_text = [u'Nosotros']

language_window_text = [u'Elegir idioma']

storyboard_window_text = [u'Elige Storyboard']

skip_text = [u'Saltar']

play_text = [u'Escuchar']

instructions_next_text = [u'Siguiente>']

instructions_pre_text = [u'<Anterior']

controls_text = ['Build','Upgrade','Market','Scroll Screen Up','Scroll Screen Down','Scroll Screen Left','Scroll Screen Right','Focus','De Focus',': ','s','u','b','up arrow','down arrow','left arrow','right arrow','f','d','OK']          

close_window_text = [u'Cerrar']

# Texts from level_change

loading_text = [u'Cargando ....']

# Texts from chat

proceed_text = [u'PARTICIPAR : Para mostrar el conjunto de chat                  CES: Para saltar chat']