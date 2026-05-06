import customtkinter as ctk
import pokebase as pb
from PIL import Image
import requests
from io import BytesIO

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

janela = ctk.CTk()
janela.geometry('500x600')
janela.title('Pokédex')

pagina1 = ctk.CTkFrame(janela)
pagina1.pack(pady=20, padx=20, fill='both', expand=True)

titulo = ctk.CTkImage(light_image=Image.open("pokemon.png"), dark_image=Image.open("pokemon.png"), size=(200, 73))
label = ctk.CTkLabel(pagina1, image=titulo, text='')
label.pack(pady=50)

pokemon = ctk.CTkEntry(pagina1, placeholder_text='Seu pokemon', width=200, height=40)
pokemon.pack(pady=10)

def Buscar():
    pokemon_pesquisado = pokemon.get().lower()
    
    try:
        poke = pb.pokemon(pokemon_pesquisado)
        
        types = {
          'fire': 'https://static.wikia.nocookie.net/pokemon/images/4/47/Type_Fire_HOME.png/revision/latest/scale-to-width-down/1200?cb=20220611140500',
          'water': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dfgdd9x-0234a28e-54f5-4dab-b37f-226db1370c31.png/v1/fill/w_894,h_894/water_type_symbol_tcg_by_jormxdos_dfgdd9x-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9lOGRkYzRkYS0yM2RkLTQ1MDItYjY1Yi0zNzhjOWNmZTVlZmEvZGZnZGQ5eC0wMjM0YTI4ZS01NGY1LTRkYWItYjM3Zi0yMjZkYjEzNzBjMzEucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.6K1hwFXJ_eLeYw9VfjTgJ7TeP7dL0rWCrV4X0Frw3oM',
          'grass': 'https://gmatheus-spinardi.e.usp.br/pokemonbasics/images/grass.png',
          'electric': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pok%C3%A9mon_Electric_Type_Icon.svg/960px-Pok%C3%A9mon_Electric_Type_Icon.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail',
          'ice': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pok%C3%A9mon_Ice_Type_Icon.svg/960px-Pok%C3%A9mon_Ice_Type_Icon.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail',
          'fighting': 'https://www.vhv.rs/dpng/d/151-1512967_fighting-type-pokemon-symbol-hd-png-download.png',
          'poison': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Pok%C3%A9mon_Poison_Type_Icon.svg/1280px-Pok%C3%A9mon_Poison_Type_Icon.svg.png',
          'ground': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pok%C3%A9mon_Ground_Type_Icon.svg/3840px-Pok%C3%A9mon_Ground_Type_Icon.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail',
          'flying': 'https://preview.redd.it/favorite-character-that-would-be-a-flying-type-if-they-v0-wlepq0dvzmtf1.png?width=894&format=png&auto=webp&s=85d2cd4167e4525012ef47b70ab5eda557bdc6d2',
          'psychic': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Pok%C3%A9mon_Psychic_Type_Icon.svg/960px-Pok%C3%A9mon_Psychic_Type_Icon.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail',
          'bug': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dffvl73-294f6e5b-aad2-484f-bde8-1ecf082f1dfe.png/v1/fill/w_894,h_894/bug_type_symbol_galar_by_jormxdos_dffvl73-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9lOGRkYzRkYS0yM2RkLTQ1MDItYjY1Yi0zNzhjOWNmZTVlZmEvZGZmdmw3My0yOTRmNmU1Yi1hYWQyLTQ4NGYtYmRlOC0xZWNmMDgyZjFkZmUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.ktuIJujg1NSyTANoB_As6zOMmKbhSQAKNVMLHMYdNLM',
          'rock': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Pok%C3%A9mon_Rock_Type_Icon.svg/1280px-Pok%C3%A9mon_Rock_Type_Icon.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail',
          'ghost': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dffvl2d-818164a9-f8e6-41fc-ba4e-c725e2be0d66.png/v1/fill/w_1280,h_1280/ghost_type_symbol_galar_by_jormxdos_dffvl2d-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9lOGRkYzRkYS0yM2RkLTQ1MDItYjY1Yi0zNzhjOWNmZTVlZmEvZGZmdmwyZC04MTgxNjRhOS1mOGU2LTQxZmMtYmE0ZS1jNzI1ZTJiZTBkNjYucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.dT01kef_VCcZu_ikUmnJ9tNW-21BDKNgum2oA0Ouv5Q',
          'dragon': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dffvl4n-1942f6ac-3f08-4dbb-a761-a722f791bc37.png/v1/fill/w_894,h_894/dragon_type_symbol_galar_by_jormxdos_dffvl4n-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9lOGRkYzRkYS0yM2RkLTQ1MDItYjY1Yi0zNzhjOWNmZTVlZmEvZGZmdmw0bi0xOTQyZjZhYy0zZjA4LTRkYmItYTc2MS1hNzIyZjc5MWJjMzcucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.HA151bNqjmamdXiS_V8Bj7VPGpszz_4glZE-M30Q9Xk',
          'steel': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Pok%C3%A9mon_Steel_Type_Icon.svg/1280px-Pok%C3%A9mon_Steel_Type_Icon.svg.png',
          'dark': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dfgddck-cbc6956c-094a-4d20-b72e-f025c89bcdc1.png/v1/fill/w_1280,h_1280/darkness_type_symbol_tcg_by_jormxdos_dfgddck-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9lOGRkYzRkYS0yM2RkLTQ1MDItYjY1Yi0zNzhjOWNmZTVlZmEvZGZnZGRjay1jYmM2OTU2Yy0wOTRhLTRkMjAtYjcyZS1mMDI1Yzg5YmNkYzEucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.IOTd-cPB3DRBSsPc2KMQMi49Z1Z7PT4g03RNfqHAS4E',
          'fairy': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Pok%C3%A9mon_Fairy_Type_Icon.svg/1280px-Pok%C3%A9mon_Fairy_Type_Icon.svg.png',
          'normal': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Pok%C3%A9mon_Normal_Type_Icon.svg/960px-Pok%C3%A9mon_Normal_Type_Icon.svg.png?_=20230404224439'
        }

        response_front = requests.get(poke.sprites.front_default)
        img_data_front = Image.open(BytesIO(response_front.content))

        response_front_shiny = requests.get(poke.sprites.front_shiny)
        img_data_front_shiny = Image.open(BytesIO(response_front_shiny.content))
        
        pagina1.pack_forget() 
        
        pagina2 = ctk.CTkFrame(janela)
        pagina2.pack(pady=20, padx=20, fill='both', expand=True)
        
        sprite_pokemon_front = ctk.CTkImage(light_image=img_data_front, dark_image=img_data_front, size=(150, 150))
        label_sprite_front = ctk.CTkLabel(pagina2, image=sprite_pokemon_front, text='')
        label_sprite_front.pack(pady=20)

        sprite_pokemon_front_shiny = ctk.CTkImage(light_image=img_data_front_shiny, dark_image=img_data_front_shiny, size=(150, 150))
        label_sprite_front_shiny = ctk.CTkLabel(pagina2, image=sprite_pokemon_front_shiny, text='')
        label_sprite_front_shiny.pack(pady=20)

        frame_horizontal_tipos = ctk.CTkFrame(pagina2, fg_color="transparent")
        frame_horizontal_tipos.pack(pady=20)

        label_types = ctk.CTkLabel(frame_horizontal_tipos, text='TIPOS: ')
        label_types.pack(side='left', padx=10)

        for i in poke.types:
            type_name = i.type.name
            if type_name in types:
                response_type = requests.get(types[type_name])
                img_data_type = Image.open(BytesIO(response_type.content))

                image_type = ctk.CTkImage(light_image=img_data_type, dark_image=img_data_type, size=(40, 40))
                
                label_type = ctk.CTkLabel(frame_horizontal_tipos, image=image_type, text='')
                label_type.image = image_type
                label_type.pack(side='left', padx=5)
    except Exception as e:
        print(f'Erro: Não foi possível encontrar ou exibir o Pokémon. Detalhe: {e}')

botao = ctk.CTkButton(pagina1, text='Procurar', command=Buscar, width=200, height=40)
botao.pack(pady=20)



janela.mainloop()