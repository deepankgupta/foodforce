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
    
    text = '\n \n \n \nEn este hermoso pa�s llamado Chile, hay un pueblo Gokul. El pueblo de Gokul se rige por Kamat que es el sarpanch (jefe) de la aldea. Pero Kamat est� envejeciendo y necesita un sucesor. �Puede usted, su hijo menor, asumir las responsabilidades del pueblo y hacer que el pueblo prospere.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat', 'Hijo, te voy a ense�ar sobre los distintos aspectos para llevar adelante una aldea en la actualidad. �Est�s listo para aprender? Vayamos a la aldea de Abujamara. ',
                'Son',' Padre, esto no es una aldea,es una terreno vac�o .... ',
                'Kamat',' S�, �ste es el lugar donde alguna vez existi� la aldea de Abujamara. La aldea se convirti� en tierra est�ril cuando Ganga maldijo a los habitantes de Abujamara cambiando el curso del r�o, inundando Abujamara. Las personas perdieron sus hogares y nosotros les ayudaremos a reconstruir su aldea']

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
    
    text = 'Cuando se construye una choza, una cierta cantidad de sus recursos son utilizados. Para cada Choza que construyes, 10 unidades de ladrillos, 10 unidades de herramientas y 3 unidades de agua se utilizan. Adem�s, las personas est�n obligadas a construir una choza. Del mismo modo, cualquier cosa que construyas requerir� materiales de construcci�n como ladrillos y mano de obra. Intenta construir otra choza.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'HOUSE','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Cuando se construye una Choza la barra de Vivienda en la esquina inferior derecha de la pantalla aumenta. Cuanto m�s este completa est� esta barra mayor es el n�mero de personas que tienen casas disponibles.  Barras de progreso altas indican un pueblo feliz y pr�spero.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'En la esquina inferior izquierda puedes ver la poblaci�n total y el total de personas albergadas. La poblaci�n total aumenta con el tiempo. La construcci�n de Casas aumenta la poblaci�n protegida. Usted siempre debe tratar de construir suficientes casas para albergar a todo el pueblo.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    

    text = 'El agua, la necesidad m�s b�sica de la vida, siempre debe estar presente para apoyar cualquier tipo de habitaci�n. Construir un Pozo permite a la gente obtener el agua de ah�.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FOUNTAIN','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'La siguiente necesidad b�sica de una aldea es la comida. Para producir alimentos, tendr� que construir granjas. Lo mejor es proporcionar una saludable mezcla de arroz, frijoles con  frutas y verduras. Esto asegurar� una nutrici�n variada y saludable.  Puedes elegir el tipo de producci�n para tu granja desde la gr�fica de barras. Haga clic en Crear -> Granja y ajustar la producci�n.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FARM','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
 
    text = 'A medida que contin�es edificando, requerir�s Herramientas y Ladrillos. Si te quedas sin ellos puedes comprarlos en el mercado. Para comprar cualquier cosa se necesita dinero y tu puedes ver la cantidad de dinero disponible en la esquina superior derecha de la pantalla.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
      
    text = 'El asentamiento ha crecido, los ni�os necesitan un lugar para estudiar. Construye una escuela para ellos.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    text = 'Bien hecho. Pero no hay libros en esta escuela. Compra los libros para la escuela en el mercado. La ventana Mercado puede ser abierta haciendo clic en el bot�n Mercado en la parte inferior. Una vez abierta la ventana Mercado, puede hacer click en las cosas que necesitas comprar y vender. A continuaci�n, selecciona la cantidad que debe ser comprada o vendida.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','BOOKS','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
   

    text = 'El bot�n de actualizaci�n proporciona mejoras tecnol�gicas. Intente actualizar las chozas con ladrillos. Haga click sobre Actualizaci�n y seleccione Choza.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'HOUSE','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Las mejoras tecnol�gicas proveen mejores edificios con capacidad para albergar a m�s trabajadores y producir m�s recursos. Por lo tanto, suelen ser �tiles para aumentar la prosperidad del pueblo. Actualice su escuela.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Debes notar que la actualizaci�n de una instalaci�n aumenta su productividad. El n�mero de ni�os a los que se ense�a en la Escuela se ha incrementado considerablemente, tambi�n la calidad de la educaci�n es ahora mejor. Las barras de progreso tambi�n han aumentado.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'Las personas est�n ociosas en la aldea, debes construir un taller para crear m�s trabajo para ellos. La construcci�n de un taller tambi�n agrega Herramientas para el acopio de tu aldea.'

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'WORKSHOP','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    text = 'Tu aldea ha crecido considerablemente ahora, la higiene y la sanidad son los dos aspectos m�s importantes de una vida saludable. Debes construir un Hospital ahora para que la gente reciba  buenos tratamientos y medicinas.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'HOSPITAL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = '�Tendr�s que comprar medicina en el mercado para que el hospital trabaje!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','MEDICINE','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
	
    text = 'Tu aldea ha dado el primer paso hacia la prosperidad. �Felicitaciones!'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 1
    
    chatText = ['Kamat','Buen trabajo con la creaci�n de la nueva aldea. Estoy realmente impresionado.',
                'Son',' Gracias ',
                'Kamat','Pero yo me pregunto, si eres lo suficientemente capaz de trabajar sin mi gu�a, ahora que has aprendido lo b�sico para construir una aldea.',
                'Kamat','Yo te dejar� la responsabilidad de la aldea por los pr�ximos 1 mese, mientras estoy fuera por la boda de tu prima hermana. ']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'No permitas que ninguna de las barras de progreso caigan por debajo de 35 ... o Kamat no estar� muy contento. �Buena suerte!'
    
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
    
    
    chatText = ['Kamat','Bien hecho Hijo. Parece que eres capaz de manejar el pueblo despues de m�.']
    
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
    
    chatText = ['Kamat','Bien hecho hijo, por cierto no me has decepcionado. Pero nuestra aldea est� ahora a punto de agotar el dinero.',
                'Kamat','Te dar� cuatro meses para traer m�s dinero a la aldea. Las reservas en efectivo siempre son �tiles en tiempos de calamidades.',
                'Kamat','Tambi�n, m�s reservas en efectivo nos permitir� mejorar los edificios, comprar materiales y alimentos para mejorar las condiciones de nuestro pueblo.',
                'Kamat','Como ya has aprendido, las Herramientas hechas en los talleres se pueden vender en el mercado para ganar dinero, debes dedicarte a eso.']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Gana  5000 Rs. m�s en los pr�ximos 1 mese. Pero recuerda, esto no deber�a ser a costa de la condici�n de la aldea. No dejes que las barras de progreso caigan por debajo de 25. �Buena suerte!'
    
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
    
    chatText = ['Kamat','Respetados miembros de Panchayat, mi hijo ha generado 5000 Rs m�s en las arcas de la aldea. Ahora, nos corresponde a nosotros decidir qu� necesitamos hacer con ella.']
    
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Panchayat discute el asunto en la asamblea de la aldea ....'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Panch','El Panchayat ha logrado una decisi�n. Vamos a invertir el dinero en la construcci�n de m�s escuelas. ',
                'Kamat',' S�, los ni�os son el futuro de nuestra aldea. Queremos ense�arles que sean capaces de sostenerse por si mismos y crear riqueza y prosperidad en la aldea m�s adelante. ',
                'Panch',' S�, y ya que su hijo ha demostrado ser experto en administraci�n, queremos que se haga cargo del dinero generado y usarlo para para educar a los hijos de nuestra aldea.',
                'Son','Ser� un placer.']
                
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Tu misi�n es simple. Aumenta la barra de progreso de Educaci�n a 70, mientras que no permitas que ninguna de las otras barras de progreso caigan por debajo de 30 durante 1 mese.'
    
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
    
    chatText = ['Kamat','Bienvenido Ajmal, hijo m�o. �C�mo te ha ido en tus estudios? ',
                'Ajmal','Gracias pap�. Yo soy un m�dico titulado ... pero qu� es esto. La higiene del pueblo es tan pobre. Esta aldea es un caldo de cultivo para todas las enfermedades.', 
                'Ajmal',' Con el agua estancada y el mercado sucio, las enfermedades est�n obligados a permanecer. Todas estas enfermedades pronto tomar�n forma de epidemia si nada muy pronto', 
                'Kamat','�Puedes trabajar con tu hermano menor para ayudar a evitar esta situaci�n. ',
                'Ajmal','claro padre',
                'Ajmal',' Por proporcionar buena salud, tenemos que proporcionar alimentos nutritivos a los aldeanos. Una dieta nutritiva consiste en todos los componentes, tales como trigo, frutas, verduras y frijoles.',
                'Ajmal',' Tambi�n necesitamos instalar hospitales y educar acerca de buenas pr�cticas y medidas sencillas para evitar las enfermedades. Escuelas instaladas por ti ya est� haciendo un buen trabajo. S�lo tenemos que traer buenos m�dicos aqu� ',
                'Ajmal','�Puedes hacer todo esto para evitar una epidemia ']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'S�, esta misi�n es m�s dif�cil. Lleva la barra de progreso de salud a 70 y la de nutrici�n por sobre 65 y ser�s calificado a seguir.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',70]
    condn2 = [False,3,'','','>=','NUTRITION',65]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)


    
    text = "Fuiste capaz de completar la tarea asignada.�Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

        
    # Mission 5
    
    chatText = ['Farmer', 'S�lvanos, s�lvanos ....',
                'Kamat','�Qu� paso? �De d�nde est�s huyendo? �D�nde est� tu ganado y pertenencias. ',
                'Farmer',' No tengo ninguno se�or .. He huido de mi casa con mis hijos y esposa ya que hay una guerra desatada. ',
                'Farmer',' Vendr�n m�s personas como yo. Voy a trabajar duro, pero por favor, dame un lugar para vivir en paz.']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Kamat y el Panchayat discuten ...'

    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Panch','Panchayat ha decidido que dejaremos entrar a nuestra aldea a los inmigrantes y los trataremos como nuestros hu�spedes. Athiti Devo Bhav']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'Parece que no hay suficientes chozas para todos los inmigrantes. Construye m�s chozas y aumenta la barra de progreso de Vivienda hasta 90. Tambi�n aumenta los progresos en Nutrici�n hasta 50.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',90]
    condn2 = [False,3,'','','>=','NUTRITION',50]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    

    
    text = "Fuiste capaz de completar la tarea asignada.�Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # Mission 6
    
    chatText = ['Panch','Buenos d�as, miembros del Panchayat. Ha sido casi 4 meses desde que los primeros inmigrantes llegaron a nuestra aldea. ',
                'Panch','Pero la mayor�a de ellos est�n sentados sin hacer nada, puesto que originalmente eran agricultores y ahora no tienen fincas. ',
                'Kamat',' Por lo tanto, los vamos a entrenar en nuestros talleres para fabricar ladrillos para nuestra aldea. Tambi�n, podemos entrenarlos como obreros y se convertir�n en una parte integral de la aldea.']
                 
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Buen trabajo recuper�ndose de la calamidad. Entrena a tu gente para que se conviertan en recursos �tiles. Aumenta la barra de progreso de capacitaci�n a 90 para aprobar esta misi�n.' 

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    condn1 = [False,3,'','','>=','TRAINING',90]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    
    text = "Fuiste capaz de completar la tarea asignada.\n�Muy bien!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 7
    
    chatText = ['Farmer','Sarpanch ji, no hay agua. Los cultivos se est�n muriendo. Ay�denos',
                'Priest, "�C�mo puede ayudar Sarpanch ji? Es el dios de la lluvia: Indra, que est� disgustado con nosotros. Celebraremos una ceremonia para complacer a Indra. ',
                'Kamat','Har� lo que pueda.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','Hijo ...',
                'Son',' S� padre, �hay algo que puedo hacer por usted.',
                'Kamat',' S�, hijo, el monz�n nos ha abandonado. Los cultivos se est�n muriendo. Los agricultores creen que el dios Indra que est� disgustado, pero usted sabe mejor.',
                'Kamat','Se llevar� a cabo una ceremonia pronto. Pero tenemos que hacer m�s que eso. ',
                'Son',' S� Padre.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'No permitas que los progresos de nutrici�n caigan por debajo del 50% y no permitas que el nivel del agua caiga por debajo de 500 durante los pr�ximos 1 mese.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,3,'','','>=','NUTRITION',48]
    condn2 = [False,4,'','WATER','>=','',500]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    


    chatText = ['Farmer', 'Gracias, Sarpanchji por resolver un problema tan grave. Sin su ayuda, hubi�semos muerto de hambre junto con nuestras familias.',
                'Kamat','Bueno esta vez no fui yo. Es mi hijo quien debe estar recibiendo el cr�dito de todo este trabajo.',
                'Son',' Gracias, padre. Pero todo fue gracias a su orientaci�n y apoyo es que soy capaz de servir para la prosperidad de la aldea.']


    action = [1,[chatText,str(storyboard_name)+'/images/chat images/Happy.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    text = "El WFP ha planificado ense�ar a los agricultores de su aldea.Se estar�a ayudando a los agricultores aumentar su productividad, ayud�ndoles a realizar una adecuado riego de sus fincas. Ayudar�a a los agricultores aplicar t�cnicas como la rotaci�n de cultivos, uso de fertilizantes, etc, por que aumente la productividad de las granjas y la fertilidad del suelo se mantenga intacta."

    
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
    
    chatText = ['Kamat','Hijo, estoy envejeciendo, pero tengo una mala sensaci�n de que algo malo est� a punto de suceder',
                'Son', '�Por qu� cree usted eso, padre? ',
                'Kamat',' Los signos est�n ah� en los animales. Mira c�mo el ganado y las ovejas est�n cada vez m�s inquietos. Ellos son los que saben primero que los dioses est�n enojados']
    
    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = " Un terremoto golpea la aldea.\n\nKamat muere durante el terremoto.\n\nAjmal tambi�n regresa a la aldea despu�s de recibir la noticia."
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Ajmal','Hermano, la responsabilidad de manejar la aldea depende de ti ahora. Debes ayudar a la gente de la aldea a recuperarse de esta calamidad.',
                'Son','Pero bhaiyya, yo no ser� capaz de hacer todo esto sin la ayuda y apoyo del Padre. ',
                'Ajmal',' Padre ten�a una visi�n para esta aldea. Le hab�a llevado toda una vida levantar esta aldea. Tu debes trabajar para su misi�n.',
                'Ajmal','Debes reconstruir todo y reponer la aldea en el camino hacia el progreso y la prosperidad',
                'Son',' No te preocupes hermano, voy a reconstruir la aldea y su antiguo esplendor. ']
    

    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Objetivo de la Misi�n: reconstruir el pueblo y subir los niveles de progreso a un 65%'
    
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

 
    text = "La aldea Panchayat ha decidido elegirte como el pr�ximo Sarpanch de la aldea. Tambi�n han decidido hacer una nueva escuela en recuerdo del mejor Sarpanch que ha tenido esta aldea en a�os, tu padre, Kamat."
    
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [10,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)


    output.close()
    
    
write_data()