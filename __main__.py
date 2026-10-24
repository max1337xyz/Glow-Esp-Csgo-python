import pymem
import pymem.process
from offsets import *
from tkinter import messagebox
import dearpygui.dearpygui as dpg


def glow_esp():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    messagebox.showinfo("Sucess","Glow Activate!")
    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow
           
def imgui():
    dpg.create_context()

    dpg.create_viewport(
        title="Glow ESP Menu",
        width=600,
        height=350
    )


    with dpg.window(
        label="Glow ESP",
        width=580,
        height=300
    ):

        dpg.add_text(
            "CS:GO",
            color=(0, 150, 255)
        )

        dpg.add_separator()

        dpg.add_text(
            "Glow"
        )

        dpg.add_spacing(count=2)

        dpg.add_button(label="Activate",callback=lambda:glow_esp())
    dpg.setup_dearpygui()

    dpg.show_viewport()

    dpg.start_dearpygui()

    dpg.destroy_context()
def main():
    imgui()
if __name__ == "__main__":
    main()