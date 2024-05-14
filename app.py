import random
import string 



def generate_password(length=8, uppercase=True, lowercase=True, digits=True, special_chars=True):
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    length = int(input("Digite o comprimento da senha: "))
    uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    digits = input("Incluir números? (s/n): ").lower() == 's'
    special_chars = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Sua senha gerada é:", password)

if __name__ == "__main__":
    main()