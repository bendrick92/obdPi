## obdPi
A Python 2.7 project designed for the Raspberry Pi to output a vehicle's OBD-II data to a 16x2 character OLED display.

[![obdPi Preview](http://i.imgur.com/OEufVUv.png)](https://www.youtube.com/watch?v=kVyh6FTyh9E)

## Code

* /docs - Documentation files (see the [documentation](https://bendrick92.github.io/obdPi/wiring/) for latest version)
* /obdpi - Contains the modules for the project as '*_manager.py' files
* /tests - Contains unit tests for several of the modules
* main_oled.py - Main script to run for output to the OLED
* main_print.py - Secondary script to run for output to console (no OLED necessary)

## Documentation

See [https://bendrick92.github.io/obdPi](https://bendrick92.github.io/obdPi) for complete overview, setup, and usage information.

## To-do

- [ ] Update logging system to log multiple OBD-II parameters simultaneously
- [x] Update logging system to restrict number/age of logs saved
- [ ] Implement button-based switching of OBD-II commands
- [ ] Implement asynchronous OBD-II requests (via python-OBD)
- [ ] Implement serial/OBD-II connection retries when failing after initial connection

## Legal Stuff

This software is provided by the contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed.  In no event shall the contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

This software is experimental and the firmware images it produces carry possible risk to the stability and functionality of the devices they are installed on.  Any and all authors and contributors to the project shall not be liable for direct or indirect damage to devices as a result of the use of this software.

This software may only be used for legal, lawful purposes.  Any and all authors and contributors to the project are not responsible for the illegal or malicious use of this software, or any and all potential damages resulting from such wrongful use.
