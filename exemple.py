import os
from dotenv import load_dotenv
import openai

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("API key not found in .env file")
    return api_key

def create_env_file(api_key):
    with open(".env", "w") as env_file:
        env_file.write(f"OPENAI_API_KEY={api_key}\n")

def generate_response(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def main():
    print("Koneksi dengan OpenAI terhubung. Ketik 'exit' untuk keluar.\n")

    try:
        api_key = load_api_key()
    except ValueError:
        print("API key not found in .env file.\n")
        api_key = input("\nMasukkan API key Anda: ")
        create_env_file(api_key)
        print("\nAPI key telah disimpan dalam berkas .env")

    while True:
        user_input = input(" tanya: ")

        if user_input.lower() == 'exit':
            print("\nKoneksi dengan OpenAI terputus, sampai jumpa!\n")
            break

        prompt = f"Anda: {user_input}\nSaya:"
        try:
            response = generate_response(prompt, api_key)
            print(" balas:", response + "\n")
        except openai.error.AuthenticationError as auth_error:
            print("Terjadi kesalahan autentikasi:", auth_error)
            retry = input("Coba masukkan kunci API yang benar lagi? (y/n): ")
            if retry.lower() != 'y':
                break

if __name__ == "__main__":
    main()