from thonny.plugins.micropython import (
    BareMetalMicroPythonProxy,
    add_micropython_backend,
    BareMetalMicroPythonConfigPage,
)


class RaspberryPiPicoBackendProxy(BareMetalMicroPythonProxy):
    @property
    def consider_unknown_devices(self):
        return False

    @property
    def known_usb_vids_pids(self):
        return {(0xF055, 0x9802)}


class RaspberryPiPicoBackendConfigPage(BareMetalMicroPythonConfigPage):
    pass


def load_plugin():
    add_micropython_backend(
        "RPiPico",
        RaspberryPiPicoBackendProxy,
        "MicroPython (Raspberry Pi Pico)",
        RaspberryPiPicoBackendConfigPage,
        bare_metal=True,
        sort_key="32",
    )
