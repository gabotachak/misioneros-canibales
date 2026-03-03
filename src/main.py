import time
from playwright.sync_api import sync_playwright, Page


def start_game(page: Page):
    """
    Ejecuta la secuencia de clics inicial para pasar las pantallas
    de introducción, menú principal e instrucciones del juego.
    """
    print("Navegando al juego local en http://localhost:8080 ...")
    page.goto("http://localhost:8080")

    print("Esperando a que cargue el iframe del juego...")
    # El script game.js inyecta un iframe
    page.wait_for_selector("iframe", state="attached", timeout=15000)

    # Damos tiempo a la pantalla inicial ("Your Logo") a renderizarse
    print("Esperando 5 segundos para que la pantalla inicial renderice...")
    time.sleep(5)

    print("Haciendo click en el botón de play inicial (pantalla 'Your Logo')...")
    logo_play_button_x = 500
    logo_play_button_y = 560
    print(f"Haciendo click en x: {logo_play_button_x}, y: {logo_play_button_y}")
    page.mouse.click(logo_play_button_x, logo_play_button_y)

    print("Esperando a que cambie la escena (Menú Principal)...")
    time.sleep(15)

    print("Haciendo click en el botón 'COMIENZO' (Menú Principal)...")
    comienzo_x = 500
    comienzo_y = 420
    print(f"Haciendo click en x: {comienzo_x}, y: {comienzo_y}")
    page.mouse.click(comienzo_x, comienzo_y)

    print("Esperando a que cargue la pantalla de Instrucciones...")
    time.sleep(3)

    print("Haciendo sweep vertical en el botón 'COMIENZO' (Instrucciones)...")
    comienzo_2_x = 500
    for comienzo_2_y in range(540, 660, 15):
        print(f"Probando click en x: {comienzo_2_x}, y: {comienzo_2_y}")
        page.mouse.click(comienzo_2_x, comienzo_2_y)
        time.sleep(0.2)

    print("Esperando a que cargue el nivel principal...")
    time.sleep(4)
    print("¡El nivel principal debería estar cargado!")


def main():
    print("🤖 Iniciando Agente para Misioneros y Caníbales con Playwright...")

    with sync_playwright() as p:
        # Lanzamos el navegador visible (headless=False)
        browser = p.chromium.launch(headless=False)

        # Creamos un contexto con un tamaño de viewport fijo para que las coordenadas de click sean predecibles
        context = browser.new_context(viewport={"width": 1000, "height": 700})
        page = context.new_page()

        # Separamos la lógica inicial en una función aparte
        start_game(page)

        input(
            "\n[Pausa] Revisa el navegador de Chromium. \n¿Avanzó al nivel con el río, los personajes y el bote?\nPresiona ENTER aquí para terminar este script..."
        )

        browser.close()


if __name__ == "__main__":
    main()
