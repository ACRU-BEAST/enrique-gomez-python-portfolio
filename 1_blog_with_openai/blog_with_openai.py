# Blog with OpenAI 🤖

# Time and generation limit
# Choose language ENG/ESP
# Hidden Keys
# Multiple generations by running the program once

import openai
from dotenv import dotenv_values
import time

'''
*VARIABLES*
'''

config = dotenv_values('keys.env.secret')
openai.api_key = config['API_KEY']

keep_writing = True
counter = 0

'''
*DEFINITIONS*
'''

def generate_blog(prompt_language, paragraph_topic):
  response = openai.Completion.create( 
    model = 'text-davinci-003', 
    prompt = prompt_language + paragraph_topic, 
    max_tokens = 400,  
    temperature = 0.3 
  ) 
  retrieve_blog = response.choices[0].text 
  return retrieve_blog 

def loop_eng(keep_writing, counter):
  while keep_writing == True and counter < 3:
    answer = input('Do you want help with your blog outline? Y for yes, anything else for no. ')
    print()
    if (answer == 'Y' or answer == 'y'):
      paragraph_topic = input('What is the topic of this blog? ')
      print('generating response...')
      print()
      time.sleep(3)
      print(generate_blog(prompt_language, paragraph_topic))
      print()
      counter += 1
      print(f'you have used {counter} out of your 3 available generations')
      print()
    else: 
      keep_writing = False 
      print('see you soon!')
  return counter

def loop_esp(keep_writing, counter):
  while keep_writing == True and counter < 3:
    answer = input('Quieres ayuda con la estructura de tu blog? S para sí, cualquier otra para no. ')
    print()
    if (answer == 'S' or answer == 's'):
      paragraph_topic = input('¿Qué tema desarrollará este blog? ')
      print('generando respuesta...')
      print()
      time.sleep(3)
      print(generate_blog(prompt_language, paragraph_topic))
      print()
      counter += 1
      print(f'has usado {counter} de 3 generaciones disponibles')
      print()
    else: 
      keep_writing = False
      print('¡nos vemos pronto!')
  return counter


'''
*CODE LOGIC*
'''

password = input('Password: ')

while password != config['BLOG_KEY']:
  password = input('Incorrect password, try again: ')

if password == config['BLOG_KEY']:
  language = input('Langguage? ESP/ENG: ')
  if language == 'ESP' or language == 'esp':
    prompt_language = 'Escribe un pequeño esquema para blog sobre el siguiente tema: '
    print('Escogiste ESPAÑOL')
    print()
    loop_esp(keep_writing, counter)
  else:
    prompt_language = 'Write a small blog outline about the following topic: '
    print('You chose ENGLISH')
    print()
    loop_eng(keep_writing, counter)