# thonny-pico
Pico support for the Thonny IDE

Requires at least Thonny 3.3.0b6 (released at Oct 19th).

## Current state
* Aivar is happy with the new UI (backend switcher and firmware flasher).

### TODO
* Add Pico-specific MicroPython API stubs to support code-completion

## Easy installation

NB! Following works for Windows, macOS and Linux on x86_64 and i686 (binaries are published only for those
platforms). On Raspberry you need to use `apt update` and `apt upgrade` to get recently published 3.3.0 or pip (see next section) if you need a version which is not yet in RPi's apt repository. 

* Install Thonny+Python bundle from https://github.com/thonny/thonny/releases/tag/v3.3.0
* Download Pico back-end as plug-in: https://github.com/raspberrypi/thonny-pico/releases/download/v0.1-post/thonny_rpi_pico-0.1-py3-none-any.whl
* Start Thonny and go to "Tools => Manage plug-ins"
* Click the link under "Install from local file" and select the whl-file.
* When done, restart Thonny.

## Overview of the pip-based usage

* pip-install Thonny pre-release into a virtual environment (see below for Linux example)
* clone this repository into a local directory and add it to PYTHONPATH environment variable. Alternatively use "Tools => Manage plug-ins" as described in the previous section.
* run Thonny
* Plug in Pico (either with or without holding BOOTSEL)
* If you held BOOTSEL, wait until OS mounts the device
* Click the flat button in the lower-right corner of Thonny Window and select "MicroPython (Raspberry Pi Pico)"
* If Pico is in bootloader mode, Thonny will open MicroPython firmware installation dialog.
* If Pico already has MicroPython and is in normal mode, Thonny will show the REPL
* General MicroPython support is described here: https://github.com/thonny/thonny/wiki/MicroPython

Please find more details below!

## Installation commands for Linux
```
python3 -m venv thonny_venv
source thonny_venv/bin/activate
pip install --pre --no-cache-dir -U thonny
git clone https://github.com/raspberrypi/thonny-pico
export PYTHONPATH=thonny-pico
thonny
```

## Back-end switcher

This is new feature in Thonny 3.3b6. Previously the user could switch interpreters from "Run => Select interpreter". 
The problem is that the menu is not visible in simple mode and Thonny didn't have good place to display the description
of the current interpreter.

Now Thonny has a thin statusbar, which has a menu-button in its right end. The button displays the description 
of the currently selected interpreter. When you click on it, you'll get a list of other back-ends, which are relevant 
at current state (eg. Pico entry is shown only if Thonny sees its mounted volume in bootloader mode or its USB VID/PID).

The old way of switching interpreters will remain -- switcher button is just a more comfortable and more lightweight
alternative.


## Firmware installer
The dialog for installing MicroPython firmware can be opened from "Run => Select interpreter" or from the back-end 
switcher if the device is in bootloader mode.

In the future Thonny will depend on https://api.github.com/repos/raspberrypi/micropython/releases/latest 
to get the version number and download URL-s for the latest stable MicroPython firmware.

For testing I created a secret URL under https://thonny.org, which provides similar json file and uf2 file.
Thonny now first tries to contact https://api.github.com/repos/raspberrypi/micropython/releases/latest and 
if this gives 404, it falls back to https://thonny.org/45624345807/index.json 

