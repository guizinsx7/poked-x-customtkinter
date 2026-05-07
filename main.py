import customtkinter as ctk
import pokebase as pb
from PIL import Image
import requests
from io import BytesIO

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

janela = ctk.CTk()
janela.geometry('300x400')
janela.title('Pokédex')
janela.iconbitmap("img/pokemon-icon.ico")

pagina1 = ctk.CTkFrame(janela)
pagina1.pack(pady=20, padx=20, fill='both', expand=True)

titulo = ctk.CTkImage(light_image=Image.open("img/pokemon.png"), dark_image=Image.open("img/pokemon.png"), size=(200, 73))
label = ctk.CTkLabel(pagina1, image=titulo, text='')
label.pack(pady=50)

pokemon = ctk.CTkEntry(pagina1, placeholder_text='Seu pokemon', width=200, height=40)
pokemon.pack(pady=10)

def Buscar():
    pokemon_pesquisado = pokemon.get().lower()
    
    try:
        poke = pb.pokemon(pokemon_pesquisado)
        
        types = {
          'fire': 'img/fire.png',
          'water': 'img/water.png',
          'grass': 'img/grass.png',
          'electric': 'img/eletric.png',
          'ice': 'img/ice.png',
          'fighting': 'img/fighting.png',
          'poison': 'img/poison.png',
          'ground': 'img/ground.png',
          'flying': 'img/flying.png',
          'psychic': 'img/psychic.png',
          'bug': 'img/bug.png',
          'rock': 'img/rock.png',
          'ghost': 'img/ghost.png',
          'dragon': 'img/dragon.png',
          'steel': 'img/steel.png',
          'dark': 'img/dark.png',
          'fairy': 'img/fairy.png',
          'normal': 'img/normal.png'
        }

        traducao_stats = {
            'hp': 'Vida',
            'attack': 'Ataque',
            'defense': 'Defesa',
            'special-attack': 'Ataque Especial',
            'special-defense': 'Defesa Especial',
            'speed': 'Velocidade'
        }

        response_front = requests.get(poke.sprites.front_default)
        img_data_front = Image.open(BytesIO(response_front.content))

        response_front_shiny = requests.get(poke.sprites.front_shiny)
        img_data_front_shiny = Image.open(BytesIO(response_front_shiny.content))

        janela.geometry('400x650')
        
        pagina1.pack_forget() 
        
        pagina2 = ctk.CTkFrame(janela)
        pagina2.pack(pady=20, padx=20, fill='both', expand=True)

        label_text_poke = ctk.CTkLabel(pagina2, text=f'{pokemon_pesquisado.upper()}: #{poke.id}', font=('Roboto', 18, 'bold'))
        label_text_poke.pack(pady=(20, 2))

        frame_pokemon = ctk.CTkFrame(pagina2, fg_color="transparent")
        frame_pokemon.pack(pady=10)
        
        sprite_pokemon_front = ctk.CTkImage(light_image=img_data_front, dark_image=img_data_front, size=(150, 150))
        label_sprite_front = ctk.CTkLabel(frame_pokemon, image=sprite_pokemon_front, text='')
        label_sprite_front.pack(pady=20, side='left')

        sprite_pokemon_front_shiny = ctk.CTkImage(light_image=img_data_front_shiny, dark_image=img_data_front_shiny, size=(150, 150))
        label_sprite_front_shiny = ctk.CTkLabel(frame_pokemon, image=sprite_pokemon_front_shiny, text='')
        label_sprite_front_shiny.pack(pady=20, side='left')

        frame_tipos = ctk.CTkFrame(pagina2, fg_color="transparent")
        frame_tipos.pack(pady=10)
        label_types = ctk.CTkLabel(frame_tipos, text='TIPOS: ')
        label_types.pack(side='left', padx=10)

        for i in poke.types:
            type_name = i.type.name
            if type_name in types:
                image_type = ctk.CTkImage(light_image=Image.open(types[type_name]), dark_image=Image.open(types[type_name]), size=(40, 40))            
                label_type = ctk.CTkLabel(frame_tipos, image=image_type, text='')
                label_type.image = image_type
                label_type.pack(side='left', padx=5)
        
        frame_stats = ctk.CTkFrame(pagina2, fg_color='transparent')
        frame_stats.pack(pady=10)

        contador = 0

        for i in poke.stats:
            status_exibido = traducao_stats.get(i.stat.name, i.stat.name)
            contador+=1

            label_stats_name = ctk.CTkLabel(frame_stats, text=f'{status_exibido.upper()}:')
            label_stats_name.grid(row=contador, column=0, sticky="w", padx=10, pady=2)

            label_stats_base = ctk.CTkLabel(frame_stats, text=i.base_stat)
            label_stats_base.grid(row=contador, column=1, sticky='w', padx=10, pady=2)

        def Voltar():
            pagina2.forget()
            janela.geometry('300x400')
            pagina1.pack(pady=20, padx=20, fill='both', expand=True)
        
        botao_voltar = ctk.CTkButton(pagina2, text="Voltar", width=80, height=30, command=Voltar)
        botao_voltar.pack(side='bottom', anchor='w', padx=10, pady=10)


    except Exception as e:
        print(f'Erro: Não foi possível encontrar ou exibir o Pokémon. Detalhe: {e}')

botao = ctk.CTkButton(pagina1, text='Procurar', command=Buscar, width=200, height=40)
botao.pack(pady=20)



janela.mainloop()