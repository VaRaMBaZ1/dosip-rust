import socket
import random
import string
import asyncio

x = 1

async def generate_random_message(min_length=50, max_length=200):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    message = ''.join(random.choice(characters) for _ in range(length))
    return message

async def send_udp_message(host, port, message):
    global x
    try:
        # Создаем UDP-сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setblocking(False) # Делаем сокет неблокирующим

        # Отправляем сообщение
        sock.sendto(message.encode(), (host, port))

        x += 1
        print(f"UDP-сообщение отправлено {x} на {host}:{port}")

    except Exception as e:
        print(e)

    finally:
        # Закрываем сокет
        if sock:
            sock.close()

async def main(ip, port):
    while True:
        random_message = await generate_random_message()
        await send_udp_message(ip, port, random_message)

async def run_main(ip, port):
    await main(ip, port)

if __name__ == "__main__":
    ip = input("IP: ")
    port = int(input("PORT: "))
    asyncio.run(run_main(ip, port))
