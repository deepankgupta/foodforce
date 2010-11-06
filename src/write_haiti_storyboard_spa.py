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
    text = 'Haití es un país caribeño. Junto a República Dominicana, ocupa la isla La Española, en el archipelago mayor de las Antillas. El área total de Haití es de 27.750 kilómetros cuadrados y su capital es Puerto Príncipe. Fue la primera nación independiente de América Latina y la primera república en el mundo en ser dirigido por un ser humano de raza negra cuando tras una rebelión exitosa de esclavos en 1804.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Gilbert Fernandez','La ciudad de Haití ha sido golpeado por un catastrófico terremoto de magnitud 7.0',
                'Stevenson Gorbachev','Muchas edificaciones notables, tales como el Palacio Presidencial, la Asamblea Nacional, la catedral de Puerto Príncipe, la principal cárcel están completamente destruidas. Muchas figuras públicas también son víctimas de este terremoto',
                'Gilbert Fernandez','Haití no es capaz de recuperarse por sí sola de este desastre',
                'Stevenson Gorbachev','Hemos pedido ayuda a nuestros países vecinos. Espero que seamos capaces de superar estos tiempos oscuros con su apoyo']
    
    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Haití ha sido golpeado por un terremoto que ha destruido la mayor parte de los edificios y deterioró gravemente la situación de la ciudad. Varios equipos se han enviado por diferentes países para atender la situación y ayudar en todo lo que can. Tu, siendo la jefatura de la ciudad, tienen que trabajar en colaboración con todos los equipos enviados para su ayuda y garantizar la restauración de la paz en la ciudad.'
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    
    #Mission 1
    
   
    chatText = ['Stevenson Gorbachev','El terremoto ha destruido todo.',
                'Tony Peralta','En este momento es necesario que se relocalicen los sobrevivientes o la gente que ha quedado aislada debido all bloqueo de carreteras, y se les suministre alimentos y medicinas.',
                'Ragnar Stefansson',' Las vías de acceso más importantes de la ciudad están bloqueadas y hemos comenzado a trabajar en ello, pero nos tomará algunos días para volver a la normalidad ',
                'Stevenson Gorbachev',' Hasta entonces , debemos hacer algo para ayudar a los sobrevivientes. ',
                'Tony Peralta','La ciudad también necesita más hospitales, ya que sólo hay un hospital en pleno funcionamiento en la ciudad y está saturado. Hay cientos de heridos.']
    
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Granjas y Hospitales ayudan a aumentar la barra de progreso de nutición y de salud.'

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La misión es proporcionar alimentos y medicamentos a las instalaciones de los sobrevivientes. Aumenta las barras de progreso de la nutrición y la salud a 30% en un lapso de 2 semanas.'
    
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
    
    text = 'Haz tenido éxito en el primer paso hacia la resurrección de la ciudad'
    
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

    chatText = ['Tony Peralta',' Grandes cantidades de suministros de alimentos han sido recogidos en Puerto Príncipe y un gran número de módulos de atención médica móvil, enviados por varios países, están trabajando con las personas heridas',
                'Ragnar Stefansson','Cerca del 90% de los edificios en la ciudad han sido destruidos y la gente vive en condiciones de hacinamiento. Hay que hacer algo ',
                'Stevenson Gorbachev','Tenemos que empezar a construir más casas para la gente, pero también debemos asegurarnos de que los progresos realizados hasta la fecha se mantengan y no se malgasten.']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La misión es proporcionar una vivienda digna a los habitantes de la aldea. Aumenta la barra de progreso para Vivienda a 40%, manteniendo las barras de progreso para nutrición y salud por encima del 30%. Esta misión debe ser completada en un lapso de 1 mes.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','NUTRITION',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'No fuiste capaz de cumplir esta misión. Debes completarla para seguir al siguiente nivel'
    
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
    
    text = 'No fuiste capaz de cumplir esta misión. Debes completarla para seguir al siguiente nivel'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 3
    
    
    chatText = ['Gilbert Fernandez','Es parte esencial del plan de recuperación que la gente disponga de fuentes de trabajo y disponga nuevamente de sueldos.',
                'Ragnar Stefansson','La gente ha empezado a vivir en sus propios hogares y el proceso de reconstrucción avanza a un ritmo acelerado ',
                'Stevenson Gorbachev','Los habitantes de la ciudad necesitan ser capacitados, de modo que puedan comenzar a alimentarse. Deben ser autosuficientes ya que el suministro de alimentos no va a durar por mucho tiempo.',
                'Gilbert Fernandez',' Estamos planeando poner en marcha un programa con el fin de proporcionar empleo a la gente. ']
    
    action  = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'La función de los talleres es entrenar a las personas para producir herramientas para la aldea.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Esta vez tendrás que entrenar a las personas para que puedan iniciar una vida normal otra vez. Aumenta la barra de progreso de capacitación a 40% creando talleres y también asegura que las barras de nutrición y salud se encuentren por sobre 30% y la barra de vivienda por sobre el 40%. El plazo para esta misión es de 1 mes.'
    
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
    
    text = 'Has perdido en este nivel. Inténtalo de nuevo'
    
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
    
    text = 'Se ha creado empleo para las personas y se han hecho autosuficientes. ¡Felicitaciones!'
    
    action = [7,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'Has perdido en este nivel. Inténtalo de nuevo'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    #Mission 4
    
    
  
    chatText = ['Stevenson Gorbachev','Debido al terremoto el sistema educativo de la ciudad ha colapsado completamente.',
                'John Tremblay','Es esencial para el futuro que los niños recibirán educación y esta se imparta desde sus inicios. ',
                'Gilbert Fernandez','La ciudad también debe poseer ahorros monetarios a fin de garantizar que este tipo de calamidades se pueden manejar de manera más efectiva. ']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Todos los servicios básicos de la aldea han sido restaurados, por lo que es tu trabajo manternerlos trabajando. Aumenta la barra de progreso de educación y capacitación a 60% y en el próximo mes ninguna de las barras debe caer por debajo del 50% y debes reunir 4000 Rs al cabo de este tiempo.'
    
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
    
    text = 'Has completado este paso de llevar la ciudad hacia plena recuperación'
    
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
    
    
    chatText = ['Stevenson Gorbachev','La situación de la ciudad ha mejorado considerablemente ',
                'Gilbert Fernandez',' Debido al rápido desarrollo del sistema educativo, One Laptop Per Child (OLPC, Un Computador por Niño) ha decidido donar computadoras portátiles a las escuelas .',
                'John Tremblay','Esta es una medida muy buena pues será de gran ayuda al crecimiento del sistema educativo. Por otra parte, este tipo de cosas ayudar mantener todos los niveles de la sociedad en equidad y por lo tanto que la sociedad se desarrolle en su conjunto.',
                'Stevenson Gorbachev','El progreso realizado a la fecha sería inútil si no se mantiene y el dinero obtenido se utilice para futuros desarrollos. ¿Tenemos suficientes alimentos y medicamentos para la gente en los próximos meses?',
                'Tony Peralta','Nuestros depósitos están llenos, estamos totalmente preparados en ese frente,',
                'Ragnar Stefansson','El área de vivienda necesita ser atendida, vamos a necesitar muchas más casas para otorgarle techo a todas las personas. ']
    
    action = [1,[chatText,'haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Ahora tiene que prestar atención al desarrollo de la persona village.Every en el pueblo debe tener una casa adecuada a itself.Your tarea es aumentar la barra de progreso para la vivienda del 70%, manteniendo todos los demás muy por encima del 30% durante los primeros 10 días y por encima del 50% para los próximos 20 dias.El plazo es de 1 meses.'
    
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
    
    text = 'Has completado este paso llevando la ciudad hacia la plena recuperación'
    
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
    
    

    
    chatText = ['Gilbert Fernandez','La gente ha vuelto a tener una vida feliz y próspera',
                'Tony Peralta','Todos nuestros esfuerzos han dado sus frutos, nuestro trabajo aquí en esta ciudad ha terminado. ',
                'Stevenson Gorbachev','Aunque la ciudad se ha recuperado de la conmoción del terremoto, es mi deber como Gobernador mantener la condición actual de la aldea. ']
    
    
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
