#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#   Author : foodforce2@gmail.com
#   Date : 01/01/2010
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
flag = 2
list_file = open('storyboard_list.pkl')
pickle.load(list_file)
storyboard_name = None
while storyboard_name == None:
    storyboard = pickle.load(list_file)
    if flag == storyboard[0]:
        storyboard_name = storyboard[1]

def write_data():
    
    output = open(os.path.join('storyboards',storyboard_name,'storyboard_spa.pkl'),'wb')

    #Introduction data
    text = 'Hait� es un pa�s caribe�o. Junto a Rep�blica Dominicana, ocupa la isla La Espa�ola, en el archipelago mayor de las Antillas. El �rea total de Hait� es de 27.750 kil�metros cuadrados y su capital es Puerto Pr�ncipe. Fue la primera naci�n independiente de Am�rica Latina y la primera rep�blica en el mundo en ser dirigido por un ser humano de raza negra cuando tras una rebeli�n exitosa de esclavos en 1804.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Gilbert Fernandez','La ciudad de Hait� ha sido golpeado por un catastr�fico terremoto de magnitud 7.0',
                'Stevenson Gorbachev','Muchas edificaciones notables, tales como el Palacio Presidencial, la Asamblea Nacional, la catedral de Puerto Pr�ncipe, la principal c�rcel est�n completamente destruidas. Muchas figuras p�blicas tambi�n son v�ctimas de este terremoto',
                'Gilbert Fernandez','Hait� no es capaz de recuperarse por s� sola de este desastre',
                'Stevenson Gorbachev','Hemos pedido ayuda a nuestros pa�ses vecinos. Espero que seamos capaces de superar estos tiempos oscuros con su apoyo']
    
    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Hait� ha sido golpeado por un terremoto que ha destruido la mayor parte de los edificios y deterior� gravemente la situaci�n de la ciudad. Varios equipos se han enviado por diferentes pa�ses para atender la situaci�n y ayudar en todo lo que can. Tu, siendo la jefatura de la ciudad, tienen que trabajar en colaboraci�n con todos los equipos enviados para su ayuda y garantizar la restauraci�n de la paz en la ciudad.'
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    
    #Mission 1
    
   
    chatText = ['Stevenson Gorbachev','El terremoto ha destruido todo.',
                'Tony Peralta','En este momento es necesario que se relocalicen los sobrevivientes o la gente que ha quedado aislada debido all bloqueo de carreteras, y se les suministre alimentos y medicinas.',
                'Ragnar Stefansson',' Las v�as de acceso m�s importantes de la ciudad est�n bloqueadas y hemos comenzado a trabajar en ello, pero nos tomar� algunos d�as para volver a la normalidad ',
                'Stevenson Gorbachev',' Hasta entonces , debemos hacer algo para ayudar a los sobrevivientes. ',
                'Tony Peralta','La ciudad tambi�n necesita m�s hospitales, ya que s�lo hay un hospital en pleno funcionamiento en la ciudad y est� saturado. Hay cientos de heridos.']
    
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Granjas y Hospitales ayudan a aumentar la barra de progreso de nutici�n y de salud.'

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La misi�n es proporcionar alimentos y medicamentos a las instalaciones de los sobrevivientes. Aumenta las barras de progreso de la nutrici�n y la salud a 30% en un lapso de 2 semanas.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    condn1 = [False,3,'','','>=','HEALTH',0]
    condnlist = [condn1]
    condnGlobal = ['NOR',14,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'No fuiste capaz de mantener las barras por sobre ell 30%. No has podido salvar al pueblo. Debes reintentar este nivel para seguir al siguiente'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',30]
    condn2 = [False,3,'','','>=','NUTRITION',30]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Haz tenido �xito en el primer paso hacia la resurrecci�n de la ciudad'
    
    action = [7,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'No fuiste capaz de mantener las barras por sobre ell 30%.  No has podido salvar al pueblo. Debes reintentar este nivel para seguir al siguiente'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 2

    chatText = ['Tony Peralta',' Grandes cantidades de suministros de alimentos han sido recogidos en Puerto Pr�ncipe y un gran n�mero de m�dulos de atenci�n m�dica m�vil, enviados por varios pa�ses, est�n trabajando con las personas heridas',
                'Ragnar Stefansson','Cerca del 90% de los edificios en la ciudad han sido destruidos y la gente vive en condiciones de hacinamiento. Hay que hacer algo ',
                'Stevenson Gorbachev','Tenemos que empezar a construir m�s casas para la gente, pero tambi�n debemos asegurarnos de que los progresos realizados hasta la fecha se mantengan y no se malgasten.']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La misi�n es proporcionar una vivienda digna a los habitantes de la aldea. Aumenta la barra de progreso para Vivienda a 40%, manteniendo las barras de progreso para nutrici�n y salud por encima del 30%. Esta misi�n debe ser completada en un lapso de 1 mes.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','NUTRITION',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'No fuiste capaz de cumplir esta misi�n. Debes completarla para seguir al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',40]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
                
    text  = 'Haz proporcionado una vivienda digna a los habitantes de tu ciudad.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'No fuiste capaz de cumplir esta misi�n. Debes completarla para seguir al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 3
    
    
    chatText = ['Gilbert Fernandez','Es parte esencial del plan de recuperaci�n que la gente disponga de fuentes de trabajo y disponga nuevamente de sueldos.',
                'Ragnar Stefansson','La gente ha empezado a vivir en sus propios hogares y el proceso de reconstrucci�n avanza a un ritmo acelerado ',
                'Stevenson Gorbachev','Los habitantes de la ciudad necesitan ser capacitados, de modo que puedan comenzar a alimentarse. Deben ser autosuficientes ya que el suministro de alimentos no va a durar por mucho tiempo.',
                'Gilbert Fernandez',' Estamos planeando poner en marcha un programa con el fin de proporcionar empleo a la gente. ']
    
    action  = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La funci�n de los talleres es entrenar a las personas para producir herramientas para la aldea.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Esta vez tendr�s que entrenar a las personas para que puedan iniciar una vida normal otra vez. Aumenta la barra de progreso de capacitaci�n a 40% creando talleres y tambi�n asegura que las barras de nutrici�n y salud se encuentren por sobre 30% y la barra de vivienda por sobre el 40%. El plazo para esta misi�n es de 1 mes.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
   
     
    
    condn1 = [False,3,'','','>=','HEALTH',30]
    condn2 = [False,3,'','','>=','NUTRITION',30]
    condn3 = [False,3,'','','>=','HOUSING',40]
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Has perdido en este nivel. Int�ntalo de nuevo'
    
    action = [8,text]
    actionData  = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','TRAINING',40]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Se ha creado empleo para las personas y se han hecho autosuficientes. �Felicitaciones!'
    
    action = [7,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'Has perdido en este nivel. Int�ntalo de nuevo'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    #Mission 4
    
    
  
    chatText = ['Stevenson Gorbachev','Debido al terremoto el sistema educativo de la ciudad ha colapsado completamente.',
                'John Tremblay','Es esencial para el futuro que los ni�os recibir�n educaci�n y esta se imparta desde sus inicios. ',
                'Gilbert Fernandez','La ciudad tambi�n debe poseer ahorros monetarios a fin de garantizar que este tipo de calamidades se pueden manejar de manera m�s efectiva. ']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Todos los servicios b�sicos de la aldea han sido restaurados, por lo que es tu trabajo manternerlos trabajando. Aumenta la barra de progreso de educaci�n y capacitaci�n a 60% y en el pr�ximo mes ninguna de las barras debe caer por debajo del 50% y debes reunir 4000 Rs al cabo de este tiempo.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',50]
    condn2 = [False,3,'','','>=','NUTRITION',50]
    condn3 = [False,3,'','','>=','HOUSING',50] 
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'No has sido capaz de completar la tarea. Debes completarla para pasar al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',60]
    condn2 = [False,5,'','','>=','',4000]
    condn3 = [False,3,'','','>=','TRAINING',60]
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Has completado este paso de llevar la ciudad hacia plena recuperaci�n'
    
    action = [7,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'No has sido capaz de completar la tarea. Debes completarla para pasar al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 5
    
    
    chatText = ['Stevenson Gorbachev','La situaci�n de la ciudad ha mejorado considerablemente ',
                'Gilbert Fernandez',' Debido al r�pido desarrollo del sistema educativo, One Laptop Per Child (OLPC, Un Computador por Ni�o) ha decidido donar computadoras port�tiles a las escuelas .',
                'John Tremblay','Esta es una medida muy buena pues ser� de gran ayuda al crecimiento del sistema educativo. Por otra parte, este tipo de cosas ayudar mantener todos los niveles de la sociedad en equidad y por lo tanto que la sociedad se desarrolle en su conjunto.',
                'Stevenson Gorbachev','El progreso realizado a la fecha ser�a in�til si no se mantiene y el dinero obtenido se utilice para futuros desarrollos. �Tenemos suficientes alimentos y medicamentos para la gente en los pr�ximos meses?',
                'Tony Peralta','Nuestros dep�sitos est�n llenos, estamos totalmente preparados en ese frente,',
                'Ragnar Stefansson','El �rea de vivienda necesita ser atendida, vamos a necesitar muchas m�s casas para otorgarle techo a todas las personas. ']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Ahora tiene que prestar atenci�n al desarrollo de la persona village.Every en el pueblo debe tener una casa adecuada a itself.Your tarea es aumentar la barra de progreso para la vivienda del 70%, manteniendo todos los dem�s muy por encima del 30% durante los primeros 10 d�as y por encima del 50% para los pr�ximos 20 dias.El plazo es de 1 meses.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condn3 = [False,3,'','','>=','TRAINING',30]
    condn4 = [False,3,'','','>=','NUTRITION',30]
    condnlist = [condn1,condn2,condn3,condn4]
    condnGlobal = ['NOR',10,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output) 
    
    
    text = 'No has sido capaz de completar la tarea. Debes completarla para pasar al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',40]
    condn2 = [False,3,'','','>=','HEALTH',40]
    condn3 = [False,3,'','','>=','TRAINING',40]
    condn4 = [False,3,'','','>=','NUTRITION',40]
    condnlist = [condn1,condn2,condn3,condn4]
    condnGlobal = ['NOR',20,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output) 
    
    
    text = 'No has sido capaz de completar la tarea. Debes completarla para pasar al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',70]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Has completado este paso llevando la ciudad hacia la plena recuperaci�n'
    
    action = [7,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    
    text = 'No has sido capaz de completar la tarea. Debes completarla para pasar al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    

    
    chatText = ['Gilbert Fernandez','La gente ha vuelto a tener una vida feliz y pr�spera',
                'Tony Peralta','Todos nuestros esfuerzos han dado sus frutos, nuestro trabajo aqu� en esta ciudad ha terminado. ',
                'Stevenson Gorbachev','Aunque la ciudad se ha recuperado de la conmoci�n del terremoto, es mi deber como Gobernador mantener la condici�n actual de la aldea. ']
    
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Felicitaciones de haber restaurado la paz y la prosperidad de su pueblo'
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [10,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

    
    output.close()
    
write_data()
