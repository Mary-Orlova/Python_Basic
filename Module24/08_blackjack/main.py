from cards_players_deck import Player, Deck


def new_game():
    deck = Deck()
    player_hand = Player("Игрок")
    dealer_hand = Player("Диллер")

    player_hand.add_card(deck.deal_card())  # раздаем две карты игроку и 1 диллеру
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print(player_hand)

    in_game = True

    while player_hand.get_value() < 21:
        answer = input("Ещё или стоп? ").lower()
        if answer == "ещё" or answer == 'еще':
            player_hand.add_card(deck.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Вы проиграли - больше 21 очков.")
                in_game = False
        else:
            print("Вы сказали СТОП!")
            break
    print("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("Вы выиграли - у диллера больше 21 очка")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("Вы выиграли!")
        else:
            print("Диллер выиграл.")


new_game()
