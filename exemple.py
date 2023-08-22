import os
from dotenv import load_dotenv
import openai

# memuatkan api key dan membuat file baru
def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("API key not found in .env file")
    return api_key

#
def create_env_file(api_key):
    with open(".env", "w") as env_file:
        env_file.write(f"OPENAI_API_KEY={api_key}")

# yang memberi response bales pesan.
def generate_response(prompt, api_key):
    try:
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=1000,
          temperature=0.5,
      )
      return response.choices[0].text.strip()
    except openai.error.APIConnectionError as error:
        # print(f"Terjadi kesalahan saat berkomunikasi dengan OpenAI: {error}")
        # return "Mohon maaf, terjadi masalah dalam berkomunikasi dengan OpenAI."
        return "anda sedang offline..."

# menjalan program
def main():

    try:
        api_key = load_api_key()
    except ValueError:
        print("\nAPI key not found in .env file.")
        print("\ndapatkan link openai dari situs web resmi milik openai:\n- https://platform.openai.com/account/api-keys\n")
        api_key = input("Masukkan API key Anda: ")
        create_env_file(api_key)
        print("\nAPI key telah disimpan dalam berkas .env\n")

    print("\nProgramming python openai chat gpt.\n- Ketik 'exit' untuk keluar.\n- Ketik 'clear untuk menghapus riwayat.\n")

    while True:
        try:
          user_input = input("tanya: ")
        except KeyboardInterrupt:
          print("\nAnda telah meminta untuk keluar.\nSampai jumpa!")
          break

        if user_input.lower() == 'exit':
            print("\nkeluar dari programming python openai!")
            break
        elif user_input.lower() == 'clear':
            os.system("clear")
            print("\nProgramming python openai chat gpt.\n- Ketik 'exit' untuk keluar.\n- Ketik 'clear untuk menghapus riwayat.\n")
            continue

        prompt = f" Anda: {user_input}\n Saya:"

        try:
            response = generate_response(prompt, api_key)
            print("balas:", response + "\n")
        except openai.error.AuthenticationError as auth_error:
            print("\nTerjadi kesalahan autentikasi:", auth_error)
            retry = input("\nOops..., Coba masukkan kunci API yang benar lagi? (y/n): ")

            if retry.lower() == 'y':
                print("\ndapatkan link openai dari situs web resmi milik openai:\n- https://platform.openai.com/account/api-keys\n")
                api_key = input("Masukkan API key Anda: ")
                create_env_file(api_key)
                print("\nAPI key telah diperbarui dalam berkas .env\n")
                continue
            else:
                print("\nTerima kasih, sampai jumpa!")
                break

# menjalan program
if __name__ == "__main__":
    main()