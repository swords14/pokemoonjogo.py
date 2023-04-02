import random

class Pokemon:
    def __init__(self, nome, tipo, hp, ataque, defesa):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, pokemon):
        dano = self.ataque - pokemon.defesa
        pokemon.hp -= dano
        print(f"{self.nome} atacou {pokemon.nome} e causou {dano} de dano.")
        
        if pokemon.hp <= 0:
            print(f"{pokemon.nome} foi derrotado!")

class Fogo(Pokemon):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, "Fogo", hp, ataque, defesa)

class Agua(Pokemon):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, "Água", hp, ataque, defesa)

class Eletrico(Pokemon):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, "Elétrico", hp, ataque, defesa)

class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.pokemons = []

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome} capturou {pokemon.nome}!")

    def listar_pokemons(self):
        print(f"Pokemons de {self.nome}:")
        for pokemon in self.pokemons:
            print(pokemon.nome)

class Jogador(Treinador):
    def escolher_pokemon(self):
        print(f"{self.nome}, escolha seu pokemon para a batalha:")
        self.listar_pokemons()
        escolha = input()
        pokemon_escolhido = None

        for pokemon in self.pokemons:
            if pokemon.nome == escolha:
                pokemon_escolhido = pokemon
                break

        if not pokemon_escolhido:
            print("Pokemon não encontrado. Escolha novamente.")
            return self.escolher_pokemon()

        print(f"{self.nome} escolheu {pokemon_escolhido.nome}!")
        return pokemon_escolhido

class Inimigo(Treinador):
    def escolher_pokemon(self):
        pokemon_escolhido = random.choice(self.pokemons)
        print(f"{self.nome} escolheu {pokemon_escolhido.nome}!")
        return pokemon_escolhido

class Jogo:
    def __init__(self):
        self.jogador = Jogador("Ash")
        self.inimigo = Inimigo("Gary")
        self.biblioteca_pokemons = [Fogo("Charmander", 50, 20, 10),
                                    Fogo("Vulpix", 40, 18, 8),
                                    Agua("Squirtle", 60, 15, 15),
                                    Agua("Magikarp", 30, 5, 5),
                                    Eletrico("Pikachu", 45, 25, 5),
                                    Eletrico("Jolteon", 55, 30, 10)]

        def iniciar(self):
           print("Bem-vindo ao jogo Pokemon!")

        for i in range(3):
            pokemon = random.choice(self.biblioteca_pokemons)
            self.inimigo.capturar(pokemon)

        while True:
            print("\nOpções:")
            print("1. Ver Pokemons")
            print("2. Capturar Pokemon")
            print("3. Batalhar")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.jogador.listar_pokemons()
            elif escolha == "2":
                self.capturar_pokemon()
            elif escolha == "3":
                self.batalhar()
            elif escolha == "4":
                print("Fim do jogo.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def capturar_pokemon(self):
        pokemon = random.choice(self.biblioteca_pokemons)
        self.jogador.capturar(pokemon)
        print(f"{pokemon.nome} foi capturado!")

    def batalhar(self):
        print("Escolha o seu pokemon para a batalha:")
        self.jogador.listar_pokemons()
        escolha = int(input("Escolha um pokemon: ")) - 1
        pokemon_jogador = self.jogador.pokemons[escolha]
        pokemon_inimigo = random.choice(self.inimigo.pokemons)
        print(f"\nUm {pokemon_inimigo.nome} selvagem apareceu!")
        print("Batalha iniciada!")
        while pokemon_jogador.esta_vivo() and pokemon_inimigo.esta_vivo():
            print(f"\n{pokemon_jogador.nome} ({pokemon_jogador.vida} vida) vs {pokemon_inimigo.nome} ({pokemon_inimigo.vida} vida)")
            turno_jogador = input("É a sua vez. O que deseja fazer? (1 - atacar, 2 - fugir): ")
            if turno_jogador == "1":
                dano = pokemon_jogador.atacar(pokemon_inimigo)
                print(f"{pokemon_jogador.nome} causou {dano} de dano em {pokemon_inimigo.nome}!")
            elif turno_jogador == "2":
                print("Você fugiu da batalha!")
                return
            else:
                print("Opção inválida. Tente novamente.")
                continue

            if not pokemon_inimigo.esta_vivo():
                print(f"\n{pokemon_inimigo.nome} desmaiou!")
                print("Você venceu a batalha!")
                return

            turno_inimigo = random.choice(["1", "2"])
            if turno_inimigo == "1":
                dano = pokemon_inimigo.atacar(pokemon_jogador)
                print(f"{pokemon_inimigo.nome} causou {dano} de dano em {pokemon_jogador.nome}!")
            elif turno_inimigo == "2":
                print(f"{pokemon_inimigo.nome} fugiu da batalha!")
                return

            if not pokemon_jogador.esta_vivo():
                print(f"\n{pokemon_jogador.nome} desmaiou!")
                print("Você perdeu a batalha!")
                return
            
