import random

def get_user_choice():
    while True:
        user_choice = input("Escolha pedra (r), papel (p) ou tesoura (s): ")
        if user_choice.lower() in ['r', 'p', 's']:
            return user_choice.lower()
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def get_ai_choice():
    ai_choice = random.choice(['r', 'p', 's'])
    return ai_choice

def get_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "Empate"
    elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def play_game():
    print("Bem-vindo ao jogo Pedra, Papel ou Tesoura!")
    print("Você está jogando contra a IA.")
    print("-----------------------------------------")

    user_score = 0
    ai_score = 0

    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()

        print(f"Você escolheu: {user_choice}")
        print(f"A IA escolheu: {ai_choice}")

        winner = get_winner(user_choice, ai_choice)
        print(winner)

        if winner == "Você ganhou!":
            user_score += 1
        elif winner == "Você perdeu!":
            ai_score += 1

        print(f"Placar: Você {user_score} - {ai_score} IA")

        play_again = input("Deseja jogar novamente? (s/n): ")
        if play_again.lower() != 's':
            break

    print("Obrigado por jogar!")

# Inicia o jogo
play_game()
