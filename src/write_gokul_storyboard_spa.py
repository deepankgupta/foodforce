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

import os
import pickle
storyboard_no = 1
storyboard_list_file = open('storyboard_list.pkl')
pickle.load(storyboard_list_file)
storyboard_name = None
while storyboard_name == None:
    storyboard = pickle.load(storyboard_list_file)
    if storyboard_no == storyboard[0]:
        storyboard_name = storyboard[1]
    
    
def write_data():

    output = open(os.path.join('storyboards',str(storyboard_name),'storyboard_spa.pkl'),'wb')
    
    # Tutorial Mission
    
    text = '\n \n \n \nEn este hermoso país llamado Chile, hay un pueblo Gokul. El pueblo de Gokul se rige por Kamat que es el sarpanch (jefe) de la aldea. Pero Kamat está envejeciendo y necesita un sucesor. ¿Puede usted, su hijo menor, asumir las responsabilidades del pueblo y hacer que el pueblo prospere.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat', 'Hijo, te voy a enseñar sobre los distintos aspectos para llevar adelante una aldea en la actualidad. ¿Estás listo para aprender? Vayamos a la aldea de Abujamara. ',
                'Son',' Padre, esto no es una aldea,es una terreno vacío .... ',
                'Kamat',' Sí, éste es el lugar donde alguna vez existió la aldea de Abujamara. La aldea se convirtió en tierra estéril cuando Ganga maldijo a los habitantes de Abujamara cambiando el curso del río, inundando Abujamara. Las personas perdieron sus hogares y nosotros les ayudaremos a reconstruir su aldea']

    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Construir una choza para albergar a las personas de Abujamara. Usted puede construir una choza, haciendo clic en Crear -> Choza.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [True,1,'HOUSE','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Cuando se construye una choza, una cierta cantidad de sus recursos son utilizados. Para cada Choza que construyes, 10 unidades de ladrillos, 10 unidades de herramientas y 3 unidades de agua se utilizan. Además, las personas están obligadas a construir una choza. Del mismo modo, cualquier cosa que construyas requerirá materiales de construcción como ladrillos y mano de obra. Intenta construir otra choza.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'HOUSE','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Cuando se construye una Choza la barra de Vivienda en la esquina inferior derecha de la pantalla aumenta. Cuanto más este completa esté esta barra mayor es el número de personas que tienen casas disponibles.  Barras de progreso altas indican un pueblo feliz y próspero.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'En la esquina inferior izquierda puedes ver la población total y el total de personas albergadas. La población total aumenta con el tiempo. La construcción de Casas aumenta la población protegida. Usted siempre debe tratar de construir suficientes casas para albergar a todo el pueblo.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    

    text = 'El agua, la necesidad más básica de la vida, siempre debe estar presente para apoyar cualquier tipo de habitación. Construir un Pozo permite a la gente obtener el agua de ahí.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FOUNTAIN','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'La siguiente necesidad básica de una aldea es la comida. Para producir alimentos, tendrá que construir granjas. Lo mejor es proporcionar una saludable mezcla de arroz, frijoles con  frutas y verduras. Esto asegurará una nutrición variada y saludable.  Puedes elegir el tipo de producción para tu granja desde la gráfica de barras. Haga clic en Crear -> Granja y ajustar la producción.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FARM','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
 
    text = 'A medida que continúes edificando, requerirás Herramientas y Ladrillos. Si te quedas sin ellos puedes comprarlos en el mercado. Para comprar cualquier cosa se necesita dinero y tu puedes ver la cantidad de dinero disponible en la esquina superior derecha de la pantalla.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
      
    text = 'El asentamiento ha crecido, los niños necesitan un lugar para estudiar. Construye una escuela para ellos.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    text = 'Bien hecho. Pero no hay libros en esta escuela. Compra los libros para la escuela en el mercado. La ventana Mercado puede ser abierta haciendo clic en el botón Mercado en la parte inferior. Una vez abierta la ventana Mercado, puede hacer click en las cosas que necesitas comprar y vender. A continuación, selecciona la cantidad que debe ser comprada o vendida.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','BOOKS','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
   

    text = 'El botón de actualización proporciona mejoras tecnológicas. Intente actualizar las chozas con ladrillos. Haga click sobre Actualización y seleccione Choza.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'HOUSE','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Las mejoras tecnológicas proveen mejores edificios con capacidad para albergar a más trabajadores y producir más recursos. Por lo tanto, suelen ser útiles para aumentar la prosperidad del pueblo. Actualice su escuela.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Debes notar que la actualización de una instalación aumenta su productividad. El número de niños a los que se enseña en la Escuela se ha incrementado considerablemente, también la calidad de la educación es ahora mejor. Las barras de progreso también han aumentado.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'Las personas están ociosas en la aldea, debes construir un taller para crear más trabajo para ellos. La construcción de un taller también agrega Herramientas para el acopio de tu aldea.'

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'WORKSHOP','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    text = 'Tu aldea ha crecido considerablemente ahora, la higiene y la sanidad son los dos aspectos más importantes de una vida saludable. Debes construir un Hospital ahora para que la gente reciba  buenos tratamientos y medicinas.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'HOSPITAL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = '¡Tendrás que comprar medicina en el mercado para que el hospital trabaje!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','MEDICINE','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
	
    text = 'Tu aldea ha dado el primer paso hacia la prosperidad. ¡Felicitaciones!'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 1
    
    chatText = ['Kamat','Buen trabajo con la creación de la nueva aldea. Estoy realmente impresionado.',
                'Son',' Gracias ',
                'Kamat','Pero yo me pregunto, si eres lo suficientemente capaz de trabajar sin mi guía, ahora que has aprendido lo básico para construir una aldea.',
                'Kamat','Yo te dejaré la responsabilidad de la aldea por los próximos 1 mese, mientras estoy fuera por la boda de tu prima hermana. ']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'No permitas que ninguna de las barras de progreso caigan por debajo de 35 ... o Kamat no estará muy contento. ¡Buena suerte!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',35]
    condn2 = [False,3,'','','>=','HEALTH',35]
    condn3 = [False,3,'','','>=','EDUCATION',35]
    condn4 = [False,3,'','','>=','NUTRITION',35]
    condn5 = [False,3,'','','>=','TRAINING',35]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    chatText = ['Kamat','Bien hecho Hijo. Parece que eres capaz de manejar el pueblo despues de mí.']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/prosper.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "No fuiste capaz de mantener la aldea correctamente. No fuiste capaz de completar la tarea que te asigne. Debes reintentar este nivel para avanzar al siguiente."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    # Mission 2
    
    chatText = ['Kamat','Bien hecho hijo, por cierto no me has decepcionado. Pero nuestra aldea está ahora a punto de agotar el dinero.',
                'Kamat','Te daré cuatro meses para traer más dinero a la aldea. Las reservas en efectivo siempre son útiles en tiempos de calamidades.',
                'Kamat','También, más reservas en efectivo nos permitirá mejorar los edificios, comprar materiales y alimentos para mejorar las condiciones de nuestro pueblo.',
                'Kamat','Como ya has aprendido, las Herramientas hechas en los talleres se pueden vender en el mercado para ganar dinero, debes dedicarte a eso.']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Gana  5000 Rs. más en los próximos 1 mese. Pero recuerda, esto no debería ser a costa de la condición de la aldea. No dejes que las barras de progreso caigan por debajo de 25. ¡Buena suerte!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',25]
    condn2 = [False,3,'','','>=','HEALTH',25]
    condn3 = [False,3,'','','>=','EDUCATION',25]
    condn4 = [False,3,'','','>=','NUTRITION',25]
    condn5 = [False,3,'','','>=','TRAINING',25]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = "No fuiste capaz de mantener el pueblo correctamente. No fuiste capaz de completar la tarea que te he asignado. Debes reintentar este nivel para alcanzar el siguiente."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,5,'','','>=','',5000]
    
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "No fuiste capaz de mantener el pueblo correctamente. No fuiste capaz de completar la tarea que te he asignado. Debes reintentar este nivel para alcanzar el siguiente."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    # Mission 3
    
    chatText = ['Kamat','Respetados miembros de Panchayat, mi hijo ha generado 5000 Rs más en las arcas de la aldea. Ahora, nos corresponde a nosotros decidir qué necesitamos hacer con ella.']
    
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Panchayat discute el asunto en la asamblea de la aldea ....'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Panch','El Panchayat ha logrado una decisión. Vamos a invertir el dinero en la construcción de más escuelas. ',
                'Kamat',' Sí, los niños son el futuro de nuestra aldea. Queremos enseñarles que sean capaces de sostenerse por si mismos y crear riqueza y prosperidad en la aldea más adelante. ',
                'Panch',' Sí, y ya que su hijo ha demostrado ser experto en administración, queremos que se haga cargo del dinero generado y usarlo para para educar a los hijos de nuestra aldea.',
                'Son','Será un placer.']
                
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Tu misión es simple. Aumenta la barra de progreso de Educación a 70, mientras que no permitas que ninguna de las otras barras de progreso caigan por debajo de 30 durante 1 mese.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condn4 = [False,3,'','','>=','NUTRITION',30]
    condn5 = [False,3,'','','>=','TRAINING',30]
    condnlist = [condn1,condn2,condn4,condn5]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = "No fuiste capaz de mantener el pueblo correctamente. No fuiste capaz de completar la tarea que te he asignado. Debes reintentar este nivel para alcanzar el siguiente."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn3 = [False,3,'','','>=','EDUCATION',70]
    
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "No fuiste capaz de mantener el pueblo correctamente. No fuiste capaz de completar la tarea que te he asignado. Debes reintentar este nivel para alcanzar el siguiente."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    # Mission 4
    
    chatText = ['Kamat','Bienvenido Ajmal, hijo mío. ¿Cómo te ha ido en tus estudios? ',
                'Ajmal','Gracias papá. Yo soy un médico titulado ... pero qué es esto. La higiene del pueblo es tan pobre. Esta aldea es un caldo de cultivo para todas las enfermedades.', 
                'Ajmal',' Con el agua estancada y el mercado sucio, las enfermedades están obligados a permanecer. Todas estas enfermedades pronto tomarán forma de epidemia si nada muy pronto', 
                'Kamat','¿Puedes trabajar con tu hermano menor para ayudar a evitar esta situación. ',
                'Ajmal','claro padre',
                'Ajmal',' Por proporcionar buena salud, tenemos que proporcionar alimentos nutritivos a los aldeanos. Una dieta nutritiva consiste en todos los componentes, tales como trigo, frutas, verduras y frijoles.',
                'Ajmal',' También necesitamos instalar hospitales y educar acerca de buenas prácticas y medidas sencillas para evitar las enfermedades. Escuelas instaladas por ti ya está haciendo un buen trabajo. Sólo tenemos que traer buenos médicos aquí ',
                'Ajmal','¿Puedes hacer todo esto para evitar una epidemia ']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Sí, esta misión es más difícil. Lleva la barra de progreso de salud a 70 y la de nutrición por sobre 65 y serás calificado a seguir.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',70]
    condn2 = [False,3,'','','>=','NUTRITION',65]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)


    
    text = "Fuiste capaz de completar la tarea asignada.¡Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

        
    # Mission 5
    
    chatText = ['Farmer', 'Sálvanos, sálvanos ....',
                'Kamat','¿Qué paso? ¿De dónde estás huyendo? ¿Dónde está tu ganado y pertenencias. ',
                'Farmer',' No tengo ninguno señor .. He huido de mi casa con mis hijos y esposa ya que hay una guerra desatada. ',
                'Farmer',' Vendrán más personas como yo. Voy a trabajar duro, pero por favor, dame un lugar para vivir en paz.']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Kamat y el Panchayat discuten ...'

    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Panch','Panchayat ha decidido que dejaremos entrar a nuestra aldea a los inmigrantes y los trataremos como nuestros huéspedes. Athiti Devo Bhav']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'Parece que no hay suficientes chozas para todos los inmigrantes. Construye más chozas y aumenta la barra de progreso de Vivienda hasta 90. También aumenta los progresos en Nutrición hasta 50.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',90]
    condn2 = [False,3,'','','>=','NUTRITION',50]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    

    
    text = "Fuiste capaz de completar la tarea asignada.¡Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # Mission 6
    
    chatText = ['Panch','Buenos días, miembros del Panchayat. Ha sido casi 4 meses desde que los primeros inmigrantes llegaron a nuestra aldea. ',
                'Panch','Pero la mayoría de ellos están sentados sin hacer nada, puesto que originalmente eran agricultores y ahora no tienen fincas. ',
                'Kamat',' Por lo tanto, los vamos a entrenar en nuestros talleres para fabricar ladrillos para nuestra aldea. También, podemos entrenarlos como obreros y se convertirán en una parte integral de la aldea.']
                 
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Buen trabajo recuperándose de la calamidad. Entrena a tu gente para que se conviertan en recursos útiles. Aumenta la barra de progreso de capacitación a 90 para aprobar esta misión.' 

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    condn1 = [False,3,'','','>=','TRAINING',90]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    
    text = "Fuiste capaz de completar la tarea asignada.\n¡Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 7
    
    chatText = ['Farmer','Sarpanch ji, no hay agua. Los cultivos se están muriendo. Ayúdenos',
                'Priest, "¿Cómo puede ayudar Sarpanch ji? Es el dios de la lluvia: Indra, que está disgustado con nosotros. Celebraremos una ceremonia para complacer a Indra. ',
                'Kamat','Haré lo que pueda.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','Hijo ...',
                'Son',' Sí padre, ¿hay algo que puedo hacer por usted.',
                'Kamat',' Sí, hijo, el monzón nos ha abandonado. Los cultivos se están muriendo. Los agricultores creen que el dios Indra que está disgustado, pero usted sabe mejor.',
                'Kamat','Se llevará a cabo una ceremonia pronto. Pero tenemos que hacer más que eso. ',
                'Son',' Sí Padre.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'No permitas que los progresos de nutrición caigan por debajo del 50% y no permitas que el nivel del agua caiga por debajo de 500 durante los próximos 1 mese.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,3,'','','>=','NUTRITION',48]
    condn2 = [False,4,'','WATER','>=','',500]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    


    chatText = ['Farmer', 'Gracias, Sarpanchji por resolver un problema tan grave. Sin su ayuda, hubiésemos muerto de hambre junto con nuestras familias.',
                'Kamat','Bueno esta vez no fui yo. Es mi hijo quien debe estar recibiendo el crédito de todo este trabajo.',
                'Son',' Gracias, padre. Pero todo fue gracias a su orientación y apoyo es que soy capaz de servir para la prosperidad de la aldea.']


    action = [1,[chatText,str(storyboard_name)+'/images/chat images/Happy.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    text = "El WFP ha planificado enseñar a los agricultores de su aldea.Se estaría ayudando a los agricultores aumentar su productividad, ayudándoles a realizar una adecuado riego de sus fincas. Ayudaría a los agricultores aplicar técnicas como la rotación de cultivos, uso de fertilizantes, etc, por que aumente la productividad de las granjas y la fertilidad del suelo se mantenga intacta."

    
    action = [6,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 

    text = "No fuiste capaz de mantener el pueblo correctamente.No fuiste capaz de completar la tarea que le ha asignado.Debes reintentar este nivel para alcanzar el siguiente."
    
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    # Mission 8
    
    chatText = ['Kamat','Hijo, estoy envejeciendo, pero tengo una mala sensación de que algo malo está a punto de suceder',
                'Son', '¿Por qué cree usted eso, padre? ',
                'Kamat',' Los signos están ahí en los animales. Mira cómo el ganado y las ovejas están cada vez más inquietos. Ellos son los que saben primero que los dioses están enojados']
    
    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = " Un terremoto golpea la aldea.\n\nKamat muere durante el terremoto.\n\nAjmal también regresa a la aldea después de recibir la noticia."
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Ajmal','Hermano, la responsabilidad de manejar la aldea depende de ti ahora. Debes ayudar a la gente de la aldea a recuperarse de esta calamidad.',
                'Son','Pero bhaiyya, yo no seré capaz de hacer todo esto sin la ayuda y apoyo del Padre. ',
                'Ajmal',' Padre tenía una visión para esta aldea. Le había llevado toda una vida levantar esta aldea. Tu debes trabajar para su misión.',
                'Ajmal','Debes reconstruir todo y reponer la aldea en el camino hacia el progreso y la prosperidad',
                'Son',' No te preocupes hermano, voy a reconstruir la aldea y su antiguo esplendor. ']
    

    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Objetivo de la Misión: reconstruir el pueblo y subir los niveles de progreso a un 65%'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    


    condn1 = [False,3,'','','>=','HOUSING',65]
    condn2 = [False,3,'','','>=','HEALTH',65]
    condn3 = [False,3,'','','>=','EDUCATION',65]
    condn4 = [False,3,'','','>=','NUTRITION',65]
    condn5 = [False,3,'','','>=','TRAINING',65]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

 
    text = "La aldea Panchayat ha decidido elegirte como el próximo Sarpanch de la aldea. También han decidido hacer una nueva escuela en recuerdo del mejor Sarpanch que ha tenido esta aldea en años, tu padre, Kamat."
    
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [10,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)


    output.close()
    
    
write_data()