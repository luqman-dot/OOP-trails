class SmartHome:
    def __init__(self):
        self.devices = {
            "lights": {"status": "off", "brightness": 0},
            "thermostat": {"status": "off", "temperature": 22},
            "security": {"status": "disarmed", "camera": "off"}
        }

    def control_device(self, device, action, value=None):
        if device == "lights":
            if action.lower() == "on":
                self.devices["lights"]["status"] = "on"
                self.devices["lights"]["brightness"] = value if value is not None else 100
            elif action.lower() == "off":
                self.devices["lights"]["status"] = "off"
                self.devices["lights"]["brightness"] = 0
            print(f"Lights turned {action}. Brightness: {self.devices['lights']['brightness']}%")
        elif device == "thermostat":
            if action.lower() == "on":
                self.devices["thermostat"]["status"] = "on"
                self.devices["thermostat"]["temperature"] = value if value is not None else 22
            elif action.lower() == "off":
                self.devices["thermostat"]["status"] = "off"
            print(f"Thermostat turned {action}. Temperature: {self.devices['thermostat']['temperature']}°C")
        elif device == "security":
            if action.lower() == "arm":
                self.devices["security"]["status"] = "armed"
                self.devices["security"]["camera"] = "on" if value else "off"
            elif action.lower() == "disarm":
                self.devices["security"]["status"] = "disarmed"
                self.devices["security"]["camera"] = "off"
            print(f"Security system {action}. Camera: {self.devices['security']['camera']}")

    def show_status(self):
        print("\n--- Home System Status ---")
        for device, settings in self.devices.items():
            print(f"{device.capitalize()}: {settings}")

    def run_routine(self, routine):
        if routine.lower() == "morning":
            print("\nRunning 'Morning' routine...")
            self.control_device("lights", "on", 75)
            self.control_device("thermostat", "on", 21)
            self.control_device("security", "disarm")
        elif routine.lower() == "night":
            print("\nRunning 'Night' routine...")
            self.control_device("lights", "off")
            self.control_device("thermostat", "on", 18)
            self.control_device("security", "arm", True)
        else:
            print(f"Routine '{routine}' not recognized.")


# Main Program
if __name__ == "__main__":
    home = SmartHome()

    while True:
        print("\n--- Smart Home Menu ---")
        print("1. Control Lights")
        print("2. Control Thermostat")
        print("3. Control Security")
        print("4. Show System Status")
        print("5. Run Routine (Morning/Night)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            action = input("Turn lights 'on' or 'off': ")
            brightness = int(input("Set brightness (0-100): ")) if action.lower() == "on" else None
            home.control_device("lights", action, brightness)
        elif choice == "2":
            action = input("Turn thermostat 'on' or 'off': ")
            temperature = int(input("Set temperature (°C): ")) if action.lower() == "on" else None
            home.control_device("thermostat", action, temperature)
        elif choice == "3":
            action = input("Arm or disarm the security system: ")
            camera = input("Enable camera with 'arm'? (yes/no): ").lower() == "yes" if action.lower() == "arm" else None
            home.control_device("security", action, camera)
        elif choice == "4":
            home.show_status()
        elif choice == "5":
            routine = input("Enter routine ('morning' or 'night'): ")
            home.run_routine(routine)
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
