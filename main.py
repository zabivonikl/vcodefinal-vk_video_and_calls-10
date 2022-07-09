import traceback
from threading import Thread

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from vk import Vk


kb = VkKeyboard()
kb.add_button("Звонок", VkKeyboardColor.POSITIVE)


def handler(incoming_event: dict):
    try:
        vk_id = str(incoming_event['from_id'])
        text: str = incoming_event["text"]
        if text == "Звонок":
            vk.send_message([vk_id], vk.create_call(), keyboard=kb)
        elif text == "Начать":
            vk.send_message([vk_id], "Чтобы начать вызов нажмите \"Звонок\"", keyboard=kb)
        else:
            vk.send_message([vk_id], "Недопустимая команда", keyboard=kb)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        traceback.print_tb(e.__traceback__)


if __name__ == "__main__":
    vk = Vk()
    while True:
        event = vk.listen_server()
        Thread(target=handler, args=(event['message'], )).start()

