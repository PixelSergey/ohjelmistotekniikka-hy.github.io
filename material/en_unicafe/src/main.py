from payment_card import Maksukortti
from cash_register import Kassapaate


def main():
    unicafe_exactum = Kassapaate()
    kortti = Maksukortti(10000)

    unicafe_exactum.syo_edullisesti_kortilla(kortti)

    print(unicafe_exactum.edulliset)
    print(kortti)


if __name__ == "__main__":
    main()
